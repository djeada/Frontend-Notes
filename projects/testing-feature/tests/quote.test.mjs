import test from 'node:test';
import assert from 'node:assert/strict';
import {calculateQuote} from '../quote.mjs';

test('one notebook costs $24 plus $6 shipping', () => {
  assert.deepEqual(calculateQuote({postalCode: '10001', quantity: 1}), {
    postalCode: '10001', quantity: 1, subtotalCents: 2400, shippingCents: 600, totalCents: 3000,
  });
});
test('three notebooks cross the free-shipping threshold', () => {
  assert.equal(calculateQuote({postalCode: '10001', quantity: 3}).totalCents, 7200);
  assert.equal(calculateQuote({postalCode: '10001', quantity: 3}).shippingCents, 0);
});
test('quantities are bounded whole numbers', () => {
  for (const quantity of [0, -1, 1.5, 11, NaN, '3']) {
    assert.throws(() => calculateQuote({postalCode: '10001', quantity}), RangeError);
  }
});
test('ZIP validation rejects malformed input without removing leading zeroes', () => {
  for (const postalCode of ['', '1234', '123456', 'A0001', 10001]) {
    assert.throws(() => calculateQuote({postalCode, quantity: 1}), RangeError);
  }
  assert.equal(calculateQuote({postalCode: '00501', quantity: 1}).postalCode, '00501');
});
