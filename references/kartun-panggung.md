# Kartun panggung — explainer kartun edukasi flat, satu panggung per adegan

Gaya keenam explainer. Angka acuannya dari dua jenis video: cerita kartun ±40 dtk
dengan satu tokoh di lima lingkungan, dan explainer ±80 dtk (7 panggung, 2 tokoh,
tanpa caption). Kegagalan yang umum dicatat di bawah karena model mudah yakin
hasilnya sudah benar.

**Definisi.** Tiap adegan adalah *panggung* sendiri seukuran frame (1920×1080 +
overscan), digambar vektor, hidup penuh (≥10 benda bergerak), punya kamera sendiri.
Kamera hanya bergerak **di dalam** panggung (zoom 1,08–1,95, tidak pernah wide).
Antar panggung: **cut**, atau geser 96 px / 72 px dengan blur ≤10 px. VO membawa
kalimat; gambar membawa makna; **tidak ada caption**.

Bedakan dari mode lain di skill ini:

| | Kartun kolase (`starter-explainer-kartun`) | Kartun panggung (`starter-explainer-panggung`) |
|---|---|---|
| Dunia | satu kertas besar berisi cutout diam | banyak panggung, tiap panggung satu frame |
| Gerak utama | kamera menyusuri aset diam | isi panggung beraksi; kamera menemani |
| Pergantian adegan | push-through kamera | cut / geser 96 px |
| Latar | kertas krem + grain + noda | flat cerah, tanpa tekstur |
| Teks | kalimat + pill highlighter | nol caption; label diegetik saja |
| Aset | ilustrasi generate → cutout | vektor digambar + kepala raster bersendi |

## Hukum 1 — Satu panggung per adegan, kamera tidak pernah wide

Rencana kamera proyek acuan: 1,95 → 1,08 · 1,65 → 1,14 → 1,18 · 1,90 → 1,12 → 1,36 ·
1,45 → 1,57 → 1,17. **Tidak ada satu pun di bawah 1,08.** Karakter di close-up
mengisi ~55–65 % tinggi frame, di wide masih ~35 %.

Kegagalan nyata: dunia dibangun sebagai satu peta raksasa (20.000 px) yang
dijelajahi kamera dengan zoom 0,2–0,7. Semua bergerak, tapi separuh video jadi
miniatur — rumah sebesar ibu jari, tanah kosong 60 % layar. Itu tetap terasa
"slide dengan gambar kecil di tengah". Perbaikannya bukan tambal sulam: dunia
harus dipecah jadi panggung-panggung seukuran frame.

Pola kamera per panggung: **tahan 0,45–0,7 dtk → satu gerak per beat VO → tahan.**
Gerak yang sah: push-in ke objek (1,12 → 1,45), tilt ke atap / ke bawah tanah
dalam panggung yang sengaja dibuat lebih tinggi dari frame, mengikuti subjek
(lompatan: tinggi kamera mengikuti busur, framing longgar di udara). Zoom
diinterpolasi logaritmik supaya terasa rata.

## Hukum 2 — Kontinu di dalam panggung, cut di antaranya

Kalimat VO berganti ≠ panggung berganti. Selama hubungan ruang/sebab-akibatnya
masih membantu penonton, tetap di panggung yang sama dan ubah **aksinya**:
dinding terangkat memperlihatkan rak, jarum meter naik, lampu hijau menyala,
tanaman tumbuh berurutan. Pindah panggung hanya saat lokasi, skala, atau cara
menjelaskan memang berganti. Proyek acuan: 39,6 dtk = 5 panggung; 81 dtk = 7.

Transisi beraksen hanya pada perpindahan tempat yang sungguh-sungguh (2 dari 6
pergantian di proyek acuan), sisanya cut langsung. Angka yang terbukti:

```
keluar  0,28 dtk  offset = -d · q²        (q = 0→1)
cut
masuk   0,42 dtk  offset = +d · (1-q)³
d = 96 px horizontal atau 72 px vertikal, blur ≤ 10 px pada kontainer,
TANPA scale bump, TANPA garis-garis sapuan tambahan.
```

Offset diterapkan ke rig kamera panggung, bukan dengan menggeser frame yang
sudah di-crop. Jangan terbang lintas dunia 3 detik (naik ke langit, menyelam ke
bawah tanah, zoom keluar) — itu pola "tahan → pan jauh sambil zoom → cut → ulangi"
yang melelahkan.

Cut antar panggung **bukan** pelanggaran "Larangan struktural #1" di SKILL.md
selama tiap panggung hidup (isinya beraksi). Yang dilarang adalah gambar diam
yang di-fade.

## Hukum 3 — Tiap panggung ≥10 benda yang bergerak

