# Explainer — cerita bergambar, bukan promo

Untuk kartun edukasi flat berkarakter (gaya 6, **kartun panggung**: satu panggung
per adegan, rig sendi, nol caption), baca [kartun-panggung.md](kartun-panggung.md).
Jumlah kalimat tidak menentukan jumlah shot; lebih banyak gerak kamera juga
bukan otomatis lebih menarik. Bagian resep kolase di bawah adalah opsi, bukan
pola wajib bagi semua explainer.

Dua gaya explainer yang paling sering dipakai:

| | Kartun + VO | Jurnalisme visual (foto) |
|---|---|---|
| Cocok untuk | sains/edukasi, ±75 dtk, 9:16 | berita/geopolitik, ±75 dtk, 9:16 |
| Latar | kertas krem bertekstur + noda warna | hitam pekat + grain tipis |
| Gambar | ilustrasi flat digenerate (GPT Image 2) lalu latar dihapus → cutout | foto asli berlisensi bebas (Wikimedia Commons, NASA, DVIDS) |
| Teks | Bricolage Grotesque tebal + Caveat (tulisan tangan) | Barlow Condensed tebal + IBM Plex Mono (kicker) |
| Aksen | pill warna (oranye/teal/merah/mustard), coretan spidol | highlighter kuning, merah untuk peringatan, garis putus |
| Suara | VO diikat ke timeline | tanpa VO — teks membawa cerita, beat 3–5 dtk untuk dibaca |

Opener menjual satu perasaan; explainer **mengantar satu argumen**. Hukum
anti-PPT tetap berlaku, tapi dengan dua kelonggaran: satu adegan boleh punya
kalimat + satu angka/anotasi, dan mockup/peta/grafik boleh "padat" karena
dibaca sebagai gambar.

## Langkah nol: pastikan gayanya, rasio, durasi, suara

