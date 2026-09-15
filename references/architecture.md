# Arsitektur — struktur proyek dan alasannya

Tiap keputusan di sini pernah salah dulu sebelum benar. Bagian "kenapa"
lebih penting daripada kodenya.

## Struktur berkas

```
proyek/
├── index.html          markup semua adegan + filter SVG motion blur
├── css/app.css         token warna, layout adegan, state awal tersembunyi
├── js/three-scene.js   dunia WebGL ber-state (latar, partikel, ornamen, bloom)
├── js/timeline.js      SATU-SATUNYA tempat waktu ditulis (GSAP master timeline)
├── js/util.js          splitChars + blurTween (motion blur berarah)
├── js/main.js          perekat: fit stage, loop render, panel kontrol
└── tools/
    ├── serve.py        dev server Cache-Control: no-store
    └── export-frames.mjs  render frame-by-frame (puppeteer)
```

Boleh dipadatkan jadi satu berkas (lihat `assets/starter-opener.html`) untuk
prototipe; pecah ke struktur di atas begitu adegan > 3.

## Panggung: 1920×1080 dipatok, lalu di-scale

```css
#stage{position:fixed;left:50%;top:50%;width:1920px;height:1080px;
  transform:translate(-50%,-50%) scale(var(--fit));overflow:hidden}
```
```js
const s = Math.min(innerWidth/1920, innerHeight/1080);
```

**Kenapa:** komposisi tidak boleh berubah karena ukuran jendela. Posisi yang
disetujui di monitor 27" harus identik saat direkam. Ukuran jendela hanya
mengubah zoom, bukan layout.

## Rig kamera `#world`

```
#stage
└── #world            ← rig kamera: DI-SCALE/TRANSLATE oleh timeline
    ├── <canvas>      ← WebGL (latar 3D)
    ├── .bgfx         ← gradient overlay (blend screen)
    └── #dom          ← semua adegan teks/UI
├── .leak             ← light leak: DI LUAR world, lapisan paling atas
├── .vignette, .grain
```

**Kenapa world membungkus canvas juga:** saat kamera zoom, yang ikut membesar
harus teks DAN latarnya.
Men-zoom layer teks saja terasa palsu; men-zoom seluruh dunia terasa kamera.
Light leak justru HARUS di luar world: ia cahaya di depan lensa, bukan
bagian dunia.

## State-driven WebGL

Scene Three.js tidak tahu apa-apa soal waktu. Ia mengekspos satu objek:

```js
const state = {
  grid: 0, dust: .5, nebula: .6, stars: 0, tunnel: 0, flow: 0,
  camX: 0, camY: 0, camZ: 16, camRoll: 0, bloom: .85, shake: 0,
  heroO: 0, heroS: 1, heroX: 0, heroY: 0, heroZ: 6,   // ornamen utama
};
```

dan timeline GSAP men-tween angka-angka itu. Fungsi `render(t)` menerima
`t = tl.time()`.

**Kenapa:** satu sumber kebenaran waktu. Scrub, pause, dan export otomatis
benar karena WebGL tidak punya jam sendiri.

**Aturan `flow`:** benda yang "mengalir" (tunnel, hujan partikel) disimpan
sebagai JARAK yang di-tween (`flow: '+=300'`), posisi tiap partikel =
`(seed + flow*speed) % span`. JANGAN `pos += speed*dt` — itu akumulasi yang
membuat scrub dan export tidak reproducible.

## Timeline: detik absolut

```js
tl.fromTo(chars, {...}, {...}, 8.10);   // ← angka absolut, bukan "+=0.3"
```

**Kenapa:** rundown adegan berisi angka detik; menulis angka yang sama di
kode membuat urutan terbaca sekali lihat, dan menggeser satu adegan tidak
merembet ke adegan lain. Sediakan konstanta `DURATION` di satu tempat.

## State awal di CSS, bukan di GSAP

```css
.hero, .line, .obj, .ornament { opacity: 0 }
```
```js
tl.fromTo(el, {opacity:0,y:60}, {opacity:1,y:0, immediateRender:false}, 8.1);
```

**Kenapa:** dengan `immediateRender:false`, CSS-lah yang memegang keadaan
sebelum tween mulai — tanpanya semua elemen berkedip di frame pertama.

**JEBAKAN yang pernah terjadi:** selector state awal kalah spesifisitas.
`.card.ghost{opacity:.85}` mengalahkan `.card{opacity:0}` sehingga elemen
muncul mendahului animasinya. Jangan pernah menulis `opacity` di selector
yang lebih spesifik dari selector state-awal; biarkan GSAP yang memberi
nilai akhirnya.

