// Local demonstration only. Do not use browser validation as a substitute for server validation.
const form = document.querySelector('#newsletter');
const email = document.querySelector('#live-email');
const feedback = document.querySelector('#email-feedback');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Do not send personal data from this teaching example.
  const value = email.value.trim();
  const valid = value !== '' && email.checkValidity();
  email.setAttribute('aria-invalid', String(!valid));
  feedback.className = valid ? 'feedback success' : 'feedback error';
  feedback.textContent = valid
    ? 'Looks valid in this browser. A server must still validate it.'
    : 'Enter an email such as name@example.com.';
  if (!valid) email.focus();
});

email.addEventListener('input', () => {
  email.removeAttribute('aria-invalid');
  feedback.className = 'feedback';
  feedback.textContent = 'Press Subscribe to check this address.';
});