User sering hanya bilang "buatkan explainer tentang X". Kalau dibiarkan,
model mengarang gaya, rasio, DAN durasi — bisa jadi 10 menit. Sebelum
menulis apa pun, ajukan SATU pertanyaan (pakai mekanisme tanya-jawab agenmu
bila ada; kalau tidak, tulis daftarnya dan tunggu jawaban) berisi empat hal.
Lewati bagian yang sudah disebut user; bila ada video referensi, gaya
diambil dari sana (ritmenya — lihat SKILL.md Hukum #3).

**Gaya** (sertakan satu baris rekomendasi: sejarah → 4 atau 1; berita → 2;
produk → 3; gerak/rute → 5; sains/edukasi berkarakter → 6; topik ringan → 1):

| # | Gaya | Rasanya | Cocok untuk | Aset |
|---|---|---|---|---|
| 1 | Kartun kolase | kertas krem, cutout ilustrasi flat, pill warna, tulisan tangan | edukasi sains/anak, topik ringan | ilustrasi digenerate → latar dihapus |
| 2 | Jurnalisme visual | hitam, foto asli, highlighter kuning, tag sumber | berita, isu viral, geopolitik | foto berlisensi bebas (Wikimedia/NASA) |
| 3 | Katalog putih | putih bergrid, cutout foto, tipografi campur, coretan | produk, brand, profil perusahaan | foto produk/orang, latar dihapus |
| 4 | Sketsa vintage | kertas sepia, ukiran/etsa, serif klasik, anotasi karat | sejarah, biografi, penemuan | ilustrasi gaya ukiran digenerate |
| 5 | Aksi kontinu (vektor) | dunia mengalir, satu subjek, angka di dalam dunia, ganti sudut | kecepatan, rute, transportasi, olahraga, proses | 100 % SVG digambar, tanpa generate |
| 6 | Kartun panggung | flat cerah, satu panggung per adegan, tokoh bersendi beraksi, mesin/air/tanaman hidup, tanpa caption | edukasi sains/sosial berkarakter, proses & dampak, cerita | tubuh & dunia vektor; kepala digenerate → ekspresi lokal |

**Tiga hal lain dalam pertanyaan yang sama:**

| Hal | Pilihan | Default bila "terserah" |
|---|---|---|
| Rasio | 16:9 (YouTube/layar) · 9:16 (Reels/TikTok/Shorts) · 1:1 | 16:9 |
| Durasi | 30 dtk · 60 dtk · 90 dtk | 60 dtk |
| Suara | tanpa suara · VO dikirim user nanti (bangun dulu, retime kemudian) · musik saja | tanpa suara, naskah VO tetap ditulis |

Yang TIDAK ditanya: caption (default tanpa) dan player (default tanpa,
autoplay + loop).

**Pagar durasi:** ikuti durasi brief dan VO; default tetap ringkas. Jumlah
adegan ditentukan oleh konteks yang berubah. Beberapa kalimat dapat memakai
satu dunia dengan aktivitas yang berkembang. Materi berlebih dipotong,
bukan videonya dipanjangkan. Permintaan "10 menit" → konfirmasi, lalu pecah
per bab ≤ 90 dtk dengan berkas terpisah.

## Penyerahan: naskah VO ikut di pesan, user yang mengisi suaranya

Explainer hampir selalu berakhir dengan VO dari user (direkam sendiri atau
di-generate di layanan TTS pilihannya). Jadi urutan bakunya: bangun tanpa
suara dengan timing baca → serahkan `index.html` + naskah VO DI DALAM pesan
penutup → minta user merekam/generate dan mengirim ulang audionya → retime
video ke audio itu. Contoh penutup:

> Naskah VO (satu paragraf = satu adegan, angka ditulis dengan kata):
> 1. …
> 2. …
> Rekam atau generate dengan suara pilihanmu — bicara wajar, jeda ±1 detik
> antar paragraf, format wav/mp3 bebas — lalu kirim ke sini; videonya akan
> saya sinkronkan ke suara itu.

Naskah yang sama disimpan sebagai `vo-script.md`. Jangan hanya menulis
"naskah ada di berkas": user membaca pesan, bukan folder.

## Mulai dari starter yang benar

Explainer SELALU dimulai dari starter gayanya (folder `assets/`):
`starter-explainer-kartun.html`, `starter-explainer-jurnalisme.html`,
`starter-explainer-katalog.html`, `starter-explainer-sketsa.html`, atau
`starter-explainer.html` untuk aksi kontinu. Kelimanya satu rig; yang beda
hanya PERMUKAAN (tekstur latar, jenis aset, font, warna). Dua mode gerak:

| Mode | Dunia | Gerak utama | Gaya yang memakainya |
|---|---|---|---|
| ALIRAN | strip parallax mengalir dari profil kecepatan, subjek diam di frame, objek dunia melintas | dunia bergerak | aksi kontinu (vektor) |
| KOLASE | kertas/foto/putih diam berisi cutout & foto, boleh lebih besar dari frame | kamera: `into` → `settle` → `look` → `home` lalu DIAM; aset `fly` dan tetap bergoyang | kartun kolase, jurnalisme foto, katalog putih, sketsa vintage |

Keduanya boleh dicampur dalam satu video (mis. kolase untuk sejarah, lalu
whip ke peta simulasi). Starter kolase sudah berisi contoh koreografi wajib:
mulai close-up aset A → `look` ke aset B → `home` (zoom out selesai) → baru
`say` kalimat + `draw` anotasi + label → `unsay` → `into`/`settle`
push-through ke adegan 2 yang letaknya di luar frame (bukan section
di-fade).

Jebakan scrub: `tl.pause(t)` GSAP menekan callback (`suppressEvents`), jadi
`onUpdate: applyCam` tidak jalan saat snapshot/scrub walau saat diputar
normal jalan. `seek` harus `tl.pause(t,false)` lalu `applyCam()`. Yang tidak boleh: menulis dari nol atau dari starter
opener — hampir pasti berujung "section yang di-fade".

## Default yang sering salah dikira

- **Rasio: default 16:9 (1920×1080) atau mengikuti layar user.** 9:16 HANYA
  bila user memintanya (Reels/TikTok/Shorts). Jangan berasumsi explainer =
  vertikal.
- **Tanpa player.** Autoplay + loop; panel scrub hanya `?debug=1`.
- **Tanpa subtitle/caption.** Default tidak ada teks pendamping VO di bawah
  layar; caption hanya bila user minta. Informasi dibawa oleh angka besar,
  label yang hidup di dalam dunia (papan nama, tanda stasiun), dan gambar.
- **Pelajari prinsip referensi, jangan salin perangkat tata letaknya.** Panel
  tiga kolom, subtitle bawah, bentuk odometer — kalau referensi memakainya,
  itu contoh, bukan resep. Ambil prinsipnya (angka di dunia, subjek terus
  bergerak) lalu wujudkan dengan cara sendiri.
- **Panggung diskalakan ke jendela dengan `position:absolute; left:50%;
  top:50%; transform:translate(-50%,-50%) scale(s)`**, bukan grid
  `place-items:center` — sel grid ikut setinggi panggung mentah, sehingga
  panggung terdorong ke bawah dan terpotong.

## Struktur yang dipelajari dari referensi (bukan ditiru)

Explainer kolase dan explainer jurnalisme visual yang baik punya tulang
yang sama, dan tulang inilah yang boleh dipakai ulang:

1. **Hook** = satu gambar + satu klaim yang bikin penasaran (viral, angka
   aneh, pertanyaan).
2. **Pertanyaan eksplisit** di layar ("Kenapa bisa?", "Kenapa tahun ini?").
3. **Konteks visual**: peta / foto lokasi / ilustrasi dunia, dengan label
   dan satu lingkaran merah di titik penting.
4. **Angka besar** yang menghitung naik, lalu dibandingkan (bar sebelum/sesudah).
5. **Linimasa** 2–3 tanggal, satu kalimat per tanggal.
6. **Grafik** yang menggambar diri (garis harga, area di bawahnya).
7. **Dampak ke penonton** ("terasa di dompet sehari-hari").
8. **Penutup yang menggema ke hook** + daftar sumber kecil.

Jangan ambil: palet, font, layout persis, maskot, kalimat. Ganti semuanya.

## Satu adegan = 3–5 elemen yang menumpuk (bukan satu gambar)

Kegagalan yang umum: tiap adegan hanya SATU cutout + satu kalimat. Walau kamera
sudah bergerak, penonton tidak tahu "seperti apa" hal yang diceritakan — satu
simbol tidak cukup menjelaskan. Explainer jurnalistik yang baik (±20 beat per
30 dtk) memakai pola berikut:

1. **Akresi per frasa.** Tiap frasa VO MENAMBAH satu elemen; elemen lama
   tetap di tempat. Adegan selesai dengan 3–5 elemen (maksimal 5) yang
   bersama-sama menjelaskan: subjek (foto/cutout) + bukti (dokumen, kliping,
   layar) + skala (angka atau grid pengulangan) + label/stempel tanggal +
   coretan. Contoh "pesan musuh tak terbaca" = kapal → kapal selam melintas →
   radio penyadap → lembar telegram berisi sandi yang terus berganti + stempel
   RAHASIA → kalimat.
2. **Bukti, bukan hiasan.** Pilih elemen yang menjawab "seperti apa
   bentuknya?": dokumen ketik dengan stempel (nama perkara · BERSALAH),
   kliping koran dengan frasa disorot, kartu sumber (badge media + judul),
   layar/mockup, blok tanggal. Dokumen dibangun di HTML (kertas putih +
   border tipis + mono + stempel miring merah) — tidak perlu digenerate.
3. **Pengulangan untuk skala.** Satu gambar diperbanyak jadi grid (foto anak sekolah
   jadi puluhan; satu rotor mesin jadi 12 rotor)
   dengan stagger `back.out` — lebih terasa daripada angka saja. Angka
   tetap ada, tapi bukan satu-satunya.
4. **Foto → dokumen.** Foto zoom out lalu ternyata ada di sampul majalah /
   koran; blok tahun muncul di sebelahnya. Satu aset, dua makna.
5. **Elemen yang bergerak sendiri** (deterministik dari `tl.time()`):
   huruf sandi berganti lalu terurai jadi teks terbaca, jarum jam berlari ke
   tengah malam, angka menghitung naik, palu hakim mengetuk.
6. **Kamera tetap satu per adegan**: elemen menumpuk di area yang sama;
   kamera `look` sedikit (±200 px, z 1–1,15) untuk menyambut elemen baru.
   Elemen baru = look kecil, bukan cut.
7. **Batas teks tidak berubah**: satu kalimat besar + satu label per adegan.
   Dokumen/stempel/blok tanggal/catatan tangan dihitung OBJEK (dibaca sebagai
   gambar) bukan tingkat teks — syaratnya isi ≤ 3 baris pendek.
8. **Aset tambahan cepat**: properti fotoreal "studio product photo,
   isolated on pure white" (Higgsfield `gpt_image_2_5`, tanpa wajah orang
   nyata) ditumpuk `mix-blend-mode:multiply` — latar putihnya lenyap di atas
   grid tanpa hapus latar. Jangan beri `drop-shadow` pada elemen multiply
   (bayangannya jadi persegi); bayangan sudah ada di fotonya. Foto arsip
   berlatar rumit tetap lewat `image_background_remover` (butuh `prompt`),
   lalu pangkas margin transparan (bbox alpha) supaya ukuran CSS = isi.
