// Render semua SVG di <folder> ke PNG transparan dengan ukuran asli SVG (sudah 2×).
// pakai: node render-svg.cjs <folder>
const puppeteer = require('puppeteer');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.svg'));
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  for (const f of files) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    const w = +svg.match(/width="(\d+)"/)[1], h = +svg.match(/height="(\d+)"/)[1];
    await page.setViewport({ width: w, height: h, deviceScaleFactor: 1 });
    await page.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
    await page.screenshot({ path: path.join(dir, f.replace('.svg', '.png')), omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
  }
  await browser.close();
  console.log('dirender', files.length, 'PNG');
})().catch(e => { console.error(e); process.exit(1); });
