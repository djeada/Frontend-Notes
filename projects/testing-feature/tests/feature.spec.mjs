import {test, expect} from '@playwright/test';

// Each test gets a fresh browser context and a real local app server.
test.beforeEach(async ({page}) => { await page.goto('/'); });

test('visitor can request a real HTTP quote and see the total', async ({page}) => {
  await page.getByLabel('US ZIP code').fill('10001');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.getByRole('heading', {name: 'Your quote'})).toBeVisible();
  await expect(page.locator('#subtotal')).toHaveText('$24.00');
  await expect(page.locator('#shipping')).toHaveText('$6.00');
  await expect(page.locator('#total')).toHaveText('$30.00');
  await expect(page.getByRole('status')).toHaveText('Quote ready.');
});

test('free shipping threshold remains correct after a quantity change', async ({page}) => {
  await page.getByLabel('Notebook quantity').selectOption('3');
  await page.getByLabel('US ZIP code').fill('00501');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#shipping')).toHaveText('FREE');
  await expect(page.locator('#total')).toHaveText('$72.00');
});

test('invalid ZIP gives an accessible error and never claims success', async ({page}) => {
  await page.getByLabel('US ZIP code').fill('oops');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#postal')).toHaveAttribute('aria-invalid', 'true');
  await expect(page.locator('#postal-error')).toBeVisible();
  await expect(page.locator('#quote-result')).toBeHidden();
});

test('503 response shows retry feedback without fabricated totals', async ({page}) => {
  await page.route('**/api/quote', route => route.fulfill({status:503, contentType:'application/json', body:JSON.stringify({error:'Unavailable'})}));
  await page.getByLabel('US ZIP code').fill('10001');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#request-error')).toBeVisible();
  await expect(page.locator('#quote-result')).toBeHidden();
  await expect(page.getByRole('button', {name: /Get shipping quote/})).toBeEnabled();
});

test('narrow viewport keeps the form and price visible', async ({page}) => {
  await page.setViewportSize({width:375, height:812});
  await page.getByLabel('Notebook quantity').selectOption('3');
  await page.getByLabel('US ZIP code').fill('10001');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#total')).toHaveText('$72.00');
  const overflows = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  expect(overflows).toBe(false);
});

test('capture real documented UI states', async ({page}) => {
  test.skip(process.env.CAPTURE_DOC_SHOTS !== '1', 'Screenshot export is opt-in.');
  const root = new URL('../../../assets/testing-feature/', import.meta.url);
  // Resolve screenshot output relative to the repository root (no generated image is misrepresented as a baseline).
  const {mkdir} = await import('node:fs/promises');
  const {fileURLToPath} = await import('node:url');
  const dir = fileURLToPath(root);
  await mkdir(dir, {recursive:true});
  await page.setViewportSize({width:1280, height:900});
  await page.screenshot({path: dir + 'shipping-before.png', fullPage:true});
  await page.getByLabel('Notebook quantity').selectOption('3');
  await page.getByLabel('US ZIP code').fill('10001');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#total')).toHaveText('$72.00');
  await page.screenshot({path: dir + 'shipping-success.png', fullPage:true});
  await page.route('**/api/quote', route => route.fulfill({status:503, body:'{}'}));
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#request-error')).toBeVisible();
  await page.screenshot({path: dir + 'shipping-error.png', fullPage:true});
});
