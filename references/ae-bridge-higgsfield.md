# After Effects lewat bridge Higgsfield — membangun kartun panggung langsung di AE

Dibaca bila user sudah membuka proyek After Effects dan bridge Higgsfield (MCP `ae_*`)
tersambung, lalu meminta explainer dibangun **langsung di AE**. Angka acuan dari satu
build explainer kartun panggung (103 dtk VO, 10 panggung, 20 karakter bersendi, 96 aset
PNG): ±67 menit dari comp master sampai contact sheet terakhir, ±100 panggilan tool AE,
0 kredit Higgsfield. Hukum gaya tetap dari `kartun-panggung.md`; dokumen ini hanya
soal CARA membangunnya lewat bridge.

## Apa yang bisa dan tidak bisa dilakukan bridge

| Bisa | Tidak bisa (dan jalan keluarnya) |
|---|---|
| `ae_build_scene_from_lottie` membuat comp + precomp + layer shape sederhana sekaligus | Lottie besar (>~60 KB) — pecah: Lottie hanya untuk **kerangka**, isi lewat op atomik |
| `ae_batch` menjalankan puluhan op (`add_shape_layer`, `add_null_layer`, `import_image`, `modify_layer`, `set_keyframes`, `set_expression`) dalam satu panggilan | `apply_gradient`, `get_layer_info`, `export_frame` di dalam batch → seluruh batch error; panggil standalone |
| `add_shape_layer` rectangle (dengan `roundness`) dan ellipse, warna `{r,g,b}` 0–1 | Path/poligon/bintang, stroke, gradient pada shape → gambar sebagai SVG di luar, render ke PNG, impor |
| `ae_import_image` PNG/JPG/WAV (WAV memberi peringatan "hidden property" yang tidak berbahaya) | SVG ("invalid file type"); file di folder sementara/virtual milik aplikasi agent sering tidak terlihat oleh AE → salin aset dulu ke folder biasa (mis. `C:/aset-ae/`) |
| `ae_apply_gradient` Gradient Ramp 2 stop / 4-Color pada shape statis (langit) | Gradient di layer berkeyframe; gradient di dalam batch |
| `set_expression` pada Position/Scale/Rotation/Opacity/Anchor | Expression pada properti efek atau path; `ae_reorder_layers` selalu "layer not found" → **urutan tumpuk = urutan pembuatan**, buat dari belakang ke depan |
| `ae_export_contact_sheet` (5–8 waktu) dan `ae_export_frame` → URL r2.dev | Melihat URL r2.dev dari Indonesia (diblokir) → relay: `media_import_url(url)` di MCP Higgsfield → `curl https://d2ol7oe51mr4n9.cloudfront.net/<user>/<media_id>.png` → Read. Relay kadang gagal ("Something went wrong"); ekspor ulang, URL baru biasanya lolos |
| `ae_get_layer_info`, `ae_list_layers`, `ae_list_compositions` untuk verifikasi angka | Menyimpan proyek, merender, menghapus comp. User harus **Ctrl+S**; MP4 lewat Render Queue atau `aerender.exe` |

Jebakan bridge yang paling sering terjadi:

1. **Null baru lahir di (960,540).** `add_null_layer` lalu langsung di-parent-kan →
   semua anak yang belum berkeyframe melompat −960,−540. Segera `modify_layer`
   anchorPoint `[0,0]` + position `[0,0]` pada null itu SEBELUM parenting apa pun.
2. **Parenting ke CAM yang sudah berkeyframe** membakar transform CAM ke anak: posisi
   ikut tergeser, skala ikut mengecil. Setelah parent, set ulang position/scale anak
   secara eksplisit (atau parent dulu, animasikan CAM belakangan).
3. **Keyframe pada layer ber-parent memakai ruang induk.** Mata di dalam kepala bukan
   `[932,472]` (comp) tapi `[-28,-2]` (relatif pusat kepala). Salah ruang = bagian
   wajah terlempar ke luar frame.
4. **Batch parsial.** Bila satu op gagal dengan `stopOnError:false`, op lain tetap
   diterapkan; baca `results[i].ok` satu per satu, jangan mengulang seluruh batch.
5. **Lottie: posisi anak ditulis di ruang comp**, bukan relatif induk; converter juga
   membuat comp duplikat bila nama sama dan membuang gradient/gambar/mask/expression.
   `ip/op/st` pada layer precomp diterjemahkan benar — gunakan itu untuk timing master.
6. **Contact sheet di dalam precomp yang di-zoom master tampak buram** → kamera bukan di
   layer precomp master, tapi null `CAM` di dalam tiap panggung.

## Arsitektur yang terbukti

