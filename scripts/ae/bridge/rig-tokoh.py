"""Rig karakter native untuk bridge AE (lihat references/ae-bridge-higgsfield.md).
Setelah op ini: modify_layer "<p> ROOT" parentLayerName "CAM", lalu set ulang position/scale ROOT (parent ke CAM berkeyframe membakar transform).

Rig manusia gua native (shape layer + null sendi) → daftar op ae_batch.
Pola yang terbukti di bridge: buat shape di posisi comp → set anchor di titik sendi + posisi = titik sendi →
parent (lompatan menjaga posisi). Rotasi sendi lalu berputar tepat di sendinya.

pakai: python rig-tokoh.py "<comp>" <prefix> <x> <gy> <skala> [varian]   → mencetak JSON ops
varian: utama (berjanggut, tunik bulu), anggota1..3 (warna/rambut berbeda)
Hierarki: <p> ROOT(null, pelvis) → paha → betis → kaki ; ROOT → torso → lengan → lengan bawah → tangan ; torso → kepala → rambut/mata/alis/mulut/janggut
"""
import json, sys

def col(h): h = h.lstrip('#'); return {"r": round(int(h[0:2], 16) / 255, 3), "g": round(int(h[2:4], 16) / 255, 3), "b": round(int(h[4:6], 16) / 255, 3)}
VAR = {
    'utama':    dict(kulit='#C98B5E', kulit2='#B07650', tunik='#A9724A', tunik2='#8C5A36', rambut='#3B2A20', janggut=True),
    'anggota1': dict(kulit='#D39A6A', kulit2='#B9835A', tunik='#7F8F5A', tunik2='#66744A', rambut='#2F2620', janggut=False),
    'anggota2': dict(kulit='#B8784E', kulit2='#9E6644', tunik='#C8553D', tunik2='#A84634', rambut='#4A3325', janggut=False),
    'anggota3': dict(kulit='#C48A5C', kulit2='#AA744E', tunik='#9C9186', tunik2='#7D736A', rambut='#2B2B2B', janggut=True),
}