9. Kalau `remove_background` menghapus subjeknya (kapal hilang, tersisa
   haluan kapal lain), jangan dipaksa — generate properti pengganti.

Helper di `assets/starter-explainer-katalog.html`: `slam` (stempel
dihentak), `block` (blok tanggal disingkap dari kiri), `multiply` (grid
beruntun); CSS `.doc`, `.stampblk`, `.pnote`, `.grid`, `.cut.card`.

## Resep teknis

**Panggung 9:16**: `#stage` 1080×1920, `fit()` sama seperti 16:9. Judul
88–168 px, kicker mono 26 px, kredit foto 20 px kiri-bawah.

**Kalimat per kata** (`say/unsay`): tiap kata `<span class="wd">` (nowrap)
masuk `yPercent 60→0, scaleY 1.3→1`, stagger 0.07–0.12, blur vertikal;
kata kunci `<span class="wd hl"><i></i>kata</span>` — `<i>` adalah
highlighter yang `scaleX 0→1` dari kiri SETELAH kata-katanya selesai
(`hlAt`). Frasa yang harus bisa patah baris JANGAN dijadikan satu `.wd`
(itu penyebab teks meluber ke luar frame di 9:16).

**Foto** (`photo(sel, at, end, {from,to,x,y})`): `object-fit:cover`, masuk
dengan blur berarah, lalu Ken Burns `scale 1→1.12–1.25` + geser sedikit
sepanjang adegan (`ease:'none'`). Gradasi gelap di atas/bawah (`.dim`,
`.top`) supaya teks kontras. Grain ringan `mix-blend-mode:overlay`.

**Cutout ilustrasi** (`enter/leave`): masuk dari bawah dengan overshoot
`back.out(1.4)`, drop-shadow di elemen pembungkus. Filter warna (grayscale)
taruh di `<img>`, bukan di pembungkus — `blurTween` menulis `filter` pada
pembungkus dan menghapus filter lain.

**Anotasi SVG** (`draw`): `strokeDasharray = L`, `strokeDashoffset L→0`.
Set `opacity:0` sampai detik mulainya — linecap bulat pada panjang 0 tampak
sebagai titik nyasar. Garis putus-putus tidak bisa pakai dashoffset (akan
"berjalan"); pakai `clip-path: inset()` yang dibuka dari kiri (`drawDash`).