```
# <judul>                     comp master 1920×1080 30fps, durasi = VO
├─ VO (wav)                   detik 0
└─ > P01 … > P10              layer precomp, ip/op dari jeda VO, st = ip (lokal mulai 0)
     ### P01 <nama panggung>  precomp, durasi = segmen + 0,6 dtk (P04 +8 dtk bila dipakai ulang sebagai penutup)
     ├─ langit                rect seukuran comp dari Lottie → ae_apply_gradient
     ├─ CAM                   null, anchor [0,0] pos [0,0]; SEMUA layer dunia di-parent ke sini
     ├─ bukit, tanah, …       PNG 2× dari SVG, scale 50, anchor dari manifest, pos = pivot comp
     ├─ <tokoh> ROOT + 29 bagian   shape asli AE (lihat rig)
     └─ lapisan gelap/pagi/api  PNG/rect overlay, dibuat TERAKHIR (paling atas), opacity berkeyframe
```

**Kamera = null CAM.** Untuk melihat titik (x,y) pada zoom z:
`CAM.Position = [960 − x·z, 540 − y·z]`, `CAM.Scale = [100z, 100z]`. Keyframe dengan
`influence` 50–75 untuk ease. Zoom tidak pernah < 1,08 (Hukum 1 kartun panggung).

**Comp dipakai ulang sebagai panggung lain** (penutup memakai panggung api unggun):
layer precomp kedua di master dengan `st` = ip − waktu_lokal_mulai; animasi bagian
penutup ditaruh di waktu lokal itu (contoh: 13 dtk), dipisah dari adegan pertama dengan
keyframe hold ganda (12,93 → 12,967) supaya tidak ada interpolasi antar adegan.

**Aksen geser 96 px** (satu kali, pergantian zaman): keyframe Position layer precomp di
master — P08 960→864 (0,3 dtk, influence 70→10), P09 1056→960 (0,4 dtk, influence 10→80);
tambah Scale 100→111 dan 111→100 di waktu yang sama supaya tepi comp tidak terbuka.

## Alur kerja

0. Rundown per panggung dikunci ke jeda VO (`vo-pauses.html` atau `ffmpeg silencedetect`),
   plus daftar kamera per panggung `(t, x, y, z)`. Style brief kartun panggung tetap wajib.
1. **Kerangka lewat satu Lottie kecil**: comp master + tiap precomp berisi hanya layer
   `langit`, layer precomp di master dengan `ip/op/st`. Impor WAV VO ke master.
2. **Aset ilustrasi dari kode** (`scripts/ae/bridge/aset-svg.py`): tiap aset = satu
   fungsi menggambar (rect/ellipse/path halus) di koordinat lokal dengan pivot yang
   ditentukan; skrip menulis SVG + `manifest.json` berisi `png, pos, anchor(px 2×),
   scale 50`. Render semua dengan `node scripts/ae/bridge/svg2png.cjs <folder>`
   (puppeteer, PNG transparan seukuran SVG 2×). Gambar sesuai zona kamera: yang di
   luar zoom ≥1,08 tidak perlu digambar.
3. **Per panggung, satu `ae_batch`** urut belakang → depan:
   `add_null_layer CAM` → `modify_layer` CAM anchor/pos 0 → `import_image` + `modify_layer`
   (anchor, position, scale 50, opacity awal) per aset → `modify_layer parentLayerName:"CAM"`
   untuk semua → `set_keyframes` kamera & aset → `set_expression` gerak idle.
   `ae_apply_gradient` langit dipanggil terpisah SEBELUM batch.
4. **Karakter**: `python scripts/ae/bridge/rig-tokoh.py "<comp>" <prefix> <x> <gy> <skala> [varian]`
   mencetak ±90 op; tambahkan `modify_layer <prefix> ROOT parentLayerName CAM` dan set
   ulang ROOT position/scale (jebakan 2). Kirim sebagai satu `ae_batch` per karakter
   (±15 KB). Setelah rig jadi, batch kedua berisi pose/aksi + expression idle.
5. **Verifikasi tiap panggung** dengan `ae_export_contact_sheet` 5–8 waktu kunci → relay
   → lihat. Cek: rig utuh (sendi tidak lepas), latar tidak bergeser (jebakan 1–2),
   overlay di atas, ≥10 benda bergerak. Terakhir contact sheet **master** di satu waktu
   per panggung + waktu transisi.
6. **Penyerahan**: minta user Ctrl+S (bridge tidak bisa simpan), hapus comp uji coba,
   render lewat Render Queue atau
   `"C:/Program Files/Adobe/Adobe After Effects 2026/Support Files/aerender.exe" -project … -comp "# …" -output ….mp4`.
   Sebutkan kompromi yang tersisa (contoh: urutan layer yang tidak bisa disusun ulang).

## Rig karakter native (`rig-tokoh.py`)

Pola yang terbukti: **buat shape di posisi comp → `modify_layer` anchor = titik sendi
(koordinat layer, relatif pusat bentuk) + position = titik sendi (comp) → parent**.
Parenting "melompat" menjaga tampilan, dan Rotation berputar tepat di sendi.

