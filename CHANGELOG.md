# Changelog

## 1.17.0 — 2026-09-14

Ringkasan isi paket.

**Opener dan promo**
- Kerangka dipilih, bukan diwarisi: tiga kandidat konsep dari menu 19 konsep, sidik jari
  struktur yang dibandingkan dengan proyek sebelumnya, komponen kanonik paling banyak dua,
  dan starter opener tanpa urutan adegan contoh (`references/opener-konsep.md`,
  `assets/starter-opener.html`).
- Contoh urutan tiap konsep adalah prinsip, bukan naskah: pembuka/penutup dan momen khas
  tidak disalin; palet, bentuk, dan properti diturunkan dari brand, tiap warna menyebut
  sumbernya.
- Panduan animasi UI untuk app/SaaS, kamera yang mengikuti klik penting, dan foto dalam
  opener (foto user, generate lewat MCP, atau stok berlisensi).

**Tipografi, latar, render**
- Sorotan kata opsional; judul dan klaim tanpa titik otomatis.
- Latar tidak pernah statis; warna latar boleh berganti kapan dibutuhkan dengan pemicu
  terlihat. Grainy gradient dengan jaga-jaga encode. Menu gaya render objek.

**Explainer**
- Enam gaya: aksi kontinu, kartun kolase, jurnalisme visual, katalog putih, sketsa vintage,
  dan kartun panggung (`references/explainer.md`, `references/kartun-panggung.md`).

**After Effects**
- Dibangun langsung lewat bridge/MCP Higgsfield (`references/ae-bridge-higgsfield.md`,
  `scripts/ae/bridge/`).

**Alat kerja**
- Verifikasi visual per detik kunci (`scripts/snap.mjs`), ekspor MP4
  (`scripts/export-frames.mjs`), pemotong jeda VO (`scripts/vo-pauses.html`).
