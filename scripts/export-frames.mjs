/* =========================================================
   Render opener jadi urutan PNG, frame demi frame.

   Bukan rekaman layar: skrip ini MENYETEL waktu timeline, menunggu
   browser selesai menggambar, baru menangkap. Jadi tidak ada frame
   yang drop walau satu frame butuh 300 ms untuk dirender.

   Prasyarat:
     npm i puppeteer
     python -m http.server 5178      (di folder proyek, jendela lain)

   Pakai:
     node tools/export-frames.mjs
     ffmpeg -framerate 60 -i frames/f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 opener.mp4
   ========================================================= */

import puppeteer from 'puppeteer';
import { mkdir } from 'node:fs/promises';

const URL   = process.env.URL   || 'http://127.0.0.1:5178/index.html?clean=1';
const FPS   = Number(process.env.FPS   || 60);
const OUT   = process.env.OUT   || 'frames';
const SCALE = Number(process.env.SCALE || 1);   // 1 = 1920x1080, 0.5 = 960x540

await mkdir(OUT, { recursive: true });

const browser = await puppeteer.launch({
  headless: 'new',
  args: ['--enable-gpu', '--use-gl=angle', '--enable-webgl', '--ignore-gpu-blocklist'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: SCALE });
await page.goto(URL, { waitUntil: 'networkidle0' });

// tunggu sampai modul selesai dimuat dan timeline terpasang
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 120000 });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => { window.OPENER.tl.pause(0); });

const DURATION = await page.evaluate(() => window.OPENER.DURATION);
const total = Math.ceil(DURATION * FPS);
console.log(`${total} frame @ ${FPS} fps (${DURATION}s) -> ${OUT}/`);

for(let i = 0; i < total; i++){
  const t = i / FPS;

  // setel waktu, lalu biarkan DUA rAF lewat: satu untuk GSAP menulis gaya,
  // satu lagi untuk loop render menggambar frame dengan nilai baru itu.
  await page.evaluate(async (time) => {
    (window.OPENER.seek||window.OPENER.tl.time.bind(window.OPENER.tl))(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, t);

  await page.screenshot({
    path: `${OUT}/f${String(i).padStart(5, '0')}.png`,
    clip: { x: 0, y: 0, width: 1920, height: 1080 },
    optimizeForSpeed: true,
  });

  if(i % FPS === 0) process.stdout.write(`\r${i}/${total}  ${t.toFixed(1)}s`);
}

console.log(`\nselesai — ${total} frame di ${OUT}/`);
await browser.close();