```
<p> ROOT (null, pelvis = gy − 214s, anchor [50,50])
├─ paha-L/R (anchor [0,−52s], sendi pinggul ±24s) → betis (lutut gy−112s) → kaki (mata kaki gy−16s)
└─ torso (anchor [0,76s], sendi pelvis)
   ├─ lengan-L/R (bahu ±52s, gy−340s) → lenganbawah (siku gy−262s) → tangan (pergelangan gy−190s)
   ├─ tunik-rumbai, leher
   └─ kepala (anchor [0,72s], leher gy−398s)
      └─ telinga, rambut-1..5, janggut (varian utama/anggota3), mata-L/R, alis-L/R, hidung, mulut
```

Urutan pembuatan = urutan tumpuk: kaki belakang (R) → lengan belakang (R) → torso →
kepala + wajah → lengan depan (L). Skala 0,75 (jauh), 0,85–0,9 (panggung normal), 1,15–1,4
(close-up). Varian kulit/tunik/rambut di `VAR`; jangan menambah varian dengan nama
merek/tokoh nyata.

Angka ekspresi/aksi yang dipakai (semua deterministik dari `time`):

| Gerak | Expression / keyframe |
|---|---|
| Napas | torso Scale `[value[0], value[1]*(1+Math.sin(time*2.4)*0.015)]` (fase beda per tokoh) |
| Kedip | mata Scale `var c=(time+0.4)%3.3; c<0.12?[value[0],value[1]*0.1]:value` |
| Jalan (digate) | paha `value ± sin((time−t0)*11)*24`, betis `max(0, ±sin(…−1))*20`, lengan berlawanan `*18`, ROOT y `−abs(sin)*6` — hanya dalam `t0<time<t1` |
| Lompat | ROOT Position 3× (0,25 dtk turun-naik 55 px), paha `−abs(sin(π·2t))*25`, betis `+35` |
| Lempar melengkung | lengan Rotation 0 → −20 (ancang) → 110 (lepas, influence 30) → 0; benda: 3 keyframe Position (tangan → puncak → tangan penerima) + Rotation 540–720 |
| Melambai | lengan Rotation −150 ↔ −120 tiap 0,3 dtk |
| Memeluk/cemas | lengan-R −35, lenganbawah-R −60, lengan-L −70, lenganbawah-L −40; alis ±15; mulut Scale `[70,60]` |
| Kaget/senang | mulut Scale `[130,260]` dalam 0,03 dtk; mata Position bergeser ±10 di ruang kepala |
| Tidur | ROOT Rotation −90 (cut, hold ganda), mata Scale `[110,12]`, napas 1,6 Hz amplitudo 0,03 |
| Api | lidah api Scale `1+sin(time*13..21)*0.07..0.18`, Rotation `sin(time*8..10)*4..5`; cahaya api PNG opacity 30, Scale bernapas 3 % |
| Lalat/bintang/semak | Position `sin/cos` amplitudo 30–80 px; bintang Opacity `value*(0.85+sin(time*2.3)*0.15)`; semak Rotation `sin(time*1.7)*2` |

## Yang dikompromikan pada build ini (katakan ke user di awal)

- Urutan layer mengikuti urutan pembuatan; benda yang harus melintas DI DEPAN tokoh
  harus dibuat setelah tokoh, atau dibuat ulang.
- Aset ilustrasi berupa PNG raster; mengubah warna/bentuk = edit skrip SVG, render
  ulang, ganti footage. Karakter tetap vektor dan bisa diedit penuh di AE.
- Tanpa motion blur, tanpa efek selain Gradient Ramp; blur/glow ditambahkan user di AE.
- Setiap karakter = ±15 KB teks perintah yang harus ditulis penuh (bridge tidak membaca
  file op); 20 karakter ≈ 300 KB. Ini penyumbang waktu terbesar, bukan latensi bridge
  (rata-rata `ae_batch` 6,5 dtk, contact sheet 12 dtk, relay 7 dtk).

## Checklist bridge

- [ ] CAM: anchor `[0,0]`, position `[0,0]` sebelum ada anak; kamera hanya di CAM,
      layer precomp master diam (kecuali aksen geser 96 px)
- [ ] Semua layer dunia ber-parent ke CAM; setelah parent, posisi/skala aset dicek
      lewat `ae_get_layer_info` (tanah harus `[0,0]`, scale `[50,50]`)
- [ ] Urutan pembuatan: langit → latar jauh → tanah → properti → tokoh → benda yang
      dilempar → overlay cahaya/malam
- [ ] Keyframe bagian tubuh dalam ruang induk; hold ganda (Δ1 frame) untuk cut di dalam
      panggung yang dipakai ulang
- [ ] Contact sheet tiap panggung dilihat mata (via relay bila r2 diblokir), lalu
      contact sheet master satu waktu per panggung
- [ ] `apply_gradient` / `get_layer_info` / `export_*` tidak pernah di dalam `ae_batch`
- [ ] Pesan penutup: Ctrl+S, hapus comp uji, perintah `aerender`, daftar kompromi
