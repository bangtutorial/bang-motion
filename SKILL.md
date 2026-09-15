---
name: bang-motion
description: Membangun motion graphic sinematik di browser (promo video, opener, intro, bumper, kinetic typography, explainer/video penjelasan bergambar 16:9 atau 9:16) memakai HTML + CSS + GSAP (+ Three.js bila perlu), dengan hasil yang bergerak seperti video sungguhan — bukan slide presentasi. Gunakan skill ini setiap kali user meminta "video promo", "opener", "intro animasi", "motion graphic", "bumper", "kinetic typography", "animasi teks sinematik", "explainer", "video penjelasan" (jurnalisme visual, kartun edukasi, kolase), atau menunjukkan referensi video promosi/explainer dan ingin dibuatkan versi web-nya — bahkan bila mereka tidak menyebut kata "motion graphic" secara eksplisit. Juga gunakan bila user mengeluh hasil animasi web "seperti PPT/presentasi" dan ingin lebih sinematik, atau ingin merender animasi web menjadi file video MP4, atau ingin explainer kartun/animasi dibangun LANGSUNG di After Effects lewat bridge/MCP Higgsfield.
license: MIT
metadata:
  author: Bang Tutorial
  author_url: https://youtube.com/bangtutorial
  version: "1.18.0"
  updated: "2026-09-14"
  homepage: https://github.com/bangtutorial/bang-motion
---

# Bang Motion — motion graphic web yang bukan PPT

