// Local demonstration only. Do not use browser validation as a substitute for server validation.

// Use separate documents so each semantic example has a valid, page-level <main>.
// The wireframes in index.html are replaced by real, isolated documents on load.
document.querySelectorAll('#semantic .wireframe').forEach((target, index) => {
  const preview = document.createElement('iframe');
  preview.src = index === 0 ? 'semantic-before.html' : 'semantic-after.html';
  preview.title = index === 0 ? 'Generic container document' : 'Semantic landmark document';
  preview.width = '100%';
  preview.height = '180';
  preview.style.width = '100%';
  preview.style.border = '0';
  target.replaceChildren(preview);
});

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
