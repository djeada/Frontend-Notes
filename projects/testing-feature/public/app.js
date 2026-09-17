const form = document.querySelector('#quote-form');
const postal = document.querySelector('#postal');
const quantity = document.querySelector('#quantity');
const postalError = document.querySelector('#postal-error');
const requestError = document.querySelector('#request-error');
const status = document.querySelector('#request-status');
const result = document.querySelector('#quote-result');
const button = document.querySelector('#submit-quote');
const money = cents => new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'}).format(cents / 100);
function clearFeedback() {
  postalError.hidden = true;
  postal.removeAttribute('aria-invalid');
  requestError.hidden = true;
  result.hidden = true;
  status.textContent = '';
}
form.addEventListener('submit', async event => {
  event.preventDefault();
  clearFeedback();
  const value = postal.value.trim();
  if (!/^\d{5}$/.test(value)) {
    postal.setAttribute('aria-invalid', 'true');
    postalError.hidden = false;
    postal.focus();
    return;
  }
  const qty = Number(quantity.value);
  if (!Number.isSafeInteger(qty) || qty < 1 || qty > 10) {
    requestError.textContent = 'Choose a quantity from 1 to 10.';
    requestError.hidden = false;
    return;
  }
  button.disabled = true;
  status.textContent = 'Checking the shipping estimate…';
  try {
    const response = await fetch('/api/quote', {
      method: 'POST', headers: {'content-type': 'application/json'},
      body: JSON.stringify({postalCode: value, quantity: qty}),
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const quote = await response.json();
    if (![quote.subtotalCents, quote.shippingCents, quote.totalCents].every(Number.isSafeInteger)) throw new Error('Invalid quote');
    document.querySelector('#subtotal').textContent = money(quote.subtotalCents);
    document.querySelector('#shipping').textContent = quote.shippingCents === 0 ? 'FREE' : money(quote.shippingCents);
    document.querySelector('#total').textContent = money(quote.totalCents);
    result.hidden = false;
    status.textContent = 'Quote ready.';
  } catch {
    result.hidden = true;
    requestError.textContent = 'Could not get a quote. Try again.';
    requestError.hidden = false;
    status.textContent = '';
  } finally {
    button.disabled = false;
  }
});
