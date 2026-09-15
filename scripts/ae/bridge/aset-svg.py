"""Aset ilustrasi kartun panggung → SVG (vektor dari kode) → manifest penempatan untuk bridge AE.
Alur: tulis fungsi menggambar per aset → jalankan skrip ini → `node svg2png.cjs aset` (PNG 2× transparan)
→ di AE lewat bridge: import_image PNG, modify_layer anchor=manifest.anchor, position=manifest.pos,
scale=50, parentLayerName="CAM". Karakter TIDAK di sini — dibangun native lewat rig-tokoh.py.

pakai: python aset-svg.py            → menulis aset/*.svg + manifest.json (contoh panggung di bawah)
Ganti/isi bagian "# ---- aset ----" dengan panggung proyekmu; palet dari style brief.
"""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'aset'); os.makedirs(OUT, exist_ok=True)
PX = 2  # kerapatan render: PNG 2×, dipasang di AE dengan scale 50 %

# Palet contoh (kartun panggung: flat cerah, tanpa tekstur). Ganti dari style brief proyek.
PAL = dict(sky1='#CFE6E4', sky2='#FBF1DC', oker='#D9A066', oker2='#B97F4A', batu='#9C9186', batu2='#7D736A',
           rumput='#9DB874', rumput2='#7FA65E', api='#C8553D', api2='#F2C46D', tinta='#2F4858', kayu='#8A6A4A',
           krem='#FBF1DC', air='#5AABB8', air2='#9ED6DD', malam='#34505E')
C = PAL

class Shapes:
    """Kumpulan bentuk di koordinat lokal; (0,0) = pivot aset. Semua rantai (return self)."""
    def __init__(s): s.items = []; s.minx = s.miny = 1e9; s.maxx = s.maxy = -1e9
    def _box(s, pts):
        for x, y in pts:
            s.minx = min(s.minx, x); s.miny = min(s.miny, y); s.maxx = max(s.maxx, x); s.maxy = max(s.maxy, y)
    def rc(s, x, y, w, h, c, r=0, rot=0):
        a = math.radians(rot); ca, sa = math.cos(a), math.sin(a)
        s._box([(x + dx * ca - dy * sa, y + dx * sa + dy * ca) for dx in (-w / 2, w / 2) for dy in (-h / 2, h / 2)])
        s.items.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r:.1f}" '
                       f'fill="{C.get(c, c)}" transform="translate({x:.1f} {y:.1f}) rotate({rot})"/>')
        return s
    def el(s, x, y, w, h, c):
        s._box([(x - w / 2, y - h / 2), (x + w / 2, y + h / 2)])
        s.items.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{w/2:.1f}" ry="{h/2:.1f}" fill="{C.get(c, c)}"/>'); return s
    def pth(s, pts, c, smooth=0.0):
        """Poligon tertutup; smooth 0 = sudut tajam, 0.3–0.5 = bukit/batu membulat (Catmull-Rom → bezier)."""
        n = len(pts); T = []
        for k in range(n):
            a, b = pts[(k - 1) % n], pts[(k + 1) % n]
            T.append(((b[0] - a[0]) * smooth / 2, (b[1] - a[1]) * smooth / 2))
        d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
        for k in range(n):
            p0, p1 = pts[k], pts[(k + 1) % n]
            c1 = (p0[0] + T[k][0], p0[1] + T[k][1]); c2 = (p1[0] - T[(k + 1) % n][0], p1[1] - T[(k + 1) % n][1])
            d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p1[0]:.1f} {p1[1]:.1f}'
            s._box([c1, c2, p1])
        s.items.append(f'<path d="{d} Z" fill="{C.get(c, c)}"/>'); return s