**v1.18.0 · by [Bang Tutorial](https://youtube.com/bangtutorial) · MIT.** Riwayat perubahan di `CHANGELOG.md`;
cara pasang di `README.md`.

Skill ini untuk AI coding agent apa pun (format Agent Skills terbuka).
Isinya hukum dan resep untuk motion graphic yang bergerak seperti video, bukan
presentasi — patuhi sebelum menulis kode.

## Prasyarat — hanya browser

Deliverable (`index.html`) hanya butuh browser modern + internet untuk CDN
(GSAP, font). Python dan Node **opsional**, dipakai hanya untuk alat kerja:
`scripts/serve.py` (server no-cache, cuma perlu bila memakai module lokal),
puppeteer (snapshot/verifikasi otomatis, `scripts/export-frames.mjs` → MP4).
Kalau user tidak punya keduanya: (1) tetap bangun satu-berkas, buka lewat
klik dua kali; (2) verifikasi visual lewat `?debug=1` (panel scrub) dan
screenshot manual per detik kunci; (3) MP4 lewat rekam layar (OBS / rekam
tab browser) — jelaskan bahwa hasil rekam layar bisa drop frame, dan render
frame-by-frame butuh Node. Jangan pernah membuat deliverable yang butuh
`npm install` untuk DITONTON.

**ffmpeg juga opsional.** Cek dulu (`ffmpeg -version`); bila tidak ada:

| Kebutuhan | Dengan ffmpeg | Tanpa ffmpeg |
|---|---|---|
| Sinkron VO (batas kalimat/paragraf) | `silencedetect` | `scripts/vo-pauses.html` — buka di browser, pilih audio, salin `SEG`/`PARA`; hasilnya sama persis (Web Audio, tanpa instal) |
| Durasi/format audio | `ffprobe` | angka `DUR` dari vo-pauses.html; browser memutar wav/mp3/m4a/ogg langsung |
| Export MP4 | gabung PNG dari export-frames.mjs | tidak ada MP4 — tawarkan instal satu perintah (`winget install Gyan.FFmpeg` / `brew install ffmpeg`) atau rekam layar |
| Mempelajari video referensi (ekstrak frame) | `fps=` + `tile=` | minta user mengirim screenshot di detik kunci, atau buka videonya di browser dan potret pada detik tertentu |

Tanpa ffmpeg alur explainer tetap lengkap sampai sinkron VO; hanya MP4 yang
butuh instalasi.

## Player — tidak ada, autoplay, loop

Default deliverable: **tanpa panel/player apa pun di layar**, langsung
memutar saat dibuka, dan mengulang dari awal saat selesai (`onComplete →
play(0)`; bila ada suara, audio ikut diulang). Kontrol tersembunyi: R ulang,
Space jeda. Panel scrub/jam hanya muncul dengan `?debug=1` (alat review),
dan `?clean=1` menahan autoplay untuk export. Ada suara? Coba `play()`
langsung; bila diblokir browser, tahan di frame 0 dan mulai pada klik
pertama — tanpa teks "ketuk untuk mulai". Ini sudah tertanam di kedua
starter.

## Larangan struktural — uji PPT yang bisa diperiksa mekanis

Model lain (dan kamu, bila lelah) akan jatuh ke pola ini walau sudah membaca
hukum di bawah. Sebelum menyerahkan, cek KODE, bukan perasaan:

1. `grep -c "class=\"scene\"\|<section" index.html` — bila ≥ 3 adegan
   berupa `<section>` yang dinyalakan-dimatikan dengan `autoAlpha`/opacity
   → itu slide deck. Adegan harus berganti karena DUNIA/KAMERA bergerak
   (kamera bergerak, whip ke sudut lain, push-through, latar berganti),
   bukan karena section di-fade. Pengecualian yang sah: **kartun panggung**
   (`references/kartun-panggung.md`) memakai cut/geser 96 px antar panggung
   — boleh, karena tiap panggung hidup penuh (≥10 benda beraksi), bukan
   gambar diam yang di-fade.
2. Ada benang merah visual yang bertahan: satu subjek (aksi kontinu) ATAU
   satu dunia kolase/kertas/putih yang disusuri kamera (kartun, foto,
   katalog, sketsa). Foto full-bleed berganti-ganti tanpa dunia bersama →
   PPT. Satu gambar + satu kalimat per adegan, berganti tiap adegan →
   tetap slideshow walau kameranya bergerak: tiap adegan 3–5 elemen yang
   masuk bertahap per frasa (explainer.md "Satu adegan = 3–5 elemen").
3. Per adegan hitung node teks: eyebrow/kicker + judul + body/kredit = 3
   tingkat → PPT. Maksimum dua: satu angka/kalimat besar + satu label dunia.
   Dokumen/stempel/blok tanggal berisi ≤ 3 baris pendek dihitung objek,
   bukan tingkat teks.
4. Ken Burns (scale 1.0→1.05 pada foto) sebagai satu-satunya gerak → PPT.
   Gerak tiap detik harus datang dari BAHASA GERAK LATAR yang dipilih di
   style brief dari menu `techniques.md` §7c (kamera bernapas di latar
   bertekstur, gradien berpindah, blob mengambang, grain hidup, sapuan
   cahaya per segmen, bentuk besar berputar lambat, partikel naik, grid
   bernapas, teks hantu bergeser, Ken Burns + parallax…). Batang/garis/
   potongan yang melintas ke samping ("lane", "range", "streak", hujan
   partikel horizontal) SUDAH dipakai dua proyek berturut-turut dengan nama
   berbeda — itu bukan default; hanya bila tema memang kecepatan/aliran,
   dan tidak boleh dua proyek berturut-turut.
5. Transisi hanya fade + scale bump + light leak di semua cut → template PPT.
   Whip ke sudut lain, cut ke instrumen (peta/speedometer/profil), push-through.
6. Explainer dimulai dari starter GAYANYA: `starter-explainer-kartun`,
   `-jurnalisme`, `-katalog`, `-sketsa` (mode kolase: kamera menyusuri aset
   diam), `starter-explainer` (aksi kontinu: dunia mengalir), atau
   `starter-explainer-panggung` (kartun panggung: satu panggung per adegan,
   rig sendi, kamera hanya di dalam panggung). Yang kolase satu rig; yang
   panggung rignya lain. BUKAN dari `assets/starter-opener.html`
   (opener teks), dan bukan dari nol.

7. **Miniatur adalah slide.** Kamera zoom < 1,08 sehingga rumah sebesar ibu
   jari dan tanah kosong mengisi separuh layar → PPT walau semua bergerak.
   Dunia dipecah jadi panggung seukuran frame, bukan satu peta besar yang
   dijelajahi (`kartun-panggung.md` Hukum 1).

8. **Kerangka template (opener/promo).** Cek rundown dan kode: adegan pertama
   berupa teks yang diperbesar lalu keluar ke kiri; tiga tile/kartu fitur
   sejajar; kotak input/searchbar yang diketik; urutan hook → fitur → fitur →
   janji → logo → CTA. Dua atau lebih tanpa tuntutan konsep → template, walau
   kulitnya baru. Pilih ulang kerangka dari `references/opener-konsep.md`.

Gagal satu poin saja → rombak sebelum ditunjukkan ke user.

## Jenis pekerjaan yang dicakup

Skill ini untuk motion graphic web secara UMUM. Explainer hanya salah satu
jenis — ia punya dokumen sendiri karena strukturnya beda, bukan karena ia
yang utama.

Starter dinamai menurut kategorinya: `starter-opener.html` untuk opener, promo,
bumper, intro, dan kinetic typography; `starter-explainer-*.html` untuk explainer,
dengan akhiran mode/gaya (`-kartun`, `-jurnalisme`, `-katalog`, `-sketsa` = kolase;
tanpa akhiran = aksi kontinu; `-panggung` = kartun panggung). Kartun panggung adalah
mode explainer (gaya 6), bukan kategori sendiri: tujuannya tetap menjelaskan dengan
VO, yang berbeda hanya cara produksinya.

| Jenis | Durasi lazim | Ciri | Resep |
|---|---|---|---|
| Opener / promo produk | 25–40 dtk | satu konsep dari menu (kerangka lahir dari produk, bukan urutan baku), satu momen istimewa, penutup brand | `references/opener-konsep.md` + alur kerja di bawah + `references/techniques.md` |
| Bumper / ident / logo sting | 3–8 dtk | logo build-on, satu gerak tanda tangan, selesai sebelum penonton sadar | `techniques.md` (logo build-on, light leak) |
| Intro / outro kanal | 5–12 dtk | nama kanal + tanda tangan gerak yang sama tiap episode | alur kerja di bawah |
| Kinetic typography / lirik | 15–60 dtk | teks adalah subjek; split per kata/huruf; ritme mengikuti audio | `techniques.md` (split + blur berarah, pan 3D per kata) |
| Title / lower third / bumper segmen | 2–6 dtk | elemen kecil di atas footage, masuk-keluar bersih, latar transparan | `techniques.md` |
| Explainer / video penjelasan | 30–90 dtk | fakta bersumber, entitas tampil, sudut pandang berganti, lima gaya | `references/explainer.md` + starter per gaya |

## Explainer dan karakter: baca sebelum menentukan shot

Untuk explainer kartun edukasi flat berkarakter (gaya keenam, **kartun
panggung**), atau revisi yang terasa seperti slideshow/miniatur, baca
`references/kartun-panggung.md`: satu panggung per adegan, zoom 1,08–1,95,
kontinu di dalam panggung dan cut/geser 96 px di antaranya, rig sendi dengan
transform manual, nol caption, palet flat cerah. Bedakan kalimat, beat visual,
framing, dan pergantian panggung. Untuk membangunnya langsung di After Effects, baca
`references/ae-bridge-higgsfield.md`. Pedoman khusus explainer ini memperjelas
aturan opener di bawah; contoh font, jumlah scene, dan efek bukan resep universal.

## Hukum #1 — Ini video, bukan slide

Penyakit paling umum: model menyusun adegan seperti slide — judul + sub-judul
+ body copy + deretan badge. Itu langsung terbaca "PPT" dan akan ditolak.

Aturan kerasnya:

- **Untuk opener: satu kalimat pendek + maksimal satu objek utama per adegan.** Tidak ada
  kicker ("01 — FITUR"), sub-judul, paragraf keterangan, chip/badge fitur,
  atau metadata teknis (nama package, URL panjang). Chip, tombol, dan label yang
  merupakan bagian UI produk yang sedang dipakai tidak termasuk.
- **Informasi baru = respons visual baru.** Pada explainer, ubah keadaan/aksi
  di dunia yang sama bila masih berhubungan; pergantian kalimat tidak wajib mengganti shot.
- **Daftar poin diganti visual, bukan otomatis tiga tile.** Pilih cara dari
  menu fitur di `references/opener-konsep.md` (satu fitur didemokan, kata
  berganti, objek bertransformasi, kartu dikocok, grid tile…); dua opener
  berturut-turut tidak memakai cara yang sama.
- **Adegan harus hidup.** Kamera boleh menetap saat objek membawa aksi.
  Gerakkan kamera untuk mengikuti atau mengungkap sesuatu; jangan mengandalkan
  teks fade/slide di atas latar diam, atau pan/zoom berulang di semua segmen.

Baca `references/anti-ppt.md` SEBELUM mendesain adegan — berisi daftar
pelanggaran nyata beserta perbaikannya.

## Hukum #2 — Deterministik atau mati

Tidak ada satu baris pun yang membaca jam sistem. Semua visual adalah fungsi
murni dari `tl.time()` (waktu timeline GSAP): spektrum, angka berjalan,
partikel, getar kamera (sinus frekuensi tinggi, bukan `Math.random()`),
posisi objek yang "mengalir" (tween JARAK, bukan akumulasi kecepatan per
frame). Konsekuensinya: scrub akurat seperti timeline After Effects, dan
render frame-by-frame ke MP4 menghasilkan gambar identik setiap kali.

## Hukum #3 — Gaya lahir dari tema, bukan dari starter, bukan dari referensi

Kegagalan yang umum: opener untuk produk lain keluar dengan kulit PERSIS
opener produk sebelumnya — gelap, aksen biru, glow, nebula, font yang sama —
karena model mengambil gayanya dari starter. Animasinya bisa bagus, tetap
gagal: opener adalah wajah produk, dan dua produk tidak boleh berwajah sama.

1. **Style brief dulu, kode belakangan.** Sebelum menyentuh starter, tulis
   enam baris ini dan tunjukkan ke user bersama rundown adegan:
   - tema/produk + tiga kata sifat perasaan yang ingin ditinggalkan;
   - **konsep & sidik jari struktur** (opener/promo): tiga kandidat konsep dari
     `references/opener-konsep.md`, satu dipilih dengan alasan dari produk, lalu
     `konsep · jumlah adegan · objek utama tiap adegan · pembuka · penutup`;
   - palet: satu warna utama DARI brand/tema (logo, ikon aplikasi, situs,
     kemasan), satu warna latar, satu aksen — sebutkan hex DAN sumber tiap
     warna; warna yang bukan dari brand ditulis "turunan: alasan";
   - font display yang punya karakter sesuai perasaan itu (bukan
     Poppins/Inter/Roboto/Montserrat/Arial) + font pendamping; pengecualian:
     konsep klaim → cara → hasil memakai font UI produk sendiri
     (`references/opener-konsep.md`);
   - penekanan teks: tanpa sorotan kata, atau satu bentuk sorotan (sebutkan) —
     sorotan kata OPSIONAL, bukan bawaan setiap opener;
   - bahasa latar per segmen: satu arah dari tabel "Arah gaya" untuk semua,
     atau rencana pergantian (segmen mana ganti, ke apa, kenapa, dipicu apa);
   - tanda tangan gerak: satu jenis gerak yang diulang sebagai identitas
     (wipe objek, roll 3D per kata, kertas terbang, garis yang menggambar,
     blok warna menabrak tepi…);
   - gerak latar: satu bahasa dari menu `techniques.md` §7c — bukan hal yang
     sama dengan tanda tangan gerak, dan bukan otomatis "benda melintas";
   - permukaan latar: dari menu §7d (gradien/cahaya/tekstur/grainy gradient,
     ≥ 2 lapis) — bukan flat;
   - gaya render objek: satu keluarga dari menu `techniques.md` §7e (flat, clay,
     glossy, kaca, isometrik, realistis, garis neon…);
   - aset foto (bila konsep memakai foto orang/tempat/produk): sumbernya — foto
     user, generate lewat MCP Higgsfield, atau stok berlisensi — DITANYAKAN ke
     user, plus daftar shot per babak (`references/opener-konsep.md` "Foto dalam
     opener");
   - transisi: tentukan batas mana yang memerlukan efek dan mana yang cukup cut;
     pilih dari menu §4c sesuai konteks, bukan wajib dua jenis atau wajib 3D;
   - satu momen istimewa (di mana efek termahal dipakai, sekali).
2. **Starter adalah arsitektur, bukan gaya.** Warna abu-abu, font sistem,
   dan latar WebGL di `assets/starter-opener.html` adalah PLACEHOLDER. Kalau salah
   satunya masih terlihat di hasil, gaya belum diturunkan. Latar WebGL
   (nebula, debu, grid, bloom) hanya satu bahasa latar dari delapan;
   matikan bila arah gayanya lain.
3. **Referensi = ritme, bukan kulit.** Dari video referensi ambil: durasi per
   shot, jenis transisi, hierarki atensi, energi, bahasa gerak. JANGAN ambil:
   palet, font, tekstur, tata letak, bentuk ornamen, kalimat, urutan adegan,
   dan momen unik (pembuka/penutup khas, gimmick satu kali). "Buatkan
   seperti ini" berarti "seenergik ini", bukan "berwarna seperti ini";
   "pakai style X" berarti kulit dan bahasa gerak X, bukan adegan X. Contoh
   urutan di `references/opener-konsep.md` diperlakukan sama: prinsip, bukan
   naskah (Hukum kerangka #7).
   Menjiplak kulit referensi = pelanggaran, walau user yang menyodorkannya —
   sebutkan itu satu kalimat lalu tawarkan versi yang lahir dari tema.
4. **Berbeda dari proyek sebelumnya — kulit DAN kerangka.** Dua produk berbeda harus berbeda di
   minimal tiga dari empat: palet, font, bahasa latar, tanda tangan gerak —
   termasuk bentuk sorotan kata bila dipakai (pill + bintang milik satu
   proyek tidak boleh muncul lagi di proyek lain). Kerangkanya juga: konsep
   berbeda, atau ≥ 3 dari 5 elemen sidik jari struktur berbeda
   (`references/opener-konsep.md`). Warna baru di atas urutan adegan lama
   tetap template.
   Jangan membuka folder proyek lama untuk "contoh" — yang boleh diwarisi
   hanya aturan di skill ini.
5. **Latar tidak default gelap.** Tanpa aturan ini semua opener cenderung
   keluar gelap dengan nebula karena starter dan contoh-contohnya gelap. Latar mengikuti
   tema: gradien terang, warna lembut, blok warna, kertas, foto, atau gelap
   — tabel "Arah gaya" punya sepuluh pilihan dan sebagian besar tidak gelap.
   Contoh-contoh di skill ini (kertas terang, nebula) hanya contoh, bukan
   templat yang dikunci.
   **Latar tidak pernah statis.** Selalu ada gerak latar (§7c), dan warna
   latar BOLEH berganti kapan pun dibutuhkan: mood/topik segmen berubah
   (masuk ke produk, masalah → solusi, klaim → CTA), brand warna-warni
   menuntut ritme warna, atau aksi di layar memang mengubahnya (toggle
   dinyalakan, benda menutup lensa, ikon membesar memenuhi frame). Yang
   dijaga hanya dua: pergantian punya pemicu yang terlihat (wipe, benda, aksi
   UI, push ke bidang warna, cut di ketukan) — bukan cross-fade tanpa sebab
   yang terasa "ganti slide" — dan latar tidak dibiarkan satu warna diam
   hanya karena tidak pernah dipertimbangkan. Rencananya ditulis di style brief.
6. **Bebas berekspresi.** Hukum-hukum di sini mengunci STRUKTUR (bukan
   slide), KONTRAS (teks terbaca), dan KEBARUAN (tidak mengulang proyek
   lain) — bukan ekspresi. Gradien kaya, cahaya, 3D, kedalaman, tekstur,
   warna berani dianjurkan bila cocok dengan tema. Yang dilarang hanya
   mengambil default termurah dan mengulanginya: balok datar menyapu, garis
   melintas, latar flat, kulit proyek lain. Kalau dua pilihan sama-sama
   memenuhi hukum, pilih yang lebih berani.
7. **Yang boleh sama di semua pekerjaan:** hukum anti-PPT, rig kamera,
   determinisme, ritme masuk-keluar asimetris, ukuran teks minimum.

### Arah gaya (pilih satu; boleh memadukan dua dengan sadar)

| Arah | Latar | Tipografi | Gerak khas | Cocok untuk |
|---|---|---|---|---|
| Sinematik gelap | gradasi nyaris hitam, partikel/nebula WebGL, bloom hanya di objek | grotesk tebal bersih | push-through, cahaya di depan lensa | alat kreatif, gaming, teknologi |
| Poster color-block | bidang warna solid besar berganti tiap adegan, tanpa gradasi | display sangat tebal, huruf raksasa terpotong tepi | wipe blok, teks menabrak tepi frame | app konsumen, musik, event |
| Editorial terang | putih/krem, ruang kosong luas, garis tipis | serif display + grotesk kecil | geser halus, garis menggambar, kamera tenang | produktivitas, finansial, SaaS |
| Kertas & cetak | tekstur kertas, potongan kolase, stempel, selotip | tulisan tangan + serif | benda terbang lalu mendarat, sudut miring | edukasi, komunitas, kuliner |
| Retro / analog | warna pudar, grain, garis scan, bingkai VHS | geometris 70–90-an | glitch terkendali, zoom kasar, freeze | nostalgia, musik, hiburan |
| Brutalis mono | hitam-putih, grid keras, kotak bergaris | monospace + kondensasi | cut keras, blok bergeser, kursor berkedip | developer tools, teknis |
| Pastel ceria | pastel bertumpuk, bentuk bulat besar | rounded sans tebal | mantul elastis, bentuk mekar | anak, kesehatan, lifestyle |
| Mewah gelap | hitam + emas/perunggu, bayangan lembut, kilau | serif tinggi berspasi lebar | gerak lambat, sinar menyapu, kedalaman | fashion, otomotif, properti |
| Flat pop berfoto | netral terang bergantian dengan medan warna brand user yang solid; bentuk flat dan stiker turunan geometri logo user + ilustrasi 3D lembut | sans geometris membulat tebal + kata raksasa terpotong tepi | foto orang potongan pop dari bawah, stiker meletup elastis, medan warna menyapu/snap di ketukan | app konsumen, fintech, e-commerce, brand anak muda |
| Grainy gradient | dasar gelap/warna dalam; bentuk bergradien jenuh 2–3 warna yang bercahaya dari dalam; butiran halus di seluruh frame | grotesk bersih kecil, atau display tebal minimal | lapisan bentuk membuka/berputar pelan, kamera menembus lubang bentuk, bola cahaya pemandu | tech, AI, musik, fintech, peluncuran kreatif |

Dua opener berturut-turut memakai baris tabel yang sama = tanda bahaya;
pilih baris lain atau padukan dua baris dengan cara yang belum dipakai.

## Hukum #4 — Teks hidup, latar tunduk

Dua opener dengan rig yang sama bisa berakhir sangat baik atau sangat buruk
hanya karena tipografi dan kontrasnya. Yang buruk: setiap judul KAPITAL
SEMUA bobot 800 di tengah, masuk dengan cara yang sama, di atas ladang cahaya
putih yang lebih terang daripada hurufnya. Yang baik: sentence case bobot
500, penekanan pada kata kunci (mis. pill + bintang — itu tanda tangan
satu proyek, bukan aturan; sorotan kata sendiri opsional), tanda baca
hanya bila perlu, ukuran/arah/
posisi bergantian, latar tenang di bawah teks, latar berganti mengikuti
segmen. Resep lengkap dengan kode: `techniques.md`
bagian 1 dan 1b. Ringkasnya:

- Sentence case bobot 500–600. Kapital-tebal hanya untuk satu adegan penekanan.
- Judul, klaim, dan frase pendek DEFAULT TANPA TITIK — terutama frase ≤ 4 kata
  dan kalimat satu baris. Tanda baca hanya bila mengubah arti atau irama: `?`
  untuk pertanyaan sungguhan, titik untuk gaya dua kalimat pendek berturut-turut
  yang disengaja, `!` sangat jarang. Gaya tanda baca diputuskan sekali di style
  brief dan konsisten; bila dipakai, ia elemen terpisah yang muncul terakhir.
- Sorotan kata (pill, garis bawah, marker, kotak, warna, coret) OPSIONAL dan
  diputuskan di style brief. Tanpa sorotan pun kalimat tetap punya penekanan:
  kata per kata dari redup ke penuh, ukuran/bobot, jeda, atau objek (ikon,
  UI) yang berdiri di samping kata. Bila dipakai: satu bentuk per video,
  tidak wajib di setiap kalimat, berbeda dari proyek lain; ornamen hanya bila
  diturunkan dari bentuk brand.
- Dua adegan berturut-turut tidak boleh sama dalam ukuran, arah masuk, dan
  posisi teks.
- Di KANTONG TEKS (bukan seluruh frame), latar harus GELAP (≤ 25 %
  luminance) atau TERANG (≥ 80 %), tidak pernah "ramai sedang". Di luar
  kantong, latar justru harus kaya: gradien, cahaya, tekstur (§7d) — flat
  satu warna ditolak. Elemen latar apa pun (partikel, bentuk,
  tekstur, garis): warna dari sisi gelap palet, opacity ≤ .35 di kantong
  teks, ≤ 40 elemen terang terlihat.
- Pertimbangkan selang-seling gelap–terang bila segmennya memang berganti
  mood; bukan kewajiban mekanis.

## Alur kerja

0. **Kenali jenisnya** (tabel "Jenis pekerjaan"). Explainer → buka
   `references/explainer.md` dan ikuti "Langkah nol" di sana: SATU
   pertanyaan berisi gaya (lima pilihan + rekomendasi), rasio, durasi,
   suara, plus pagar durasi. Jenis lain → lanjut; tanya hanya hal yang
   benar-benar tidak bisa diturunkan dari brief (rasio, durasi, ada
   musik/VO atau tidak), dalam satu pertanyaan.
0b. **Tulis style brief** (Hukum #3) dan tunjukkan bersama rundown. Tanpa
   style brief yang disetujui, jangan menyentuh kode.
1. **Serap referensi & sumber brand.** Minta screenshot/potongan video
   referensi bila ada; petakan per shot (durasi, gerakan, jenis transisi,
   urutan atensi) — hanya RITMENYA, bukan kulitnya (Hukum #3). Warna, logo
   (path vektor ASLI, jangan digambar ulang), font, dan klaim fitur diambil
   dari sumber resmi PRODUK yang sedang dibuat — bukan dari referensi, bukan
   dari proyek lain, bukan karangan.
2. **Tulis rundown dari konsep yang dipilih** — tabel `detik | adegan |
   kalimat | visual`. Jumlah dan jenis adegan mengikuti konsep
   (`references/opener-konsep.md`), bukan pola hook → fitur → fitur → janji →
   logo → CTA. Total 25–40 detik. Minta persetujuan user atas rundown ini
   sebelum menulis kode; merombak rundown murah, merombak kode mahal.
3. **Scaffold arsitektur.** Opener/promo/bumper/typography: salin
   `assets/starter-opener.html` (stage 1920×1080, rig kamera `#world`, scene
   Three.js ber-state, helper timeline) lalu SEGERA ganti token warna, font,
   dan bahasa latarnya sesuai style brief — starter sengaja abu-abu. Explainer: salin starter sesuai gaya —
   `starter-explainer-kartun/-jurnalisme/-katalog/-sketsa.html` (mode
   kolase: kamera into/settle/look/home di atas cutout/foto, say/unsay per
   kata, draw anotasi, push-through antar adegan) atau
   `starter-explainer.html` (aksi kontinu: dunia mengalir, hero, objek
   dunia, view peta, whip). Semua sudah autoplay + loop tanpa player. Struktur multi-file dan
   penjelasan tiap keputusan ada di `references/architecture.md`.
4. **Bangun adegan satu per satu** dengan resep di
   `references/techniques.md` (split per huruf + motion blur berarah,
   pan 3D per kata, menu transisi, mockup UI). Resep adalah perkakas, bukan
   daftar belanja: pakai hanya yang dituntut konsep.
5. **Verifikasi VISUAL, bukan cuma "kode jalan".** Kamu tidak bisa menonton
   video; kamu hanya bisa melihat FRAME. Potret 6–20 detik kunci (awal
   tiap adegan, saat teks muncul, transisi) dengan `scripts/snap.mjs`
   (puppeteer, buka `file://`, tanpa server), susun jadi lembar kontak, dan
   nilai seperti sutradara: teks kepotong? tumpang tindih? teks muncul
   sebelum kamera selesai? masih terasa slide? Perbaiki, potret lagi.
   JANGAN merender semua frame untuk mengecek — itu ribuan gambar dan bukan
   verifikasi; render penuh hanya untuk export MP4 (langkah 6) bila user
   memintanya. Tanpa Node: buka `?debug=1`, scrub manual, screenshot.
6. **Serahkan sebagai SATU `index.html` yang bisa diklik dua kali.** Output
   akhir tidak boleh butuh server/Node: CSS dan JS ditulis INLINE di dalam
   berkas (module lokal `<script type="module" src="…">` diblokir CORS saat
   dibuka lewat `file://`, module inline tidak), library dari CDN, aset
   (ikon/gambar) relatif di folder yang sama. Server no-cache
   (`scripts/serve.py`) hanya alat KERJA saat mengedit, bukan syarat
   menonton. Tanpa player di layar (lihat "Player"); sebutkan `?debug=1`
   untuk scrub. **Export MP4 hanya bila user memintanya**: `scripts/
   export-frames.mjs` merender tiap frame (60 fps) ke PNG lalu ffmpeg
   menggabungkannya — cara ini bebas frame drop, tapi mahal, jadi bukan
   langkah rutin dan bukan alat pengecekan.

7. **Khusus explainer: naskah VO + ajakan merekam** — pesan penutup wajib
   memuat naskah VO lengkap dan meminta user merekam/generate lalu mengirim
   ulang audionya untuk disinkronkan. Detail bentuk naskah, petunjuk rekam,
   dan retime di `references/explainer.md` → "Penyerahan".

## Checklist sebelum menyerahkan

- [ ] Style brief (tema, palet dari brand, font display berkarakter, satu
      bahasa latar, tanda tangan gerak, momen istimewa) ditulis dan disetujui
      SEBELUM kode
- [ ] Tidak ada sisa placeholder starter (abu-abu, font sistem, nebula bila
      arah gayanya lain) dan tidak ada kulit referensi yang disalin (palet,
      font, tekstur, tata letak, kalimat)
- [ ] Berbeda dari opener/promo sebelumnya: minimal tiga dari palet, font,
      bahasa latar, tanda tangan gerak
- [ ] Opener/promo: tiga kandidat konsep ditulis dan satu dipilih; sidik jari
      struktur tertulis dan berbeda dari opener sebelumnya; paling banyak dua
      komponen kanonik (teks zoom → keluar kiri, tiga tile, input diketik,
      push-through, light leak, logo + CTA di tengah), masing-masing dituntut
      konsep (`references/opener-konsep.md`); tidak menyalin contoh konsep
      (pembuka/penutup berbeda dari contohnya, ≤ 1 momen ✦ yang ditransformasi,
      palet dan bentuk dari brand user)
- [ ] App/SaaS: minimal satu babak UI hidup — dirakit, dipakai, menghasilkan —
      dari komponen produk user, bukan screenshot diam yang di-zoom
      (`references/opener-konsep.md` bagian animasi UI); bila demo terasa
      statis, klik penting diikuti kamera (dekat → klik → mundur/geser),
      tidak di setiap klik (`techniques.md` §8)
- [ ] Teks hidup (Hukum #4): sentence case bobot 500–600, penekanan jelas,
      tanpa titik otomatis (tanda baca hanya bila mengubah arti/irama),
      ukuran/arah/posisi bergantian antar adegan;
      kapital-tebal hanya di satu adegan. Sorotan kata hanya bila style brief
      memilihnya (bukan otomatis di setiap kalimat, bukan pill + bintang
      warisan proyek lain)
- [ ] Latar tunduk (Hukum #4): di bawah teks luminance ≤ 25 % atau ≥ 80 %,
      elemen latar redup dan berwarna gelap di kantong teks; uji grayscale —
      tidak ada latar seterang huruf
- [ ] Transisi dipilih pada batas yang membutuhkan; tidak otomatis semua
      batas diberi efek atau semua efek dihapus. Objek penyapu punya makna
      dalam adegan; kecepatan, amplitudo, dan jeda sudah diperiksa.
- [ ] Permukaan latar dari menu §7d: ≥ 2 lapis (dasar + cahaya/tekstur/
      blob), warna dari palet — tidak flat satu warna, bukan hitam/putih murni
- [ ] Gaya render objek satu keluarga (§7e), atau pergantiannya dijadikan momen
- [ ] Opener berfoto: sumber foto disepakati user (foto user / generate MCP /
      stok berlisensi), wajah fiktif bila di-generate, logo/teks brand ditambahkan
      di kode, foto dianimasikan (pop, parallax, wadah) — bukan Ken Burns saja
- [ ] Bila memakai grainy gradient/butiran: butiran masih terlihat di MP4 hasil encode
      dan gradien tidak banding
- [ ] Bila memakai video: klip dipasang lewat `clip()` (tanpa `autoplay`/`loop`), dibungkus
      elemen yang dianimasikan, sumbernya disepakati user, folder `assets/` disebutkan saat
      penyerahan, dan detik yang berisi klip sudah dipotret (`snap.mjs`)
- [ ] Gerak latar dipilih dari menu §7c dan BERBEDA dari proyek sebelumnya;
      tidak ada batang/garis melintas ke samping kecuali tema kecepatan/
      aliran dan belum dipakai di proyek sebelumnya
- [ ] Latar bergerak di setiap adegan (tidak ada latar diam); pergantian warna
      latar boleh kapan dibutuhkan asal punya pemicu terlihat
- [ ] Lolos 6 poin "Larangan struktural" (bukan section yang di-fade, ada
      benang merah visual, ≤ 2 tingkat teks, gerak tiap detik, transisi
      bervariasi, starter yang benar)
- [ ] Tanpa player di layar; autoplay; loop; `?debug=1` untuk scrub
- [ ] Opener: satu gagasan utama tanpa tumpukan badge; explainer: satu
      peristiwa dapat memuat beberapa beat dan objek yang saling berhubungan.
- [ ] Kamera, cut, dan gerak objek dipilih sesuai konteks; tidak ada keharusan
      menggerakkan kamera di tiap segmen. Saat kamera bergerak, seluruh dunia ikut.
- [ ] Motion blur berarah pada semua teks masuk/keluar
- [ ] Latar lahir dari tema (tidak otomatis gelap; terang bisa gradien,
      warna lembut, blok warna, kertas), punya kedalaman (bukan satu warna
      flat), TIDAK lebih ramai daripada subjek; pergantian latar diputuskan
      per segmen di style brief dan, bila ada, terjadi di balik wipe/cut
- [ ] Glow dipakai pada objek (tile, bar, ikon dekor) — judul teks BERSIH
      (putih penuh + drop shadow tipis), kecuali user minta sebaliknya
- [ ] Font display ≠ font mockup UI; mockup memakai font produk aslinya
      (konsep klaim → cara → hasil: seluruh teks memakai font UI produk)
- [ ] Nol pemakaian `Date.now()` / `Math.random()` di jalur render
- [ ] Sudah dipotret di detik kunci (snap.mjs / ?debug=1) dan dilihat dengan
      mata — bukan render penuh; MP4 hanya bila diminta
- [ ] Ada suara? Halaman menahan di frame awal bila autoplay diblokir dan mulai
      bersama suara pada gestur pertama — tidak pernah mulai tanpa suara; tanpa
      file peluncur (`.cmd`/`.bat`)
- [ ] Explainer kolase: kamera punya koreografi (close-up → meluncur → zoom
      out), bukan hanya elemen in/out — lihat explainer.md "Kamera explainer".
      Kartun panggung: tidak ada frame dengan zoom < 1,08; kamera hanya
      bergerak di dalam panggung; antar panggung cut atau geser 96/72 px
- [ ] Kartun panggung: sendi diputar lewat proxy transform manual (tidak ada
      `transformOrigin`/`rotation` GSAP pada sendi, tidak ada tween `x/y`
      pada grup ber-`translate`); tiap panggung ≥10 benda bergerak; nol
      caption; kepala raster punya varian kedip + ekspresi
- [ ] Build lewat bridge AE: CAM di-nol-kan sebelum parenting, semua layer dunia
      ber-parent ke CAM, layer dibuat belakang → depan, keyframe bagian tubuh
      dalam ruang induk, contact sheet tiap panggung + master sudah dilihat,
      pesan penutup memuat Ctrl+S + hapus comp uji + perintah aerender
      (`references/ae-bridge-higgsfield.md`)
- [ ] Explainer: pesan penutup memuat naskah VO lengkap + ajakan merekam /
      generate sendiri dan mengirim ulang audionya untuk disinkronkan;
      `vo-script.md` tersimpan di folder proyek
- [ ] Explainer: gaya, rasio, durasi, dan suara sudah ditanya dalam SATU
      pertanyaan (kecuali yang sudah disebut user) sebelum menulis kode;
      durasi mengikuti brief/VO; jumlah adegan mengikuti konteks, bukan durasi ÷ 6
- [ ] Rasio default 16:9 / mengikuti layar; 9:16 hanya bila diminta. Tanpa
      subtitle/caption kecuali diminta. Tata letak referensi (panel, subtitle)
      tidak disalin — hanya prinsipnya
- [ ] Explainer topik aksi/kecepatan: satu subjek hadir dari awal sampai
      akhir, latar terus mengalir, angka hidup di dalam dunia (subjek
      melintas di depannya) — lihat explainer.md "Gaya kelima: aksi kontinu"
- [ ] Sudut pandang berganti: tidak ada tiga adegan berturut-turut dengan
      sudut yang sama; tiap fakta dapat instrumennya (speedometer, peta,
      profil ketinggian, balapan peta, interior, tampak depan) — lihat
      explainer.md "Sudut pandang WAJIB berganti"; kamera bernapas
- [ ] Tidak ada teks di bawah 30 px pada panggung 1080 (body ≥ 44, label ≥ 34,
      kredit ≥ 30) — ditonton di HP; teks hantu & anotasi bervariasi, bukan
      selalu outline / lingkaran putus-putus
- [ ] Explainer: tiap orang/perusahaan/tempat/produk yang DISEBUT tampil
      fotonya di adegan itu (lihat explainer.md → "Entitas yang disebut")
- [ ] `index.html` terbuka langsung lewat `file://` (klik dua kali) tanpa
      server — CSS/JS inline, tidak ada `src` module lokal
- [ ] Angka yang berubah tiap frame (jam, counter) memakai
      `font-variant-numeric:tabular-nums` + `min-width` supaya wadahnya
      tidak berubah lebar

## Jebakan yang sudah memakan korban

Detail dan perbaikannya di `references/techniques.md` bagian "Jebakan":
bloom threshold rendah → layar putih; nebula additive → menumpuk lewat bloom;
selector CSS lebih spesifik mengalahkan state awal `opacity:0` → elemen
muncul mendahului animasinya; module JS di-cache browser → edit "tidak
ngefek" (pakai server `Cache-Control: no-store`); objek 3D pipih diputar
penuh di sumbu Y → jadi sebatang garis (goyangkan, jangan putar penuh);
kotak filter SVG default memotong ekor blur (lebarkan `x/y/width/height`).

## After Effects — langsung lewat bridge Higgsfield

Bila After Effects sudah terbuka, MCP bridge `ae_*` Higgsfield tersambung, dan user
meminta animasi/explainer dibangun di AE, bangun langsung lewat perintah bridge. Baca
`references/ae-bridge-higgsfield.md`: kerangka comp lewat satu Lottie kecil, null
`CAM` per panggung (anchor & position di-nol-kan SEBELUM parenting), ilustrasi
dari SVG-kode → PNG 2× (`scripts/ae/bridge/aset-svg.py` + `svg2png.cjs`), karakter
sebagai shape asli AE bersendi (`scripts/ae/bridge/rig-tokoh.py`, ±90 op per tokoh),
keyframe bagian tubuh dalam ruang induk, verifikasi lewat contact sheet (relay
bila r2.dev diblokir). Hukum kartun panggung tetap berlaku penuh. Bridge tidak
bisa menyimpan/merender dan tidak bisa menyusun ulang urutan layer — sebutkan itu
dan buat layer dari belakang ke depan. Build 10 panggung ≈ 1 jam, 0 kredit.

## Isi paket

| Berkas | Kapan dibaca |
|---|---|
| `references/kartun-panggung.md` | KARTUN PANGGUNG: satu panggung per adegan, kamera ≥1,08, cut/geser 96 px, rig sendi + transform manual, kepala raster + ekspresi lokal, nol caption, palet flat |
| `assets/starter-explainer-panggung.html` | EXPLAINER kartun panggung: sistem panggung + kamera per panggung, `J()` sendi, `character()` (kepala vektor atau raster), whoosh 96 px, contoh dua panggung |
| `scripts/kepala-ekspresi.py` | kepala hasil generate → varian senang/cemas/kaget + kedip, dibuat lokal (deteksi pupil & mulut) |
| `references/ae-bridge-higgsfield.md` | BRIDGE: membangun kartun panggung langsung di AE lewat MCP Higgsfield — batas bridge, jebakan (null 960,540; parent ke CAM berkeyframe; reorder rusak), arsitektur CAM per panggung, rig native, relay contact sheet, penyerahan |
| `scripts/ae/bridge/aset-svg.py`, `svg2png.cjs`, `rig-tokoh.py` | BRIDGE: aset ilustrasi dari kode → SVG + manifest → PNG 2× (puppeteer); generator ±90 op `ae_batch` untuk satu karakter bersendi |
| `references/anti-ppt.md` | sebelum mendesain adegan |
| `references/opener-konsep.md` | OPENER/PROMO sebelum rundown: tiga kandidat konsep, menu 19 konsep (termasuk estafet benda, pamer sistem brand, klaim → cara → hasil, ekosistem UI hidup, pop flat berfoto, menembus bentuk bergradien, dan tur produk berselang klaim, semuanya diturunkan dari layanan/aset/produk brand), panduan layout-warna-ritme, panduan animasi UI untuk app/SaaS, panduan foto dalam opener (input user / generate via MCP), menu fitur, pembuka, penutup, transisi tanpa cut yang dibawa objek, sidik jari struktur — mencegah kerangka template |
| `references/explainer.md` | bila yang diminta explainer/video penjelasan (kartun+VO, jurnalisme visual foto, katalog putih, sketsa vintage, atau aksi kontinu; default 16:9, 9:16 hanya bila diminta) |
| `references/architecture.md` | saat scaffold / butuh alasan di balik struktur |
| `references/techniques.md` | saat membangun adegan & efek (termasuk grainy gradient §7d, menu gaya render objek §7e, dan video sebagai layer footage §9b) |
| `references/roadmap.md` | saat mengembangkan skill ini lebih lanjut |
| `assets/starter-opener.html` | titik awal OPENER/promo — arsitektur + perkakas (8 pintu teks, transisi opsional); SENGAJA tanpa urutan adegan contoh, kerangka dari `opener-konsep.md` |
| `assets/starter-explainer.html` | EXPLAINER gaya aksi kontinu (vektor): mode aliran (strip + hero + objek dunia) + view peta + whip + contoh mode kolase |
| `assets/starter-explainer-kartun.html` | EXPLAINER kartun kolase: kertas krem + grain + noda, cutout ilustrasi, Bricolage + Caveat, pill warna |
| `assets/starter-explainer-jurnalisme.html` | EXPLAINER jurnalisme visual: hitam + grain, foto asli + tag sumber, Barlow Condensed + Plex Mono, highlighter kuning/merah, anotasi putus |
| `assets/starter-explainer-katalog.html` | EXPLAINER katalog putih: grid samar, cutout foto, Archivo Black + Caveat + Inter, highlighter kuning |
| `assets/starter-explainer-sketsa.html` | EXPLAINER sketsa vintage: kertas sepia (tekstur CSS), cutout ukiran multiply, Playfair + Garamond + Cinzel, karat & emas |
| `scripts/serve.py` | dev server no-cache (opsional, butuh Python; hanya bila memakai module lokal) |
| `scripts/snap.mjs` | VERIFIKASI: potret detik kunci → lembar kontak (opsional, butuh Node + puppeteer) |
| `scripts/vo-pauses.html` | deteksi jeda VO di browser (pengganti ffmpeg silencedetect, tanpa instal) |
| `scripts/export-frames.mjs` | EXPORT: render semua frame → MP4, hanya bila diminta (opsional, butuh Node + puppeteer + ffmpeg) |
