import test from 'node:test';
import assert from 'node:assert/strict';
import {createAppServer} from '../server.mjs';

async function withServer(run) {
  const server = createAppServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  try { await run(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise((resolve, reject) => server.close(error => error ? reject(error) : resolve())); }
}
test('real HTTP endpoint returns the quote contract', async () => withServer(async base => {
  const response = await fetch(`${base}/api/quote`, {method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({postalCode:'00501', quantity:3})});
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), {postalCode:'00501', quantity:3, subtotalCents:7200, shippingCents:0, totalCents:7200});
}));
test('server rejects invalid quantities, not only the browser', async () => withServer(async base => {
  const response = await fetch(`${base}/api/quote`, {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify({postalCode:'10001', quantity:0})});
  assert.equal(response.status, 400);
  assert.match((await response.json()).error, /quantity/i);
}));
test('malformed request and unsupported methods fail explicitly', async () => withServer(async base => {
  const bad = await fetch(`${base}/api/quote`, {method:'POST', body:'not-json'});
  assert.equal(bad.status, 400);
  const method = await fetch(`${base}/api/quote`);
  assert.equal(method.status, 405);
}));