**Peta**: citra satelit domain publik (NASA MODIS/Worldview) sebagai dasar +
label `.tag` mono dengan garis kiri kuning + lingkaran merah + garis putus
jalur. Lebih jujur dan lebih cepat daripada menggambar peta sendiri.

**Grafik garis**: hitung titik dari data di JS, `path` digambar dengan
dashoffset, area gradasi fade-in setelahnya, titik data pop stagger, label
hanya untuk 2–3 titik penting (awal, puncak, terakhir).

**Angka besar**: tween objek `{v}` → `textContent = Math.round(v)`;
`font-variant-numeric: tabular-nums`.

**Tint per adegan**: lapisan `.tint` full-frame (malam/dingin/gelap) di
dalam `#world`, di-tween opacity — murah dan langsung mengubah mood.

**Potongan antar adegan** (`cut`): dorong dunia 1.05× lalu adegan baru
lahir 1.08–1.12× dan mengendap ke 1 dalam 0.8 dtk; elemen lama keluar ke
atas dengan blur SAMBIL yang baru masuk. Kamera tetap bernapas di antara.

**Retime ke VO yang datang belakangan** (video dirancang dulu tanpa suara).
Tanpa ffmpeg: buka `scripts/vo-pauses.html`, pilih audionya, salin `SEG`
(mulai tiap potongan ucapan), `PARA` (mulai tiap paragraf = adegan) dan
`DUR`; angkanya identik dengan `silencedetect` (ambang -30 dB relatif
puncak, jeda >= 0,45 dtk, paragraf >= 0,8 dtk; ubah bila VO berisik).
Langkahnya:
jangan tulis ulang build(). Bungkus `tl.to/fromTo/set` dengan pemetaan
posisi linear per adegan `T(t)` dari batas adegan lama (OLD) ke awal
paragraf VO (NEW, dari silencedetect jeda ≥0,9 dtk; VO bernoise perlu
ambang −25 dB). Durasi tween tetap; hanya posisinya yang meregang. Transisi
push-through dihitung langsung di waktu baru (`T(cut)-.9`) supaya tetap
presisi. Satu berkas VO lebih mudah daripada delapan klip.

**VO diikat timeline** (kalau ada): `<audio>` per klip + `syncAudio()` di
loop rAF: bila timeline play dan `t` di dalam rentang klip → `currentTime =
t - start`, play; bila tidak → pause. Perlu tombol "Mulai" pertama karena
autoplay. Durasi adegan ikut durasi klip (ukur dulu dengan ffprobe).

## Sumber gambar