def rig(comp, p, x, gy, s, var='utama'):
    V = VAR[var]; ops = []
    def add(name, shape, cx, cy, w, h, c, r=0):
        ops.append({"tool": "add_shape_layer", "input": {"compositionName": comp, "name": f"{p} {name}", "shapeType": shape,
                    "size": [round(w * s, 1), round(h * s, 1)], "position": [round(cx, 1), round(cy, 1)], "fillColor": col(c),
                    **({"roundness": round(r * s, 1)} if shape == 'rectangle' and r else {})}})
    def joint(name, ax, ay, jx, jy):
        """anchor (koordinat layer, relatif pusat bentuk) + posisi titik sendi di comp."""
        ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} {name}",
                    "anchorPoint": [round(ax * s, 1), round(ay * s, 1)], "position": [round(jx, 1), round(jy, 1)]}})
    def parent(child, par):
        ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} {child}", "parentLayerName": f"{p} {par}"}})
    X = lambda dx: x + dx * s
    Y = lambda dy: gy + dy * s        # dy negatif = ke atas dari telapak
    pel = (X(0), Y(-214))
    # ---- ROOT ----
    ops.append({"tool": "add_null_layer", "input": {"compositionName": comp, "name": f"{p} ROOT"}})
    ops.append({"tool": "modify_layer", "input": {"compositionName": comp, "layerName": f"{p} ROOT", "anchorPoint": [50, 50], "position": [round(pel[0], 1), round(pel[1], 1)]}})
    # ---- kaki belakang (R) lalu depan (L) — urutan buat = urutan tumpuk (yang dibuat terakhir di atas) ----
    order = []
    for side, dx, shade in (('R', 24, 'kulit2'), ('L', -24, 'kulit')):
        hip = (X(dx), Y(-214)); knee = (X(dx), Y(-112)); ank = (X(dx), Y(-16))
        add(f'kaki-{side}', 'rectangle', ank[0] + 12 * s, ank[1] + 6 * s, 64, 26, '#5A3E2B', 12); joint(f'kaki-{side}', -12, -6, ank[0], ank[1])
        add(f'betis-{side}', 'rectangle', knee[0], knee[1] + 50 * s, 38, 110, V[shade], 18); joint(f'betis-{side}', 0, -50, knee[0], knee[1])
        add(f'paha-{side}', 'rectangle', hip[0], hip[1] + 52 * s, 46, 118, V[shade], 22); joint(f'paha-{side}', 0, -52, hip[0], hip[1])
        order += [(f'kaki-{side}', f'betis-{side}'), (f'betis-{side}', f'paha-{side}'), (f'paha-{side}', 'ROOT')]
    # ---- lengan belakang (R) ----
    sh_r = (X(52), Y(-340)); el_r = (X(52), Y(-262)); wr_r = (X(52), Y(-190))
    add('tangan-R', 'ellipse', wr_r[0], wr_r[1] + 8 * s, 34, 40, V['kulit2']); joint('tangan-R', 0, -8, wr_r[0], wr_r[1])
    add('lenganbawah-R', 'rectangle', el_r[0], el_r[1] + 36 * s, 30, 86, V['kulit2'], 15); joint('lenganbawah-R', 0, -36, el_r[0], el_r[1])
    add('lengan-R', 'rectangle', sh_r[0], sh_r[1] + 38 * s, 34, 96, V['kulit2'], 17); joint('lengan-R', 0, -38, sh_r[0], sh_r[1])
    # ---- torso: tunik bulu + tali bahu ----
    add('torso', 'rectangle', X(0), Y(-290), 136, 190, V['tunik'], 48); joint('torso', 0, 76, X(0), Y(-214))
    add('tunik-rumbai', 'rectangle', X(0), Y(-205), 150, 40, V['tunik2'], 18); joint('tunik-rumbai', 0, 0, X(0), Y(-205))
    add('leher', 'rectangle', X(0), Y(-388), 34, 40, V['kulit'], 12); joint('leher', 0, 0, X(0), Y(-388))
    # ---- kepala ----
    nk = (X(0), Y(-398))
    add('kepala', 'ellipse', X(0), Y(-470), 150, 162, V['kulit']); joint('kepala', 0, 72, nk[0], nk[1])
    add('telinga', 'ellipse', X(-70), Y(-468), 30, 40, V['kulit2']); joint('telinga', 0, 0, X(-70), Y(-468))
    for k, (dx, dy, w, h) in enumerate([(-48, -540, 80, 70), (0, -556, 96, 74), (48, -540, 80, 70), (-66, -505, 40, 60), (66, -505, 40, 60)]):
        add(f'rambut-{k+1}', 'ellipse', X(dx), Y(dy), w, h, V['rambut']); joint(f'rambut-{k+1}', 0, 0, X(dx), Y(dy))
    if V['janggut']:
        add('janggut', 'ellipse', X(0), Y(-408), 118, 70, V['rambut']); joint('janggut', 0, 0, X(0), Y(-408))
    for side, dx in (('L', -28), ('R', 28)):
        add(f'mata-{side}', 'ellipse', X(dx), Y(-472), 16, 20, '#23201C'); joint(f'mata-{side}', 0, 0, X(dx), Y(-472))
        add(f'alis-{side}', 'rectangle', X(dx), Y(-500), 30, 8, V['rambut'], 4); joint(f'alis-{side}', 0, 0, X(dx), Y(-500))
    add('hidung', 'ellipse', X(4), Y(-450), 26, 22, V['kulit2']); joint('hidung', 0, 0, X(4), Y(-450))
    add('mulut', 'rectangle', X(2), Y(-422), 34, 9, '#5A2E24', 5); joint('mulut', 0, 0, X(2), Y(-422))
    # ---- lengan depan (L) ----
    sh_l = (X(-52), Y(-340)); el_l = (X(-52), Y(-262)); wr_l = (X(-52), Y(-190))
    add('tangan-L', 'ellipse', wr_l[0], wr_l[1] + 8 * s, 34, 40, V['kulit']); joint('tangan-L', 0, -8, wr_l[0], wr_l[1])
    add('lenganbawah-L', 'rectangle', el_l[0], el_l[1] + 36 * s, 30, 86, V['kulit'], 15); joint('lenganbawah-L', 0, -36, el_l[0], el_l[1])
    add('lengan-L', 'rectangle', sh_l[0], sh_l[1] + 38 * s, 34, 96, V['tunik'], 17); joint('lengan-L', 0, -38, sh_l[0], sh_l[1])
    # ---- parenting (anak dulu, lalu induk ke induk) ----
    order += [('tangan-R', 'lenganbawah-R'), ('lenganbawah-R', 'lengan-R'), ('lengan-R', 'torso'),
              ('tangan-L', 'lenganbawah-L'), ('lenganbawah-L', 'lengan-L'), ('lengan-L', 'torso'),
              ('tunik-rumbai', 'torso'), ('leher', 'torso'), ('kepala', 'torso'), ('telinga', 'kepala'), ('hidung', 'kepala'), ('mulut', 'kepala')]
    order += [(f'rambut-{k+1}', 'kepala') for k in range(5)] + [(f'mata-{sd}', 'kepala') for sd in 'LR'] + [(f'alis-{sd}', 'kepala') for sd in 'LR']
    if V['janggut']: order.append(('janggut', 'kepala'))
    order.append(('torso', 'ROOT'))
    for c_, p_ in order: parent(c_, p_)
    return ops

if __name__ == '__main__':
    comp, p, x, gy, s = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    var = sys.argv[6] if len(sys.argv) > 6 else 'utama'
    ops = rig(comp, p, x, gy, s, var)
    print(json.dumps(ops, separators=(',', ':')))
    print(len(ops), 'ops', file=sys.stderr)