## Determinisme — daftar larangan

| Larangan | Gantinya |
|---|---|
| `Math.random()` di render loop | sinus frekuensi tinggi: `Math.sin(t*137.2)` |
| `Date.now()` / `performance.now()` | `tl.time()` diteruskan sebagai parameter |
| `setInterval` untuk teks berjalan/mengetik | tween `{i:0→n}` + `onUpdate` slice |
| akumulasi `pos += v*dt` | posisi = fungsi(seed, state.flow) |
| `Math.random()` saat SETUP boleh | seed dibuat sekali saat load, bukan per frame |

## Dev server wajib no-cache

`python -m http.server` membiarkan browser menahan module JS lama lewat
heuristic caching — edit "tidak ngefek", dan kamu akan mengejar hantu.
Selalu pakai server yang mengirim `Cache-Control: no-store`
(`scripts/serve.py`). ES module tidak jalan lewat `file://`, jadi server
memang wajib.

## Verifikasi vs export — dua hal berbeda

- **Verifikasi** (setiap batch perubahan): `scripts/snap.mjs` memotret
  6–20 detik kunci lewat `OPENER.seek(t)`; hasilnya dilihat, bukan
  disimpan. Tanpa Node: `?debug=1` + screenshot manual.
- **Export** (hanya bila user minta MP4): render semua frame. Jangan
  tertukar — merender penuh untuk "ngetes" membuang ribuan gambar dan tidak
  memberi penilaian apa pun.

## Export ke video

Jangan merekam layar untuk hasil final (frame drop). Karena semuanya
deterministik: set `tl.time(frame/fps)` → tunggu 2× rAF (satu untuk GSAP
menulis style, satu untuk render loop menggambar) → screenshot → ulangi.
`scripts/export-frames.mjs` melakukannya via puppeteer; gabungkan dengan:

```
ffmpeg -framerate 60 -i frames/f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 out.mp4
```

Ekspos `window.OPENER = { tl, DURATION }` supaya skrip export (dan debugging
konsol) bisa mengendalikan timeline.

## Panel kontrol developer — tersembunyi

Jangan tampilkan player di deliverable. Default: autoplay saat dibuka, loop
saat selesai, R ulang, Space jeda. Panel (play/pause, slider scrub, jam
`t.toFixed(2)`) hanya muncul dengan `?debug=1`; `?clean=1` = tanpa panel dan
tanpa autoplay untuk skrip export. Scrub tetap alat review utama user —
mereka berpikir dalam "detik ke-X" — tapi lewat URL debug, bukan di hasil.

## Verifikasi visual (bukan opsional)

Setelah tiap batch perubahan: buka di browser, `tl.pause(); tl.time(X)` di
konsol untuk tiap detik kunci, screenshot, nilai dengan heuristik di
`anti-ppt.md`. Kode yang jalan ≠ adegan yang benar; hampir semua revisi
user datang dari MELIHAT, bukan dari error.


## Bentuk deliverable: satu berkas, tanpa server

Selama pengembangan boleh multi-file (css/, js/) + server no-cache. Tapi yang
DISERAHKAN adalah satu `index.html` yang bisa diklik dua kali:

- `<style>` dan `<script type="module">` ditulis inline. Alasannya teknis:
  Chrome menolak `<script type="module" src="js/app.js">` dari `file://`
  (origin `null` → CORS), sedangkan module inline boleh meng-`import` dari
  CDN https tanpa masalah.
- Import map + GSAP/Three dari CDN tetap dipakai (butuh internet, tidak butuh
  server). Font Google juga.
- Aset lokal (ikon, gambar) cukup path relatif — `<img src="icon.png">`
  aman di `file://`.
- Hindari `fetch()`/XHR ke berkas lokal — itu diblokir di `file://`.
- Node/puppeteer hanya untuk render MP4; jangan sampai user mengira opener
  butuh `node_modules`. Jelaskan itu di README. Tanpa Node: rekam layar
  (dengan catatan bisa drop frame). Tanpa Python: tidak ada yang hilang —
  server hanya perlu bila memakai module lokal, dan deliverable satu-berkas
  tidak memakainya.
- Skrip render/snap memakai default `pathToFileURL(process.cwd())` supaya
  bekerja tanpa server; URL http tetap bisa dioper lewat env `URL`.

Proses inline yang aman: baca css & js, ganti tag `<link>`/`<script src>`
dengan isinya, pastikan JS tidak mengandung `</script>`, lalu hapus folder
sumbernya supaya tidak ada dua kebenaran.