- **Digenerate** (kartun): Higgsfield `gpt_image_2` (1k, medium), prompt
  satu gaya untuk semua aset ("flat vector, outline coklat tebal, warna
  hangat, latar putih polos"), lalu `remove_background` → PNG transparan.
  Generate dalam satu batch supaya gayanya seragam.
- **Foto asli** (jurnalistik): Wikimedia Commons API
  `action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1920`
  → cek `LicenseShortName` (Public domain / CC BY / CC BY-SA), unduh thumb
  1920 px, tulis kredit di layar. NASA (MODIS/Worldview) dan DVIDS/DoD
  domain publik. Jangan pakai screenshot berita/TV.
- Kalau foto lokasi persis tidak ada, pakai foto sejenis dan beri label
  "ilustrasi" — jangan berpura-pura.
- **Video pelengkap**: klip 3–8 dtk sebagai layer footage (`techniques.md` §9b) — dari user,
  stok berlisensi, atau generate lewat MCP bila disetujui (label "ilustrasi/rekonstruksi" pada
  topik faktual). Klip tetap dibungkus desain adegan: kartu, bingkai, anotasi, angka.

## Entitas yang disebut WAJIB tampil (aturan krusial)

Kegagalan yang umum: nama perusahaan disebut tanpa foto perusahaannya, nama
penemu disebut tanpa wajahnya, "17 pabrik" tanpa pabriknya, produk disebut
tanpa kemasannya — penonton tidak bisa mengaitkan kata dengan gambar. Prosedur:

1. Dari naskah, tulis **daftar entitas**: orang, perusahaan, gedung/kota,
   produk/varian, peristiwa. Tiap entitas = satu gambar di adegannya.
2. Urutan sumber: foto bebas lisensi (Commons/NASA) → foto resmi dari situs
   produk/artikel (`og:image` halaman, kredit dicantumkan) → foto kiriman
   user → generate fotoreal berlabel "ilustrasi" hanya untuk tempat/objek
   generik (pabrik, lini produksi), **tidak pernah** untuk wajah orang nyata.
3. Foto orang dari komposit/meme (mis. tangkapan layar viral) boleh dipotong
   dan dihapus latarnya jadi cutout — hasilnya justru cocok dengan gaya
   kolase. Cantumkan sumbernya.
4. Kalau semua gagal, tanya user sebelum memakai siluet/placeholder.

## Keterbacaan di ponsel (aturan keras)

Keterangan ilustrasi 22 px dan sub-label nama 26 px hampir tidak bisa dibaca,
apalagi di ponsel. Video 9:16 ditonton di layar ±6 inci,
dan safe-area scale 0,78 memperkecil semuanya lagi. Ukuran MINIMUM pada
panggung 1080 px (sebelum safe-scale):

| jenis teks | minimum |
|---|---|
| body copy / keterangan | 44 px |
| label nama, kicker, tahun | 34 px (sub-label 32 px) |
| kredit / sumber | 30 px, kontras cukup (opacity ≥ .6) |
| anotasi tulisan tangan | 48 px |
| judul | 100 px ke atas |

Kalau memakai safe-scale, kalikan 1/0,78 dulu. Tidak ada teks di bawah
30 px, titik. Kalau ada informasi yang "tidak muat", pecah ke adegan lain
atau buang — bukan dikecilkan.

## Variasi, bukan pola tetap

Dua kebiasaan yang membuat video terasa "itu-itu saja":

- **Teks hantu / angka tahun besar**: pilih SATU gaya untuk satu video
  (outline di satu adegan dan isi di adegan lain terasa tidak
  konsisten) — dan pastikan terlihat: isi transparan ≥ .18–.25, jangan
  .08–.12 karena menyatu dengan latar. Gaya lain (outline, blur, terpotong
  tepi) dipakai di video lain, bukan dicampur dalam satu video.
- **Lingkaran / anotasi** tidak harus putus-putus. Bergantian: garis utuh
  tipis, garis warna aksen, garis ganda, kotak sudut, garis bawah tangan,
  atau tanpa lingkaran sama sekali.

## Aset harus terasa hidup

Ayunan cutout ±10 px selama 2 dtk terlihat statis. Minimum:
ayunan ±22–28 px dengan durasi 1,3–1,8 dtk (`sine.inOut`, yoyo), ditambah
putaran kecil ±1,5° dan pertumbuhan skala 1→1,06 pelan sepanjang adegan,
serta geser x beberapa belas px. Beri fase/durasi berbeda per objek supaya
tidak serempak. Untuk objek besar (kapal, kota) tambahkan gerak arah
(berlayar, dorong kamera) dengan `ease:'none'`.

## Resep kamera kolase: close-up → meluncur → zoom out

Ini satu resep untuk kolase berteks. Untuk animasi karakter/proses, kamera dapat
menetap, mengikuti subjek, atau menyusuri sistem setelah reveal awal. Jangan
memaksakan resep ini pada setiap segmen; gunakan kebutuhan narasi sebagai alasan.

Resep ini menjawab tiga kegagalan umum: (a) animasi yang hanya
"elemen masuk, elemen keluar" terasa PPT; (b) setelah kamera zoom out lalu
mendorong lagi ke catatan, "info lain terpotong"; dan potongan langsung dari
lebar ke close-up "terkesan tiba-tiba karena latar tiba-tiba zoom in".

- Rig `#world` = kamera: state `C={x,y,z}` (titik fokus dalam koordinat
  adegan + zoom), diterapkan tiap frame: `transformOrigin:'0 0'; scale:z;
  x:540-sx*z; y:960-sy*z` dengan (sx,sy) titik fokus setelah safe-scale.
  Helper `look(at,x,y,z,dur,ease)`; `HOME` = posisi identitas (pusat frame,
  z 1) — hitung dari safe-scale, bukan asal (540,960).
- **Pola per adegan**: lahir di close-up aset pertama (z ≈ 1,4, mengendap
  ke 1,32) → meluncur ke aset kedua sambil ia masuk → zoom out ke HOME saat
  judul muncul → **diam** di HOME sampai transisi. Tidak ada dorongan lagi
  setelah zoom out; catatan/rute cukup dianimasikan elemennya.
- **Transisi = push-through** (bukan jump): 0,9 dtk sebelum cut, elemen lama
  sudah pergi dan kamera mendorong (`power2.in`) ke titik aset pertama adegan
  berikutnya; tepat di cut adegan baru lahir di framing itu dan kamera
  mengendap (`power3.out`). Latar yang kontinu membuat potongan tak terasa.
  Aset pertama harus sudah masuk ≤ 0,1 dtk setelah cut supaya close-up tidak
  kosong.
- **Urutan wajib: zoom out SELESAI dulu, baru teks muncul.** Alasannya:
  teks yang lahir bersamaan (atau lebih dulu) dengan zoom out "terasa
  terpotong". Judul, body, label tahun, catatan tangan — semuanya
  dijadwalkan ≥ 0,1 dtk setelah `home()` selesai. Zoom out dibuat singkat
  (1,0–1,2 dtk) supaya masih ada waktu baca; kalau tidak muat, buang satu
  kalimat (kalimat pembuka yang sudah dibawa VO adalah kandidat pertama).
- Panorama (kota, kapal): pan menyusur 2,5–3 dtk pada z 1,3–1,5, baru ke
  HOME. Objek yang masuk dari samping "disambut" kamera yang ikut bergerak.
- Wajib: latar/kertas jauh lebih luas dari frame (`inset:-1400px`) dan
  vignette DI LUAR rig; jangan tumpuk tween scale lain pada rig (kamera
  bernapas digantikan koreografi ini).

## Format sosial (IG Reels / TikTok / Shorts)

- **Safe area**: bungkus semua adegan dalam `.safe{transform:scale(.78);
  transform-origin:50% 45%}` → margin atas ±190 px, bawah ±230 px pada
  1080×1920 supaya tidak tertutup caption/navigasi. Grid/latar tetap penuh.
- **Tanpa kontrol**: tidak ada overlay Play maupun slider. R = replay,
  spasi = pause. `?clean=1` tetap ada untuk render.
- **Suara harus terdengar sejak awal.** Browser memblokir audio autoplay tanpa
  gestur (juga di `file://`), dan user menganggap "suara tidak muncul"
  sebagai bug. Dua lapis:
  1. Di halaman: coba `vo.play()`; bila berhasil → play dari 0 bersuara.
  2. Bila ditolak: **JANGAN mulai tanpa suara** — tahan di frame awal dengan
     petunjuk kecil "ketuk / tekan tombol apa pun", lalu gestur pertama
     memulai video + suara bersamaan dari 0. (Memutar visual dulu lalu
     restart saat diketuk terasa seperti suara hilang.)
  Jangan membuat file peluncur (`.cmd`, `.bat`, skrip shell) untuk memaksa
  autoplay — deliverable cukup `index.html` (+ `assets/`). Trik
  play-muted-lalu-unmute juga tidak bekerja: unmute tanpa gestur tetap
  diblokir.

## Fakta

Explainer berita wajib sumber: cari dulu (EIA/lembaga resmi, media besar,
Wikipedia Current Events untuk tanggal), simpan daftar sumbernya di README
dan tampilkan ringkasannya di kartu penutup. Angka yang tidak terverifikasi
tidak ditampilkan — tulis klaim kualitatifnya saja.

## Jebakan yang sudah terjadi

| Gejala | Sebab | Obat |
|---|---|---|
| Kalimat meluber ke luar frame 9:16 | satu frasa panjang dijadikan satu `.wd` nowrap | pecah per kata |
| Mockup ponsel menutupi baris ke-3 judul | posisi ponsel dihitung untuk judul 2 baris | ukur tinggi judul asli, ponsel mulai ≥ 60 px di bawahnya |
| Cutout tetap berwarna padahal diberi grayscale | `blurTween` menimpa `filter` pembungkus | filter warna di `<img>` |
| Titik merah nyasar sebelum coretan digambar | linecap bulat pada dash length 0 | `opacity:0` sampai `draw` mulai |
| Latar kanvas WebGL tidak diperlukan | explainer 2D | lewati Three.js; cukup rig `#world` + tint + grain |


## Gaya ketiga: "katalog putih" (cutout foto di latar putih)

Ciri gaya: latar putih bergrid tipis, cutout produk, objek terbang melewati
lensa, lingkaran putus-putus, tipografi script + sans tebal miring.
Cocok untuk explainer produk atau merek (±60 dtk, 9:16, tanpa VO) dengan warna
dan foto asli — bukan hitam-putih, bukan kartun.

- Latar `#fff` + grid 120 px `rgba(0,0,0,.07)` yang dipudarkan ke tepi (mask
  radial). Tanpa grain, tanpa vignette — bersih.
- **Cutout** = foto Commons yang latarnya dihapus (impor URL ke Higgsfield
  `media_import_url` → `remove_background`; lebih andal daripada upload +
  PUT). Bayangan dua lapis `drop-shadow` (jauh lembut + dekat tipis).
- **Properti pendukung** (sumpit, globe, blok mi) boleh digenerate fotoreal
  "studio product photo, isolated on pure white" lalu dihapus latarnya.
- **Tipografi campur** per beat: script (Caveat) untuk penghubung ("lihat
  bagaimana", "lalu…"), sans 900 untuk subjek, italic 900 untuk angka/klaim,
  kicker mono-ish uppercase spasi lebar, body copy kecil abu-abu.
  Masuk: script `scale .7→1 back.out`, bold dari kiri dengan blur horizontal,
  body per baris.
- **Lingkaran putus-putus** di sekitar objek utama: `stroke-dasharray` tetap,
  digambar dengan `clip-path: inset()` dari kiri (bukan dashoffset).
- **Objek lewat lensa** (`pass`): cutout besar terbang diagonal dengan blur
  horizontal konstan, 1.2–1.3 dtk, lalu hilang — dipakai 1–2× per adegan.
- Peta dunia SVG opacity ~.16 + titik merah + garis putus rute.
- Jebakan: cutout tinggi (foto potret) mudah menabrak body copy — hitung
  tinggi dari rasio foto; taruh body copy DI ATAS peta/objek bila perlu.
- **Elemen bukti** (explainer tokoh sejarah ±50 dtk, 9:16, VO): kartu foto
  (`.cut.card`: foto arsip berbingkai putih 16 px, grayscale ringan),
  dokumen ketik (`.doc`: judul Inter spasi lebar + Plex Mono + stempel
  `.stamp` merah/hijau yang dihentak `slam`), blok tanggal (`.stampblk`
  hitam/kuning disingkap `block`), catatan tangan (`.pnote` Caveat di
  kertas krem), grid pengulangan (`.grid` + `multiply`), jam SVG dengan
  jarum yang di-tween `rotation` + `svgOrigin`. Lihat bagian "Satu adegan =
  3–5 elemen".
- 9:16: W=1080, H=1920, bungkus `#world` dalam `.safe` (scale .78);
  area adegan 1080×1920 disusun di dunia (jarak 1600 px mendatar, 2400–3000
  px menurun agar sisa cutout adegan sebelumnya tidak ikut terlihat), kertas
  grid dibuat 14000×12500 px supaya semua area tertutup.


## Gaya keempat: "buku sketsa vintage" (ukiran sepia di kertas tua)

Dipakai untuk explainer sejarah (mesin uap, 64 dtk, 9:16, tanpa suara).

- Semua gambar digenerate satu batch dengan prefiks prompt yang sama:
  "Vintage 19th-century copperplate engraving illustration, fine sepia ink
  cross-hatching, etching style … isolated on a plain white background, no
  text, no border". Potret tokoh sejarah: "engraved portrait … bust inside an
  oval" — sebut era/profesi, bukan nama, lalu beri label nama di layar dan
  kredit "ilustrasi gaya ukiran".
- Latar dihapus (remove background) lalu cutout dipasang dengan
  `mix-blend-mode:multiply` di atas tekstur kertas (juga digenerate, 9:16)
  supaya tinta "meresap" ke kertas; bayangan hanya untuk objek besar.
- Tipografi: serif display tebal (Playfair Display 900) + italic Garamond
  untuk kalimat penghubung + small-caps berspasi (Cinzel) untuk label tahun/
  nama; anotasi tulisan tangan warna karat; highlighter emas transparan.
- Tahun besar sebagai "ghost" outline di atas, label "Tempat · Tahun" di
  bawahnya — ini linimasa tanpa garis linimasa.
- Rate limit generator (maks 4 job bersamaan): kirim remove-background
  bertahap 3–4 sekaligus.


## Gaya kelima: "aksi kontinu" — satu subjek yang tidak pernah berhenti

Obat untuk explainer yang "terasa slide PPT" walau kameranya sudah
berkoreografi. Contoh polanya: explainer olahraga kecepatan tinggi (ilustrasi
flat, 16:9): semua fakta disampaikan TANPA menghentikan aksinya. Bisa 100 %
vektor SVG yang digambar prosedural di JS (tanpa gambar generate) — justru
itu yang memberi rasa motion graphic After Effects.

Prinsip (urutan penting):

1. **Satu pahlawan, dari detik 0 sampai akhir.** Subjek utama (atlet, kereta,
   motor, kurir) tidak pernah keluar frame. Yang berganti adalah DUNIA di
   sekitarnya, bukan subjeknya. Kalau ada 10 adegan, pahlawan hadir di 10-nya.
2. **Selalu bergerak.** Latar mengalir (parallax 2–3 lapis, looping), ada
   garis kecepatan, percikan/debu/asap partikel, subjek sendiri bergoyang
   halus. Tidak ada satu detik pun yang diam total — bahkan saat angka besar
   sedang dibaca.
3. **Angka adalah properti panggung, bukan overlay.** Angka besar berdiri di
   dalam dunia (di belakang subjek, dengan kedalaman parallax), lalu subjek
   MELINTAS DI DEPANNYA dan menyapu angka itu keluar. Angka yang berubah
   (35 → 43) berputar seperti odometer di tempat, bukan fade in/out.
4. **Sudut pandang berganti, subjek tetap di tengah.** Samping → depan
   (head-on) → miring mengikuti tikungan (seluruh dunia di-rotate 8–15°) →
   atas (top-down). Pergantian sudut = pergantian adegan; tidak perlu cut.
5. **Perubahan palet = perubahan tempo.** Saat cerita naik (kecepatan,
   bahaya), latar berganti warna dalam 0,3 dtk + blur gerak; subjek tetap.
   Kembali ke palet awal saat tempo turun.
6. **Perbandingan tetap di dalam dunia yang sama** (angka pembanding
   berdiri di latar, objek pembanding lewat di jalur lain), bukan layar
   dibelah jadi panel — membelah layar terasa "template" dan menghentikan
   dunia.
7. **Teks hanya dua tingkat: angka besar + label dunia.** Tanpa subtitle
   (lihat "Default yang sering salah dikira"); tidak ada kicker/body/badge.

Resep teknis (HTML + GSAP):

- Pahlawan = beberapa lapisan PNG (badan, kepala/helm, kendaraan, bayangan)
  dalam satu `#hero` supaya tiap bagian bisa punya goyangan sendiri
  (`yoyo` ±6–10 px dengan periode berbeda) + `#hero` di-nudge ±25 px.
- Latar = 2–3 strip lebar (`width:300%`) yang di-`x` looping
  (`repeat:-1`, `ease:'none'`); kecepatan lapisan belakang ½ dari depan.
  Ganti "tempat" dengan mengganti isi strip saat berada di luar frame.
- Angka dunia: elemen di lapisan `.deep` (skala .9, gerak ¾ kecepatan
  latar depan) sehingga subjek yang di depan menutupinya saat melintas.
  Odometer: dua `<span>` bertumpuk dalam `overflow:hidden`, tween `y`.
- Ganti sudut: siapkan 2–3 set gambar pahlawan (samping/depan/atas) yang
  digenerate satu batch dengan gaya sama; saat ganti, whip 0,25 dtk
  (blur gerak arah + geser 60 px) lalu set berikutnya sudah bergerak.
- Tikungan: `rotate` seluruh `#world` 8–15° selama 1,5 dtk, subjek ikut
  miring sedikit lebih banyak (lead 3–5°).
- Palet: semua warna lewat CSS variable; tween `--bg`, `--ink` dengan gsap
  (registerPlugin tidak perlu; tween objek lalu `style.setProperty`).
- Objek dunia diberi `t0` (masuk) dan `t1` (dibuang) supaya gunung/portal
  yang sudah "ditembus" tidak tetap tergambar di depan subjek.
- Menyembunyikan satu view dengan `visibility:hidden` TIDAK menyembunyikan
  anak SVG yang punya atribut `visibility="visible"` sendiri — atribut anak
  mengalahkan induk, objeknya "tembus" ke view lain (penanda peta muncul di
  atas kereta samping, dan tampak blur karena view lama masih ber-filter).
  Untuk menampilkan anak, HAPUS atributnya (`removeAttribute('visibility')`),
  jangan set 'visible'.
- Bangunan/peron yang "melayang": kanopi + tiang tipis saja tanpa dinding di
  belakang subjek dan lantai di depan roda. Beri dinding berjendela di lapisan
  belakang dan lantai peron di lapisan depan yang menutup bogie.
- Grup SVG yang diskalakan/diputar dari titik (0,0) lokalnya (kereta yang
  mendekat, subjek yang miring): tulis atribut `transform` langsung
  (`translate(x y) scale(s)`), jangan `gsap.set` — `transformOrigin` GSAP
  diukur dari kotak pembatas elemen dan `svgOrigin` dari koordinat global,
  sehingga objek melompat atau hilang saat kecil.
- Ukuran teks tetap mengikuti aturan "Keterbacaan di ponsel".

**Sudut pandang WAJIB berganti.** "Subjek dari samping + teks" dari awal
sampai akhir terasa statis dan monoton walau latar mengalir dan kamera
bergerak. Aturan: tidak ada tiga adegan berturut-turut dengan
sudut yang sama, dan tiap fakta baru idealnya dapat "instrumen" sendiri.
Katalog sudut yang sudah terbukti (semua vektor, semua dari rig yang sama):

| Fakta | Sudut / instrumen |
|---|---|
| pembuka & penutup | samping (jangkar visual — hanya di sini subjek boleh "hanya lewat") |
| kecepatan | kabin pengemudi: jarum speedometer menyapu + angka digital ikut, rel mengalir di kaca depan |
| rute / jarak / titik henti | simulasi peta: rute tergambar, penanda berjalan, titik pop, kamera zoom awal → seluruh rute |
| medan / terowongan / tanjakan | profil ketinggian (grafik kontur), rute memotong bukit, terowongan sebagai segmen berongga, yang terpanjang disorot lalu di-zoom |
| perbandingan waktu | balapan di peta: tiga penanda berangkat bersamaan di jalurnya masing-masing, satu jam tempuh berjalan, pemenang tiba saat yang lain baru ¼ jalan — bukan panel |
| jumlah / kapasitas | interior: lorong kabin perspektif, deretan kursi menyala berurutan, jendela dengan pemandangan mengalir |
| kedekatan / skala | tampak depan: subjek mendekat dari titik hilang sampai memenuhi frame |

Urutan yang enak: samping → kabin → peta → profil → balapan peta → depan →
interior → samping. Tiap view = satu `<div class="view">` berisi SVG
sendiri, diganti dengan whip (blur + geser 0,3 dtk); render tiap view tetap
fungsi murni dari waktu & jarak dunia yang sama, jadi sinkron VO tidak
terganggu saat view diganti.

Pemecah monotoni paling murah kalau hanya sempat satu: **simulasi peta
rute**. Peta vektor bergaya (garis pantai, sungai, waduk, ikon gunung, jalan
tol tipis, blob kota, kompas + skala), rute digambar dengan
`stroke-dasharray = panjang` dan `dashoffset` mengikuti progres; penanda
subjek bergerak lewat `getPointAtLength` dan diputar mengikuti tangen;
stasiun/titik "pop" (scale 0→1 dengan sedikit overshoot) saat progres
melewati fraksi panjangnya; kamera peta mulai zoom 2–2,5× di titik awal,
mengikuti penanda, lalu melonggar ke seluruh rute (`translate(pusat)
scale(z) translate(-cx -cy)` dihitung dari progres). Angka total (jarak,
waktu) muncul setelah zoom out. Tanpa ini, "subjek + teks" dari awal
sampai akhir tetap terasa statis walau latar mengalir.

Kamera samping juga harus "bernapas": rangkaian keyframe
`[t, zoom, cx, cy]` (dorong masuk 1,06–1,12× pada momen penting: angka
besar, portal terowongan, kedatangan) + osilasi ±0,6 % lambat, diterapkan
pada satu `<g>` pembungkus isi SVG — bukan pada teks HTML yang menempel di
kamera.

Jebakan: kalau pahlawan berganti gambar tiap adegan (pose baru, warna baru),
efek "satu subjek" hilang — jaga siluet, warna, dan posisi di frame. Dan
jangan hentikan latar untuk membaca teks; perlambat ke 40 % saja.
