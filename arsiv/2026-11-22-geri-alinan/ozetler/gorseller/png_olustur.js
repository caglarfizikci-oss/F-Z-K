// Bu klasördeki tüm SVG görsellerini 2x çözünürlükte PNG'ye çevirir.
// Kullanım (depo kökünden): NODE_PATH=$(npm root -g) node ozetler/gorseller/png_olustur.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = __dirname;
  const svgs = fs.readdirSync(dir).filter(f => f.endsWith('.svg'));
  const browser = await chromium.launch();
  for (const f of svgs) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    const [, , , w, h] = svg.match(/viewBox="([\d.\s-]+)"/)[1].split(/\s+/).map(Number).reduce((a, n) => a.concat(n), [null]);
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await page.goto('file://' + path.join(dir, f));
    await page.screenshot({ path: path.join(dir, f.replace(/\.svg$/, '.png')) });
    await page.close();
    console.log(f, '→', f.replace(/\.svg$/, '.png'));
  }
  await browser.close();
})();
