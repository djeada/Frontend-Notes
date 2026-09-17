# Shipping quote: a feature you can keep working

This is a **fictional US-only shipping estimate**, not a shop, payment system, or real carrier quote. It deliberately includes a real local HTTP endpoint, business logic, user-visible form states, and three testing boundaries. It does not persist or transmit ZIP codes to any external service.

## Run

Requires Node.js 20+ and npm. From this directory:

```sh
npm ci
npx playwright install chromium
npm run test:unit
npm run test:e2e
npm start
```

Open `http://127.0.0.1:4173`. `npm run test:unit` runs dependency-free Node tests; browser tests need the Playwright package and its Chromium binary installed. `npm test` runs both. On CI, browsers may also require `npx playwright install --with-deps chromium`.

## Feature contract

A notebook costs $24.00 each. Quantity is a whole number 1–10; a US ZIP code must be exactly five digits (leading zeroes are preserved). Shipping costs $6.00 for subtotals below $50.00 and $0.00 otherwise. The form performs a **real request** to this repository's local `POST /api/quote` handler. Server-side validation repeats the checks. The app shows a working state, totals only after a successful response, and a recoverable error if the request fails. No taxes, real carriers, inventory, checkout, or payments are modeled.

| Requirement | Cheap proof | Boundary proof | Browser proof |
|---|---|---|---|
| $24 + $6 = $30 | `tests/quote.test.mjs` | `tests/api.test.mjs` | `tests/feature.spec.mjs` |
| Three notebooks ship free | Unit threshold test | HTTP response | Select 3 and see FREE / $72 |
| Reject quantity zero | Unit rejects | Server returns 400 | Quantity select cannot offer 0; API still validates direct requests |
| Invalid ZIP never succeeds | Unit rejects | HTTP returns 400 if sent | Error text, `aria-invalid`, no result |
| Server is unavailable | Not a unit rule | Request mocked at browser boundary | 503 gives retry text, no quote |
| Narrow layout | Not a unit rule | Not an API rule | 375px viewport, assert no horizontal overflow |

## Deliberately break it to understand a regression

Change `subtotalCents >= 5000` in `quote.mjs` to `subtotalCents > 7500`. The unit test for quantity 3 fails, the real HTTP test fails, and the browser free-shipping workflow fails: one defect is caught at three different boundaries. **Revert the change afterward.** The test suite does not prove that real postal addresses exist or that a payment was processed.

## Screenshots and evidence

The linked images in `notes/10_testing.md` are generated from Chromium in an explicit fixed desktop viewport. They depict default, success and controlled HTTP-error states—not arbitrary mockups or an approved visual baseline. Set `CAPTURE_DOC_SHOTS=1` only when intentionally regenerating them in the documented browser environment. Review image diffs manually; behavior and accessibility assertions remain separate.

Sources and workflow choices: [Node test runner](https://nodejs.org/api/test.html), [Playwright best practices](https://playwright.dev/docs/best-practices), [visual comparisons](https://playwright.dev/docs/test-snapshots).
