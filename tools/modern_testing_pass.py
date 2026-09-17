"""One-time in-place edit to the original testing chapter. Removed by workflow."""
from pathlib import Path

p = Path('notes/10_testing.md')
old = p.read_text(encoding='utf-8')
anchor = '### What is testing?\n'
assert old.count(anchor) == 1
assert '## Worked example: keep a shipping quote working' not in old
lesson = r'''## Worked example: keep a shipping quote working

*2026-maintained teaching example: one actual application, multiple boundaries, and screenshots from a running browser.* The earlier pricing, form and account snippets remain below as independent illustrations. This section connects the whole story to code you can clone, run, deliberately break, and repair: [`projects/testing-feature/`](../projects/testing-feature/README.md). It implements a small US-only shipping estimator with a real local HTTP server—not a mock screenshot, a real shop, or a production carrier integration.

### Start with a user promise, not a test framework

Imagine you built a product page and someone changes the pricing code next week. Your promise to the visitor is: **"Give me an accurate, understandable shipping quote before I buy anything."** Define what must survive refactors *before* deciding which tool to install:

| Contract | What could regress? | Smallest useful check |
|---|---|---|
| One $24 notebook plus $6 shipping totals $30 | A developer changes the arithmetic | Pure function unit test |
| Three notebooks cross the $50 free-shipping threshold; total $72 | A threshold changes from `>=` to `>` or $50 to $75 | Boundary unit test plus a browser journey |
| Quantity must be a whole number from 1 to 10 | Someone bypasses HTML controls and POSTs zero | Real HTTP API test; server validates again |
| ZIP must be exactly five digits, retaining leading zeroes | A developer converts `00501` to a number | Unit and API tests; browser error state |
| A failed HTTP response must **not** show a successful quote | The interface treats every `fetch` resolution as success | Controlled 503 browser test |
| Users can read the form at 375px and understand errors | CSS clips controls or errors become color-only | Browser viewport and semantic assertions; manual assistive-tech check |

The test's *oracle* is the observable contract, not implementation trivia such as a private variable or the exact number of React components. In a real product, confirm shipping, tax, supported regions, and pricing rules with the business owner; the values above are explicit **fictional fixtures**, not actual carrier rates.

### See the application, its result, and its failure

These are **actual Chromium screenshots exported by the repository's Playwright test**, at a documented desktop viewport. They are teaching evidence of the captured states, not automatically approved pixel baselines or accessibility certification.

**Before interaction:** quantity, ZIP field, a useful label, and the action. The result is hidden rather than displaying fabricated totals.

![Real Chromium screenshot of the shipping estimator before submitting](../assets/testing-feature/shipping-before.png)

**After a successful request:** select three notebooks, enter `10001`, submit, and see the real local server response with **FREE shipping and $72.00 total**.

![Real Chromium screenshot showing the completed quote with free shipping](../assets/testing-feature/shipping-success.png)

**When the server fails:** the test deliberately returns HTTP 503. The previous total disappears and the visitor gets an explicit, retryable message—not a green success toast.

![Real Chromium screenshot of a controlled server error with no successful quote](../assets/testing-feature/shipping-error.png)

Run the app yourself and inspect all three states. Images prove only the rendered pixels at capture time; the test assertions separately check total text, `aria-invalid`, no false result, button recovery, and mobile overflow. See the executable [feature contract and commands](../projects/testing-feature/README.md).

### Stage 1 — unit tests protect business rules

The real [`quote.mjs`](../projects/testing-feature/quote.mjs) computes integer cents and validates postal-code strings. These are selected lines from the runnable [`quote.test.mjs`](../projects/testing-feature/tests/quote.test.mjs):

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import {calculateQuote} from '../quote.mjs';

test('three notebooks cross the free-shipping threshold', () => {
  assert.equal(calculateQuote({postalCode: '10001', quantity: 3}).totalCents, 7200);
  assert.equal(calculateQuote({postalCode: '10001', quantity: 3}).shippingCents, 0);
});
```

`cd projects/testing-feature && npm run test:unit` runs Node's built-in test runner. Other tests cover one notebook, invalid/decimal quantities, and leading-zero ZIP codes. A successful unit suite still cannot prove that the server sends the right JSON or that the page displays it. **No need to install Jest or Vitest for this dependency-free Node fixture.** In a project already using Vite, Vitest may fit the existing tooling; match the runner to your project rather than migrating just because a package is fashionable. [Node test-runner documentation](https://nodejs.org/api/test.html).

### Stage 2 — API integration tests protect the boundary

[`api.test.mjs`](../projects/testing-feature/tests/api.test.mjs) starts the **actual local HTTP server on an ephemeral port**, sends `POST /api/quote`, asserts status and exact JSON, and closes the server even if the check fails. This catches a broken route, incorrect JSON shape, or a server that trusts client-only validation. For example, a direct request with quantity `0` must return HTTP 400 even though the HTML select does not offer it.

```js
const response = await fetch(`${base}/api/quote`, {
  method: 'POST',
  headers: {'content-type': 'application/json'},
  body: JSON.stringify({postalCode: '00501', quantity: 3}),
});
assert.equal(response.status, 200);
const quote = await response.json();
assert.equal(quote.shippingCents, 0);
assert.equal(quote.totalCents, 7200);
```

Here `base`, `assert`, and the server fixture are provided by the complete linked test; this excerpt is intentionally not a standalone file. The HTTP test exercises our own server, not a real carrier API. In a larger application also test authentication, authorization, database persistence, and the specific contracts your feature actually uses.

### Stage 3 — a browser test protects the person's task

The checked-in [`feature.spec.mjs`](../projects/testing-feature/tests/feature.spec.mjs) opens the working app through Playwright, locates controls by accessible labels and roles, submits the quote, and checks **what a visitor sees**:

```js
import {test, expect} from '@playwright/test';

test('free shipping survives a quantity change', async ({page}) => {
  await page.goto('/');
  await page.getByLabel('Notebook quantity').selectOption('3');
  await page.getByLabel('US ZIP code').fill('00501');
  await page.getByRole('button', {name: /Get shipping quote/}).click();
  await expect(page.locator('#shipping')).toHaveText('FREE');
  await expect(page.locator('#total')).toHaveText('$72.00');
});
```

The browser tests also check that bad ZIP input exposes text and `aria-invalid`, an intercepted HTTP 503 never invents totals, the button re-enables after failure, and the 375px view has no horizontal overflow. CSS/layout-based IDs above identify the *output* amounts; prefer roles and labels for interaction. Do not test an implementation detail such as a hook's private state. For independent browser tests Playwright uses fresh contexts, while the server and its deterministic fixture remain under our control. [Playwright best practices](https://playwright.dev/docs/best-practices).

### Stage 4 — demonstrate the regression rather than asserting tests exist

In [`quote.mjs`](../projects/testing-feature/quote.mjs), change `subtotalCents >= 5000` to `subtotalCents > 7500`. Run `npm run test:unit` and observe the failure for three notebooks. Then run `npm run test:e2e`: the same bug crosses the HTTP boundary and changes the displayed FREE shipping and $72 total. Revert the line and rerun both. This is a **deliberate mutation exercise**: the committed code is the passing implementation. Do not commit the broken mutation or change the expectations merely to turn the suite green.

A useful failure message identifies a **broken promise**: `three notebooks should ship free`, not merely `component snapshot changed`. A failing E2E test cannot by itself identify whether the defect is pricing, HTTP, DOM, or styling; unit and API tests narrow the cause. A passing browser screenshot can likewise miss incorrect cents if no text assertion exists.

### Stage 5 — run the same checks on every change

From `projects/testing-feature/`, on Node 20+:

```sh
npm ci
npx playwright install chromium
npm run test:unit
npm run test:e2e
npm test
```

`npm ci` requires the checked-in lockfile generated for this example. On a minimal Linux machine, Playwright may also require `npx playwright install --with-deps chromium`. The [repository's feature-specific GitHub Actions workflow](../.github/workflows/testing-feature.yml) runs the suite for relevant pull requests and on changes to `main`; it uses a real local app, not production. When a check fails, inspect the assertion, browser trace, network response and screenshot artifact; fix the cause and re-run. Keep test accounts and fixture data isolated in applications that actually have them. Avoid arbitrary sleeps and indiscriminate retries. [Playwright CI guide](https://playwright.dev/docs/ci-intro).

**Screenshot discipline:** snapshots detect unexpected appearance changes at a fixed browser/version/viewport; review baseline changes rather than automatically approving them. They do not replace assertions about prices, names, keyboard order, error text or screen-reader announcements. These three documentation PNGs are example captures, not `toHaveScreenshot()` golden files. For a real visual-regression suite use reviewed baseline images in a reproducible environment; see [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).

### Which tools are current, and who demonstrably uses or documents them?

There is no trustworthy universal winner or single tool for every kind of check. The following links are **verifiable published examples as of September 2026**, not unverified claims about a company's private test stack or market share:

| Approach | Published user/example | Where it fits | Watch out for |
|---|---|---|---|
| Node `node:test` + `node:assert` | [Node's own test-runner documentation](https://nodejs.org/api/test.html); used by the complete example here | Small library and server tests with few dependencies | It cannot drive a real browser by itself. |
| Vitest + DOM emulation | [Angular CLI uses Vitest by default for **new** projects](https://angular.dev/guide/testing); [Next.js documents Vitest](https://nextjs.org/docs/app/guides/testing) | Logic and component tests in compatible projects | A simulated DOM differs from actual browser layout and accessibility. |
| React Testing Library | [React Testing Library's published examples](https://testing-library.com/docs/react-testing-library/example-intro/) | Test React components via visible/accessible behavior | It is a querying/rendering library, **not** a test runner; combine with Jest/Vitest as configured. |
| Playwright Test | [Next.js's official E2E guide](https://nextjs.org/docs/app/guides/testing/playwright); [Microsoft Playwright's own repository test scripts](https://github.com/microsoft/playwright/blob/main/package.json) | Browser journeys, HTTP routing, screenshots, traces | Keep browsers, state and data reproducible; only cover critical journeys at this cost. |
| Cypress | [Cypress Real World App](https://docs.cypress.io/), maintained by the tool authors; [Next.js Cypress guide](https://nextjs.org/docs/app/guides/testing) | Component/browser journeys and API checks with Cypress | Check installed-version browser support and whether plugins are required. |
| Mock Service Worker | [Testing Library's example using MSW](https://testing-library.com/docs/react-testing-library/example-intro/) | Simulate external API responses at the request layer | A stub does not prove the real service works; add an appropriate integration/contract check. |
| Karma (legacy) | [Karma maintainers' explicit deprecation notice](https://github.com/karma-runner/karma); [Angular migration documentation](https://angular.dev/guide/testing/migrating-to-vitest) | Understanding existing projects being maintained | Not a sensible unqualified default for a new suite: it is deprecated. |

**Choosing for a project you already built:** identify its framework, existing runner, deployment boundary, and most expensive user-facing failure. Start with one deterministic business-rule test and one browser journey for the critical task. Add real API tests where contracts matter, controlled failure tests where recovery matters, and exploratory accessibility/device testing alongside automation. Tool brand adoption is not proof of suitability.

### Before release: a small, honest testing checklist

- [ ] Requirements and edge cases were written in observable language (including threshold boundaries and invalid input).
- [ ] Unit, integration and browser checks cover their **own** boundaries; fixtures have predictable setup and teardown.
- [ ] A deliberate regression fails at least one test, then passes after the code is restored.
- [ ] A simulated failed request never displays false success; the person can retry.
- [ ] The form can be used with keyboard and at narrow/zoomed widths; screen-reader experience is checked manually where relevant.
- [ ] The PR's automated checks pass in CI, with failures and visual changes reviewed rather than rubber-stamped.
- [ ] The team knows what is **not** covered (real carrier pricing, tax, payment, performance, security or a full accessibility audit in this teaching app).

---

'''
new = old.replace(anchor, lesson + anchor, 1)
karma = '| **Karma** | Test runner that launches browsers | Runs tests with another framework; it is not an assertion library by itself. |'
assert new.count(karma) == 1
new = new.replace(karma, '| **Karma (deprecated)** | Legacy browser test runner | Maintainers deprecated it; existing projects can migrate deliberately. For new Angular CLI projects the default unit runner is Vitest. |')
assert len(new) > len(old) and new.count('## Worked example: keep a shipping quote working') == 1
p.write_text(new, encoding='utf-8')
print(f'Original testing chapter expanded: {len(old.splitlines())} -> {len(new.splitlines())} lines')
