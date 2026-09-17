// Prices are integer cents. This is a teaching fixture, not real shipping or tax logic.
export function calculateQuote({postalCode, quantity}) {
  if (typeof postalCode !== 'string' || !/^\d{5}$/.test(postalCode)) {
    throw new RangeError('Enter a five-digit US ZIP code.');
  }
  if (!Number.isSafeInteger(quantity) || quantity < 1 || quantity > 10) {
    throw new RangeError('Quantity must be a whole number from 1 to 10.');
  }
  const subtotalCents = 2400 * quantity;
  const shippingCents = subtotalCents >= 5000 ? 0 : 600;
  return {postalCode, quantity, subtotalCents, shippingCents, totalCents: subtotalCents + shippingCents};
}