Bukan hiasan: tiap benda menjelaskan tempat, kegiatan, atau hubungan. Contoh
yang terbukti: kipas berputar (`t·100°`), jarum meter bergoyang, lampu status
berdenyut, tetes air merambat **mengikuti jalur pipa** (parametrik
`getPointAtLength`, bukan dash-offset), riak sungai bergeser, asap/uap naik
dengan opacity berkeyframe, debu tertiup, burung melintas, jemuran bergoyang,
daun pohon bernapas, ayam berjalan dengan kaki bergerak, lampu rak menyala
berurutan lalu berkedip acak-deterministik, tanaman tumbuh lalu layu, retakan
menjalar (stroke-dashoffset), lapisan tanah menumpuk, muka air turun.

Partikel: **satu tween gerak + satu tween opacity berkeyframe**
(`keyframes:{opacity:[0,.9,.9,0]}`), keduanya `repeat:-1`. Dua tween opacity
tak-hingga pada elemen yang sama saling menimpa — uapnya tidak pernah muncul.

## Hukum 4 — Rig sendi, bukan gambar utuh

Gambar utuh tidak punya sendi. Hierarki yang terbukti (koordinat lokal, kaki di y=0):

```
root (pelvis di 0,-214)
├─ thigh_L/R  translate(±26,-214)   paha 118 → lutut di +102
│  └─ shin     translate(0,102)     betis 108 → mata kaki di +96
│     └─ foot  translate(0,96)
└─ torso       translate(0,-214)    badan -152..+8, leher -178..-138
   ├─ arm_R    translate(50,-126)   lengan atas 98 → siku +78    (digambar SEBELUM badan)
   │  └─ fore  translate(0,78)      lengan bawah 90 → pergelangan +74
   │     └─ hand translate(0,74)
   ├─ arm_L    (sama, -50; digambar SESUDAH badan)
   └─ head     translate(0,-160)    dagu di sendi leher, overlap 14 px ke leher
```

Idle yang membuat tokoh hidup tanpa "melakukan" apa-apa:
badan `±1,1° / 1,7 dtk`, kepala `±1,7° / 2,3 dtk`, lengan `±1–1,5° / 1,9 dtk`,
**kedip tiap ≈3,5 dtk selama 0,13 dtk** (offset per tokoh supaya tidak serempak).
Jalan: `step = sin(t·8)`; paha `step·15°`, betis `max(0,step)·18°`, badan
naik-turun `|step|·3–4 px`, **bayangan elips di kaki ikut bergeser**. Lompat: paha,
betis, lengan, bayangan (mengecil di udara) semua fungsi satu kurva `jump(t)`.
Aksi kecil di tiap kalimat: menunjuk (lengan atas 6° → -72° dalam 0,7 dtk),
melambai, menimba (lengan -62°/-10° yoyo 0,42 dtk + engkol `+=180°`), mengipas
wajah (lengan bawah -40° ↔ -70°, 0,35 dtk).

Ekspresi = tukar gambar kepala (senang / cemas / kaget), bukan morph. Kedip =
gambar kepala kedua dengan mata tertutup, opacity 0 → 1 → 0.

Bayangan kaki: elips `rx ≈ 72·skala, ry 16, opacity .13`, digambar **sebelum**
tokoh, ikut bergerak saat jalan.

## Hukum 5 — Transform ditulis manual; GSAP tidak boleh menyentuh sendi

Dua jebakan yang paling sering terjadi:

1. **`transformOrigin` GSAP pada SVG relatif ke bounding box**, dan bbox grup
   berubah saat anaknya bergerak. Akibatnya bahu, leher, poros kipas, kaki ayam
   — semuanya berputar di titik yang bergeser: kepala terlihat lepas, baling-baling
   melayang keluar dari porosnya, kaki tertinggal di belakang badan.
2. **Tween `x`/`y` GSAP pada grup yang sudah punya `translate(...)` menimpa
   translate itu** (nilai absolut, bukan tambahan). Tiang listrik lenyap, awan
   tidak pernah pindah.

Solusi (pola null-per-sendi): tiap sendi punya proxy `{tx,ty,x,y,r,sx,sy}` dan
atribut `transform` ditulis sendiri —

```js
function J(el,tx=0,ty=0){const j={el,tx,ty,x:0,y:0,r:0,sx:1,sy:1,
  apply(){el.setAttribute('transform',
    `translate(${j.tx+j.x},${j.ty+j.y}) rotate(${j.r}) scale(${j.sx},${j.sy})`);}};
  j.apply();return j;}
tl.to(j,{r:-62,duration:.42,onUpdate:j.apply},at);     // sumbu putar = titik asal lokal
```

Aturan turunannya: grup **penempatan** (`translate`) dan grup **yang
dianimasikan** selalu dua elemen berbeda. GSAP boleh langsung menyentuh
`opacity`, `attr`, dan `x/y` pada elemen **tanpa** transform (rect/circle
dengan `x/cx`), atau `scaleX/scaleY` pada elemen tunggal (bbox-nya tetap).

## Hukum 6 — Nol caption, teks hanya diegetik

Proyek acuan tidak punya satu pun kalimat di layar. Teks yang ada adalah bagian
dunia: papan "AIRLOCK", tabung "O2", plat "PUSAT DATA", papan "DIJUAL". Kalimat
VO tidak ditulis ulang di layar — kalau penonton butuh membaca, gambarnya yang
belum menjelaskan. Kalimat sorotan + pill highlighter milik mode kolase, bukan
mode ini.

