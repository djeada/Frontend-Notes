# Frontend testing: test behavior at the right boundary

[Original testing chapter](../10_testing.md) · [All chapter updates](README.md)

Tests provide evidence about behavior under specified conditions. They cannot *ensure* the absence of security, performance, or usability bugs; they reduce risk and help developers notice regressions.

## Corrections to the original

- Unit, integration, system, and end-to-end describe **scope and boundaries**, not a rigid hierarchy of specific tools. E2E tests can exercise a system, but calling them synonyms hides the difference between a complete-system check and a browser-driven user journey.
- Karma is a **test runner**, while Puppeteer is a **browser automation library**; they should not be compared as interchangeable unit-test frameworks. A test assertion library, runner, browser driver, and coverage tool play different roles.
- Jest is not literally zero configuration for every modern JavaScript project. The setup depends on module format, transforms, DOM test environment, and tooling.
- The sample Cypress workflow against `https://example.com` is **illustrative pseudocode**, not a runnable test of that site. Use a locally controlled application and stable selectors for a real example.
- A passing test on one browser or viewport does not guarantee accessibility. Test keyboard use, labels, and relevant assistive technology in addition to assertions and automated checks.

## Test the same feature at three boundaries

Imagine a form that calculates shipping from subtotal and country:

1. **Unit:** pure `shippingCost(subtotal, country)` returns the expected result for ordinary and boundary inputs.
2. **Integration:** entering a subtotal and choosing a country updates the UI, with validation and accessible messages. Stub only the network boundaries necessary to make the test deterministic.
3. **End-to-end:** a browser visits the deployed test app, completes the checkout flow, and observes the confirmation. Control test accounts and data; avoid shared production state.

Example using the built-in Node.js test runner for a pure function:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import { shippingCost } from './shipping.js';

test('free domestic shipping starts at the threshold', () => {
  assert.equal(shippingCost(50, 'domestic'), 0);
});

test('shipping is charged below the threshold', () => {
  assert.equal(shippingCost(49, 'domestic'), 5);
});
```

The example assumes `shipping.js` implements a **documented policy** of free domestic shipping at 50 and a charge of 5 below that level; it is not a universal pricing rule. Test negative inputs and unknown countries according to the actual specification.

## Reliable test checklist

Define an observable expected outcome. Prefer role/label-based selectors when they reflect what users see; use `data-testid` selectively. Wait for events or conditions instead of arbitrary sleeps. Isolate fixtures, clean up data, and reproduce failing seeds. Run fast checks on each change and reserve slower cross-browser flows for key journeys. Treat coverage as a diagnostic, not a quality score.

**References:** [Node.js test runner](https://nodejs.org/api/test.html), [Testing Library: guiding principles](https://testing-library.com/docs/guiding-principles/), [Playwright: best practices](https://playwright.dev/docs/best-practices), [W3C: accessibility evaluation](https://www.w3.org/WAI/test-evaluate/).
