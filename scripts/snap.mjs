/* =========================================================
   VERIFIKASI VISUAL: potret beberapa detik kunci, bukan render penuh.

   AI tidak bisa menonton video — ia hanya bisa MELIHAT frame. Skrip ini
   membekukan timeline di detik yang diminta (OPENER.seek), menunggu browser
   selesai menggambar, lalu memotret. 6–20 frame sudah cukup untuk menilai
   satu explainer; JANGAN merender semua frame hanya untuk mengecek
   (60 dtk × 60 fps = 3.600 gambar — itu kerja export-frames.mjs, dan hanya
   bila user minta MP4).

   Prasyarat (opsional — tanpa Node, verifikasi manual lewat ?debug=1):
     npm i puppeteer            (sekali, di folder mana pun; jalankan dari sana)

   Pakai (dari folder proyek, tanpa server; berkas dibuka lewat file://):
     node <path>/snap.mjs shots 1 3.5 8 12 20
     URL="file:///C:/proyek/index.html?clean=1" node <path>/snap.mjs shots 1 3.5 8
   Hasil: shots/t1_00.png, shots/t3_50.png, ... — gabungkan jadi lembar
   kontak (PIL/ffmpeg tile) dan NILAI dengan mata: teks kepotong? tumpang
   tindih? teks muncul sebelum kamera selesai? masih terasa slide?

   Halaman harus mengekspos window.OPENER = { W, H, ready, seek(t) } — semua
   starter di skill ini sudah begitu. ?clean=1 menahan autoplay & panel.
   ========================================================= */
import puppeteer from 'puppeteer';
import { pathToFileURL } from 'node:url';
import { mkdir } from 'node:fs/promises';

const [outDir, ...times] = process.argv.slice(2);
if (!outDir || !times.length) { console.log('pakai: node snap.mjs <folder-output> <detik> [<detik> ...]'); process.exit(1); }
const URL = process.env.URL || pathToFileURL(process.cwd()).href + '/index.html?clean=1';
await mkdir(outDir, { recursive: true });
const browser = await puppeteer.launch({ headless: 'new', args: ['--enable-gpu', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'] });
const page = await browser.newPage();
page.on('pageerror', e => console.log('PAGEERROR', e.message));
await page.goto(URL, { waitUntil: 'networkidle0' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 60000 });
const { W, H } = await page.evaluate(() => ({ W: window.OPENER.W || 1920, H: window.OPENER.H || 1080 }));
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
for (const ts of times) {
  const t = Number(ts);
  await page.evaluate(async (time) => {
    window.OPENER.seek(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    window.OPENER.seek(time);   // dua kali: GSAP menulis style, lalu render loop menggambar
  }, t);
  await page.screenshot({ path: `${outDir}/t${t.toFixed(2).replace('.', '_')}.png`, clip: { x: 0, y: 0, width: W, height: H } });
  process.stdout.write(`${t} `);
}
await browser.close(); console.log('\nselesai');