## Hukum 7 — Palet cerah flat; bukan kertas, bukan grain

Kertas krem + grain + noda air adalah kulit *kartun kolase* — di mode ini
terlihat vintage dan salah. Yang terbukti: langit gradien pucat
(`#BFDDE3 → #F6EFDD` atau `#EDB095 → #F8D8AD`), tanah `#D88560`/`#E6D5AC`, krem
`#FFF3DC`, navy `#345867`, teal `#237C80`, mint `#8DD3C3`, emas `#F4BC52`, koral
`#E0714F`. Flat fill, tanpa outline, tanpa tekstur, tanpa vignette. Bayangan hanya
elips kontak di tanah dan sisi gelap bangunan 0,86–0,9× warna dasar. Pilih palet
dari tema tetap berlaku (Hukum #3 SKILL.md) — yang dikunci di sini hanya
**tanpa tekstur**.

## Karakter: kepala raster + tubuh vektor

Pipeline yang terbukti (identitas boleh dari foto user, boleh anonim):

1. **Generate hanya KEPALA** (satu gambar, latar transparan). Prompt yang
   berhasil (tanpa menyebut merek apa pun):
   > ONE isolated front-facing cartoon HEAD, centered, generous margin. No body,
   > no neck below the jaw, no shoulders, no text. VERY MINIMAL flat 2D
   > educational-cartoon style: broad softly rounded head, simple small ears,
   > hair as ONE solid silhouette (no strands, no highlights), eyes ONLY TWO
   > SMALL SOLID BLACK DOTS (no sclera, iris, highlights, eyelids), two tiny
   > eyebrow strokes, nose omitted, mouth a tiny curved smile line. Flat fills,
   > ~3 colors, no gradients, no outlines, no shading. A clean silhouette for a
   > cutout animation puppet.
   Tambahkan ciri identitas (warna kulit, model rambut, kacamata, hijab polos
   satu warna) sebagai kalimat terpisah.
2. **Ekspresi & kedip dibuat lokal** — `scripts/kepala-ekspresi.py`: deteksi dua
   pupil (komponen gelap hampir persegi di tengah wajah) dan mulut (komponen
   lebar-tipis di bawahnya), lalu gambar ulang: kedip = elips kulit + garis
   lengkung; cemas = mulut cekung; kaget = lingkaran. Menghasilkan
   `<nama>-{senang,cemas,kaget}[-kedip].png` + `kepala-meta.json` (bbox, pupil,
   warna kulit). Tidak ada generate ulang untuk ekspresi.
3. **Tubuh digambar vektor** dengan hierarki Hukum 4; kepala ditempel di sendi
   leher dengan `<image>` yang dagunya (bawah bbox) tepat di (0,0) dan overlap
   14 px ke leher. Lebar kepala ≈ 150 px pada badan selebar 130 px.
4. Semua variasi kostum (baju, celana, gaun) lewat warna & path tubuh; kepala
   yang sama dipakai ulang. Master yang disetujui dibekukan.

Tanpa akses generate: `character()` di starter punya kepala vektor sederhana
(lingkaran kulit, siluet rambut, dua titik mata, garis mulut) — cukup untuk
gaya ini.

## Panggung yang terbukti untuk cerita "proses & dampak"

Halaman rumah (tokoh + ponsel, balon respons, sinyal terbang) · eksterior mesin
besar (push-in → dinding terangkat → isi menyala → tilt ke atap) · pabrik tepi
sungai (dua arah aliran + panah lingkaran) · menara & langit (panggung tinggi:
tilt mengikuti uap ke awan, hujan, angin) · sumur & penampang tanah (permukaan
di y≈520, lapisan menumpuk, akuifer, pipa penyedot berlabel) · tanah kering &
kemarau (matahari naik, retakan, tanaman layu, tokoh mengipas) · peta petak sawah
(grid terisi air berurutan, pita hujan bergeser) · kembali ke panggung
sebelumnya dengan kamera lebih dekat sebagai penutup.

Skala tinggi karakter ≈ 520 px pada skala 1 (kepala 186 + badan). Panggung
dengan bawah tanah: tinggi tokoh 0,85 dan lapisan ≤ 440 px supaya kepala dan
akuifer muat satu frame pada zoom 1,08.

## Verifikasi

Potret 20–24 detik kunci (`scripts/snap.mjs`) → lembar kontak 4 kolom, lalu
nilai dengan mata: **ada frame yang wide?** kepala/menara terpotong? tokoh
"lepas" di sendi? benda yang seharusnya muncul tidak ada (tanda tween menimpa
translate)? Untuk sekuens kontinu, render GIF 8 fps satu panggung penuh —
bukan montase — untuk membuktikan tidak ada patahan. Selain itu cek mekanis:
`grep` tidak ada `transformOrigin:'0px 0px'` / `rotation:` pada sendi, dan tidak
ada `tl.to(<grup ber-translate>,{x|y})`.