MAN = {}
def asset(panggung, name, build, pivot=(0, 0)):
    """build(sh) menggambar di koordinat lokal dengan (0,0) = pivot; pivot = posisi di comp panggung (1920×1080).
    Manifest: png, pos (= pivot, comp), anchor (px sumber 2×), scale 50 — langsung dipakai modify_layer."""
    sh = Shapes(); build(sh); m = 6
    x0, y0 = math.floor(sh.minx - m), math.floor(sh.miny - m); w, h = math.ceil(sh.maxx + m) - x0, math.ceil(sh.maxy + m) - y0
    fn = f"{panggung.split()[0]}_{name.replace(' ', '-')}.svg"
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*PX}" height="{h*PX}" viewBox="{x0} {y0} {w} {h}">' + ''.join(sh.items) + '</svg>'
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(svg)
    MAN.setdefault(panggung, []).append(dict(name=name, svg=fn, png=fn.replace('.svg', '.png'), w=w * PX, h=h * PX,
                                            pos=[round(pivot[0], 1), round(pivot[1], 1)], anchor=[-x0 * PX, -y0 * PX], scale=100 / PX))

# ---- potongan yang sering dipakai (koordinat comp; pivot aset latar = (0,0)) ----
def bukit(sh, base, c='rumput'):
    sh.pth([(-400, base + 460), (-400, base), (100, base - 120), (520, base - 40), (900, base - 190), (1350, base - 70),
            (1760, base - 160), (2320, base - 30), (2320, base + 460)], c, 0.4)
def tanah(sh, gy, c='oker', rim='rumput2'):
    sh.rc(960, gy + 300, 2700, 600, c).rc(960, gy + 8, 2700, 22, rim)
def batu(sh, x, y, s=1.0, c='batu'):
    sh.pth([(x - 90 * s, y), (x - 70 * s, y - 55 * s), (x - 10 * s, y - 80 * s), (x + 60 * s, y - 60 * s), (x + 95 * s, y)], c, 0.5)
def pohon(sh, x, gy, s=1.0):
    sh.rc(x, gy - 90 * s, 34 * s, 190 * s, 'kayu', 10 * s).el(x - 60 * s, gy - 230 * s, 150 * s, 130 * s, 'rumput2') \
      .el(x + 55 * s, gy - 240 * s, 140 * s, 125 * s, 'rumput2').el(x, gy - 300 * s, 170 * s, 150 * s, 'rumput')
def api_layers(P, x, gy):
    """Api unggun = kayu + 3 lidah terpisah (agar tiap lidah bisa di-scale/rotate sendiri lewat expression)."""
    asset(P, 'api kayu', lambda sh: sh.rc(-60, 0, 150, 18, 'kayu', 8, -12).rc(60, 0, 150, 18, 'kayu', 8, 12), (x, gy))
    for k, (dx, w, h) in enumerate([(-28, 70, 170), (26, 60, 140), (0, 46, 100)]):
        asset(P, f'api lidah {k+1}', lambda sh, w=w, h=h: sh.el(0, -h / 2, w, h, 'api' if h > 120 else 'api2'), (x + dx, gy - 22))

# ---- aset (CONTOH satu panggung; ganti dengan panggung proyekmu) ----
P = 'P01 contoh'; gy = 860
asset(P, 'bukit jauh', lambda sh: bukit(sh, 700))
asset(P, 'tanah', lambda sh: tanah(sh, gy))
asset(P, 'pohon', lambda sh: pohon(sh, 0, 0, 1.1), (1500, gy))
asset(P, 'batu duduk', lambda sh: batu(sh, 0, 0, .9, 'batu2'), (560, gy + 20))
api_layers(P, 960, gy + 20)
asset(P, 'cahaya api', lambda sh: sh.el(0, 0, 900, 520, 'api2'), (960, gy - 60))   # di AE: opacity 30, dibuat sebelum tokoh

json.dump(MAN, open(os.path.join(HERE, 'manifest.json'), 'w', encoding='utf-8'), indent=1)
print(sum(len(v) for v in MAN.values()), 'aset di', len(MAN), 'panggung ->', OUT)
