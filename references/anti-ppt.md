# Anti-PPT — hukum desain adegan

Dokumen ini adalah alasan skill ini ada: hasil yang "secara teknis benar" tetap
gagal bila terasa seperti presentasi PPT.

## Kenapa model selalu jatuh ke pola slide

Model dilatih menyusun INFORMASI: judul → penjelas → bukti pendukung.
Struktur itu bagus untuk dokumen, dan fatal untuk motion graphic.
Video promosi tidak menjelaskan — ia **menyatakan**, satu pukulan per shot,
dan membiarkan gerakan + musik yang membawa emosinya. Kalau kamu merasa
sebuah adegan "kurang informasi", itu justru tanda adegannya sudah benar.

## Tabel pelanggaran → perbaikan

| Pelanggaran | Perbaikan |
|---|---|
| Kicker "02 — FITUR" + judul 2 baris + body copy 2 baris + 4 chip badge, layout kolom kiri-kanan | Satu kalimat ≤ 5 kata di tengah-atas + satu objek produk naik ke tengah |
| Tiga baris teks besar berisi tiga klaim "TANPA …" | Headline 2 kata + satu cara dari menu fitur (`opener-konsep.md`): satu fitur didemokan, kata berganti, objek bertransformasi, kartu dikocok, grid tile… — dipilih per proyek |
| Opener produk B memakai kulit opener produk A (palet, glow, nebula, font yang sama) karena diambil dari starter/proyek lama | Gaya diturunkan dari brand B lewat style brief: palet dari logo/ikon B, font berkarakter lain, bahasa latar lain, tanda tangan gerak lain (SKILL.md Hukum #3) |
| Semua judul KAPITAL SEMUA, font lebar bobot 800, selalu di tengah, masuk dengan stagger huruf yang sama — terasa kaku | Sentence case bobot 500, penekanan pada kata kunci (sorotan kata opsional — bisa juga kata per kata, ukuran, jeda, objek di samping kata), tanpa titik otomatis (tanda baca hanya bila mengubah arti), ukuran/arah/posisi bergantian (techniques.md §1) |
| Setiap judul/klaim diakhiri titik, termasuk frase dua kata — terasa kaku dan seperti template | Default tanpa titik; `?` untuk pertanyaan sungguhan, titik hanya untuk gaya dua kalimat pendek yang disengaja dan konsisten (techniques.md §1 aturan 5) |
| Ladang 96 batang cahaya putih ber-bloom di belakang judul — latar ramai, teks tidak kontras | Kantong gelap di bawah teks, partikel berwarna sisi gelap palet dan redup, ≤ 40 elemen terang, bloom hanya di objek (techniques.md §1b) |
| Semua opener gelap dengan nebula/partikel, latar tidak pernah dipertimbangkan per segmen | Latar dari tema (gradien terang, warna lembut, blok warna, kertas, foto, atau gelap); pergantian diputuskan per segmen di style brief dan terjadi di balik cut/wipe (techniques.md §7b) |
| Setiap opener memberi kata sorotan (garis bawah/pill) di setiap kalimat, atau memakai pill + bintang yang sama persis dengan proyek lain | Sorotan kata opsional dan diputuskan di style brief; bila dipakai, satu bentuk per video yang dipilih per proyek, tidak di setiap kalimat, ornamen hanya dari bentuk brand (techniques.md §1) |
| Opener app/SaaS hanya menampilkan screenshot diam yang di-zoom atau digeser | UI dirakit ulang dari komponen produk, dipakai (kursor, jari, atau UI yang bereaksi sendiri), data mengisi, transisi dibawa UI (`opener-konsep.md` bagian animasi UI) |
| Video ditempel layar penuh dengan `autoplay loop`, berjalan dengan jamnya sendiri, dan animasi lain berhenti selama klip diputar | Klip dipasang lewat `clip()` sebagai layer footage yang terikat timeline, dibungkus wadah/perangkat/bingkai yang ikut dianimasikan, teks dan anotasi tetap hidup di atasnya (techniques.md §9b) |
| Dua opener untuk produk berbeda sama-sama berlatar batang/potongan cahaya melesat ke samping ("lane" / "range") — hasil aturan "objek melintas tiap detik" | Gerak latar dipilih dari menu techniques.md §7c (gradien berpindah, blob, grain hidup, sapuan cahaya, bentuk berputar, partikel naik, grid bernapas…) dan berbeda dari proyek sebelumnya; aliran horizontal hanya untuk tema kecepatan/aliran |
| Transisi: balok/persegi warna datar raksasa menyapu miring di setiap cut ("kotak persegi aneh"), atau garis tipis menyapu | Menu transisi techniques.md §4c: push-through 3D, kartu berputar dari kedalaman, objek berketebalan melewati lensa, mask bentuk brand, sapuan cahaya; minimal dua jenis, satu berkedalaman, wipe ≤ 2 |
| Latar flat satu warna (gelap atau terang) dari awal sampai akhir | Permukaan latar ≥ 2 lapis dari menu §7d: glow horizon, duotone diagonal, mesh blob, spotlight + tint, langit berlapis, tekstur — warna dari palet |
| Latar diam, atau warna latar tidak pernah berganti walau segmen/energi berubah | Latar selalu bergerak (§7c); warna latar boleh berganti kapan dibutuhkan asal ada pemicu terlihat: benda menutup lensa, aksi UI, push ke bidang warna, medan menyapu, cut di ketukan (techniques.md §7b) |
| Menyalin palet, font, dan tata letak video referensi yang disodorkan user | Ambil ritme dan energinya saja; kulit lahir dari tema produk — katakan itu ke user satu kalimat |
| Menampilkan `com.example.app` (nama package) di adegan CTA | Dihapus. User tidak peduli; kalau perlu, cukup baris hasil pencarian store |
| Teks in/out dengan kamera statis | Ukuran shot berganti ke elemen yang sedang bercerita (techniques.md §3b) + koreografi elemen beririsan (§4b); napas kamera sebagai lapisan dasar; push-through hanya bila termotivasi, ±1 per video |
| "Zoom in-out" dikerjakan sebagai napas kamera beberapa persen — tidak terlihat, video tetap terasa statis | Pergantian ukuran shot yang jelas: kamera mendekat ke elemen (medium close-up / close-up) lalu mundur ke wide saat komposisi butuh seluruh frame; label di lapisan layar supaya tidak terpotong (techniques.md §3b) |
| Glow tebal 4 lapis di semua judul | Judul putih bersih + drop shadow tipis; glow disimpan untuk OBJEK (objek produk, ornamen) |
| Latar warp 520 garis putih panjang | 300 partikel pendek berwarna gelap senada — latar tidak boleh bersaing dengan subjek |
| Latar biru merata (flat) | Gradasi vertikal tegas: nyaris hitam di atas, menyala di horizon bawah |
| Elemen UI (badge status) muncul mendahului kalimat utamanya | Urutan atensi: kalimat → objek utama → detail pendukung |
| Zoom push-through dipakai di SEMUA transisi | Perpustakaan gerakan: spin, yaw 3D, roll, elemen terbang melewati lensa; zoom hanya saat termotivasi (mis. menyelam ke layar mockup). "Satu jenis transisi di semua cut" = template transisi PPT, cuma versi mahal |
| Whip-pan translasi — tepi panggung tersingkap jadi gap hitam | Terbaca "pindah halaman". Jangan pernah menggeser dunia sampai tepinya terlihat |
| Spin/yaw/roll kejut (zoom+putar tiba-tiba dengan blur di tiap cut) | Itu bahasa PRESET editor video, bukan motion design. Ganti: kamera bernapas + koreografi elemen beririsan + object wipe |
| Demo UI terasa statis: UI penuh di frame, kamera diam, hanya kursor bergerak, klik terlalu kecil untuk terbaca | Kamera mengikuti interaksi bila perlu: dekati area yang akan diklik (scale 1,4–2,2, 0,6–0,9 dtk ease in-out), klik terbaca, lalu mundur/geser ke hasilnya; tidak di setiap klik (techniques.md §8) |
| Opener produk berbeda-beda keluar dengan kerangka sama: teks zoom lalu keluar ke kiri, tiga tile fitur, kotak input diketik, hook → fitur → fitur → janji → logo → CTA — kesannya template walau warnanya baru | Tiga kandidat konsep dari `opener-konsep.md`, satu dipilih dari sifat produk; sidik jari struktur berbeda dari opener sebelumnya; komponen kanonik maks dua dan hanya bila dituntut konsep |

## Pola gagal yang umum pada explainer

Contoh explainer sejarah 30 dtk, 6 adegan, yang terasa seperti PPT. Kodenya:

| Yang dibuat | Kenapa PPT | Yang seharusnya |
|---|---|---|
| 6 × `<section class="scene">` berisi foto full-bleed, dinyalakan `autoAlpha` bergantian | Ganti section = ganti slide, apa pun transisinya | Satu dunia yang mengalir; adegan berganti karena kamera/dunia bergerak atau whip ke sudut lain |
| Tiap section: eyebrow (kicker) + judul 2 baris + kredit | Tiga tingkat teks = layout slide | Satu angka/kalimat besar + satu label yang hidup di dunia |
| Gerak hanya Ken Burns foto 1.08 → 1.015 dan scale bump `#world` 1.12 → .96 di tiap cut | Gerak yang sama di semua cut = template | Parallax, objek melintas, whip, instrumen (peta/profil/speedometer), kamera bernapas beda per momen |
| Light leak di setiap cut | Preset editor video | Simpan untuk satu momen istimewa |
| Tidak ada subjek yang bertahan antar adegan | Tidak ada yang "dibawa" penonton | Hero hadir > 60 % durasi |

Pelajaran: hukum naratif saja tidak cukup; perlu larangan struktural yang bisa diperiksa dari kode
(SKILL.md → "Larangan struktural") dan starter yang memaksa rig yang benar
(`assets/starter-explainer.html`).

## Prinsip yang bisa dibawa ke proyek mana pun

1. **Satu shot = satu pernyataan.** Kalimat ≤ 5 kata lebih kuat daripada
   kalimat lengkap. "Dua kata. Satu pukulan." mengalahkan "Aplikasi ini
   bisa melakukan X, Y, dan Z untuk kamu".
2. **Hierarki atensi per adegan:** kalimat dulu, objek utama menyusul,
   detail paling akhir — jangan pernah terbalik.
3. **Teks panjang adalah bug.** Kalau sebuah klaim butuh > 6 kata,
   pecah jadi dua adegan atau ubah jadi visual (ikon, angka, mockup).
4. **Metadata bukan konten.** Nama package, URL panjang, versi, footnote —
   buang. Penonton awam tidak membacanya, penonton teknis tidak membutuhkannya.
5. **Mockup UI adalah pengecualian teks banyak** — layar aplikasi boleh penuh
   teks kecil karena ia dibaca sebagai GAMBAR, bukan sebagai teks. Justru
   itu: mockup harus setia pada aplikasi aslinya (font, warna, layout).
6. **Gerakan adalah kalimatnya juga.** Zoom masuk = penekanan; pan menyusur =
   pengungkapan bertahap; pull-back = reveal; bounce kecil = playful.
   Pilih gerakan yang searti dengan kalimatnya, jangan acak.
7. **Transisi ala motion designer, bukan preset editor.** Dua kegagalan
   umum: whip translasi menyingkap tepi ("pindah halaman"); spin/yaw kejut
   terbaca efek preset editor. Yang benar:
   (a) kamera BERNAPAS — drift zoom pelan tanpa henti, tak pernah
   menyentak; (b) perpindahan dikerjakan KOREOGRAFI ELEMEN yang keluar-
   masuk beririsan waktu; (c) OBJECT WIPE — sebuah elemen/ornamen menyapu
   dekat lensa menutup frame, adegan berganti di baliknya; (d) zoom cepat
   hanya bila TERMOTIVASI (menyelam ke layar mockup). Efek kejut apa pun
   (zoom/putar tiba-tiba + blur di tiap cut) adalah tanda bahaya.
8. **Kamera adalah pemersatu.** Sekali kamu punya rig kamera yang menggerakkan
   seluruh dunia, adegan-adegan terpisah terasa satu film. Tanpa itu,
   berapapun polesan per adegan, hasilnya tetap deck yang di-autoplay.
9. **Ritme keluar-masuk asimetris.** Masuk pelan-tegas (0.7–1.3 detik,
   `power4.out`), keluar cepat (0.35–0.55 detik, `power2.in`). Simetris
   terasa mekanis.
10. **Pilih 1–2 momen istimewa.** Efek paling mahal (pan 3D per kata, logo
   build-on) dipakai sekali-dua kali saja. Dipakai di semua tempat,
   berhenti terasa istimewa.
11. **Kalau ragu, gelapkan latarnya dan besarkan teksnya.** Kontras adalah
    produksi termurah yang paling sering dilupakan.

## Kalibrasi rasa (heuristik cepat)

Screenshot sebuah frame lalu tanya:

- Bisakah frame ini jadi slide korporat tanpa diubah? → gagal, rombak.
- Apakah mataku tahu harus melihat ke mana dalam 0,2 detik? → kalau tidak,
  kurangi elemen.
- Kalau semua teks disembunyikan, apakah latarnya masih menarik tapi tidak
  berisik? → keduanya harus ya.
- Apakah ada sesuatu yang BERGERAK karena kamera, bukan karena elemen
  menganimasikan dirinya sendiri? → harus ya di tiap transisi.
