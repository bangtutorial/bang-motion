"""
Ekspresi & kedip untuk kepala kartun hasil generate — dibuat LOKAL, tanpa generate ulang.

Masukan : PNG kepala (latar transparan) gaya flat: dua titik mata hitam, mulut garis.
Keluaran: <nama>-senang.png, -cemas.png, -kaget.png, masing-masing + varian -kedip.png,
          dan kepala-meta.json (bbox kepala, posisi pupil, kotak mulut, warna kulit).

Cara:
  python kepala-ekspresi.py karakter/kepala-pria.png karakter/kepala-wanita.png
  (nama keluaran diambil dari nama berkas setelah "kepala-", atau nama berkasnya)

Deteksi: komponen gelap (max RGB < 90, alpha > 180) → dua komponen kecil hampir persegi di
tengah wajah = pupil; komponen lebar-tipis di bawah pupil = mulut. Warna kulit disampel di
antara mata dan mulut. Kedip = elips kulit menutup pupil + garis lengkung. Cemas = mulut
cekung. Kaget = lingkaran. Semua ukuran relatif ke ukuran pupil/mulut yang terdeteksi.
Butuh: Pillow, numpy, opencv-python.
"""
import sys, json, os
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np, cv2

INK = (35, 32, 28, 255)

def bez(d, p, color, width):
    pts = []
    for t in np.linspace(0, 1, 50):
        q = (1-t)**3*np.array(p[0]) + 3*(1-t)**2*t*np.array(p[1]) + 3*(1-t)*t*t*np.array(p[2]) + t**3*np.array(p[3])
        pts.append(tuple(q))
    d.line(pts, fill=color, width=width, joint='curve')

def process(path):
    path = Path(path)
    name = path.stem[len('kepala-'):] if path.stem.startswith('kepala-') else path.stem
    im = Image.open(path).convert('RGBA'); px = np.array(im); H, W = px.shape[:2]
    alpha = px[:, :, 3]; ys, xs = np.where(alpha > 10)
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    dark = ((px[:, :, :3].max(2) < 90) & (alpha > 180)).astype('uint8')
    n, lab, st, cen = cv2.connectedComponentsWithStats(dark)
    comps = [(i, st[i], cen[i]) for i in range(1, n) if st[i, 4] > 60]
    eyes = [c for c in comps if 12 < c[1][2] < 80 and 12 < c[1][3] < 80
            and abs(c[1][2]-c[1][3]) < c[1][2]*.5 and H*.35 < c[2][1] < H*.75]
    eyes = sorted(sorted(eyes, key=lambda c: c[1][4], reverse=True)[:2], key=lambda c: c[2][0])
    assert len(eyes) == 2, f'{name}: pupil tidak terdeteksi 2 buah — cek gaya kepalanya (dua titik mata solid)'
    ey = float(np.mean([c[2][1] for c in eyes])); ex = float(np.mean([c[2][0] for c in eyes]))
    mouth = [c for c in comps if c[2][1] > ey+20 and c[1][2] > c[1][3]*1.6 and c[1][2] < W*.4]
    assert mouth, f'{name}: mulut tidak terdeteksi'
    mx0, my0, mw, mh = [int(v) for v in sorted(mouth, key=lambda c: c[1][4], reverse=True)[0][1][:4]]
    sy, sx = int((ey+my0)/2), int(ex); skin = tuple(int(v) for v in px[sy, sx])
    if skin[3] < 200: skin = (200, 140, 100, 255)
    meta = {'size': [W, H], 'bbox': bbox,
            'eyes': [[float(c[2][0]), float(c[2][1]), int(max(c[1][2], c[1][3]))] for c in eyes],
            'mouth': [mx0, my0, mw, mh], 'skin': list(skin[:3])}
    out_dir = path.parent
    for expr in ['senang', 'cemas', 'kaget']:
        for blink in [False, True]:
            out = im.copy(); d = ImageDraw.Draw(out)
            if blink:
                for cx, cy, sz in meta['eyes']:
                    r = sz*.75; d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=skin)
                    bez(d, [(cx-sz*.9, cy), (cx-sz*.35, cy+sz*.45), (cx+sz*.35, cy+sz*.45), (cx+sz*.9, cy)], INK, max(4, int(sz*.28)))
            if expr != 'senang':
                pad = int(mh*.9); d.rectangle((mx0-pad, my0-pad, mx0+mw+pad, my0+mh+pad), fill=skin)
                cx, cy, w = mx0+mw/2, my0+mh/2, max(4, int(mh*.9))
                if expr == 'cemas':
                    bez(d, [(cx-mw*.45, cy+mh*.4), (cx-mw*.15, cy-mh*.9), (cx+mw*.15, cy-mh*.9), (cx+mw*.45, cy+mh*.4)], INK, w)
                else:
                    rr = mh*1.1; d.ellipse((cx-rr*.8, cy-rr, cx+rr*.8, cy+rr), fill=INK)
            out.save(out_dir / f'{name}-{expr}{"-kedip" if blink else ""}.png')
    return name, meta

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    metas = {}
    for f in sys.argv[1:]:
        name, meta = process(f); metas[name] = meta; print(name, 'bbox', meta['bbox'], 'pupil', [e[:2] for e in meta['eyes']])
    out = Path(sys.argv[1]).parent / 'kepala-meta.json'
    old = json.load(open(out)) if out.exists() else {}
    old.update(metas); json.dump(old, open(out, 'w'), indent=1)
    print('->', out)
