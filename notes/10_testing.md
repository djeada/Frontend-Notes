## Frontend Testing

Testing reduces uncertainty about whether an application behaves as intended. A passing test suite cannot *guarantee* security, performance, or freedom from defects: its value depends on the scenarios, environments, and assertions it covers. Combine automated checks with exploratory, accessibility, and real-device testing.

### What is testing?

A test starts with an observable requirement, performs an action or supplies input, and compares the actual outcome with the expected outcome. For example, the requirement “an invalid email is explained in text” yields a stronger test than “the form renders.” Define a failure condition before writing the assertion.

### Levels of testing

**Unit tests** check a small, well-defined unit such as a conversion function. They should run quickly and make failures easy to diagnose. Isolation can be useful, but an excessive number of mocked dependencies may hide broken integration.

**Integration tests** exercise boundaries between modules or systems—for instance, a form component, its validation logic, and the HTTP client together. A test may use a real database or a controlled fake depending on the boundary being studied.

**System tests** assess an assembled application with its relevant environment. **End-to-end (E2E) tests** are a common workflow-oriented type: they drive a browser through a complete user journey, including several components and often a backend. These categories overlap, but are not universally identical. Label a test by what it actually exercises rather than by the tool used to run it.

The testing pyramid is a useful heuristic, not a mandatory count: make cheap, deterministic checks common and reserve slower browser tests for important user journeys. Accessibility, visual regression, security, and performance tests measure *different properties* and can exist at several levels.

#### Unit testing in depth

Benefits:

- Fast feedback identifies regressions while you are developing.
- Tests can preserve intended behavior during refactoring.
- Writing small, testable functions can make responsibilities clearer.

**Choose tools by their roles.** A test *runner* discovers and executes tests; an *assertion library* describes expectations; a *browser automation tool* interacts with a browser. Some products combine several roles.

| Tool | What it primarily provides | Typical use or limitation |
| --- | --- | --- |
| **Mocha** | JavaScript test framework/runner; assertions can come from another library | Flexible unit or integration suites; configure assertions and mocking separately. |
| **Jest** | Runner, assertions, mocking and snapshots | Unit and integration testing; browser DOM behavior typically requires a configured environment. |
| **Jasmine** | Testing framework and assertions | Behavior-focused JavaScript tests. |
| **Karma** | Test runner that launches browsers | Runs tests with another framework; it is not an assertion library by itself. |
| **Puppeteer** | Browser automation using the Chrome DevTools Protocol | Browser workflows, screenshots and inspection; assertions and runner depend on setup. |
| **Nightwatch** | Browser-based E2E test framework | Browser interaction using its supported automation backends. |
| **Cypress** | Browser-oriented test runner and automation | Component and E2E tests; check the current browser/platform support for your installed version. |
| **Playwright** | Browser automation and an optional test runner | Cross-browser workflow tests and screenshots; configure browser dependencies in CI. |

Versions, maintainers, configuration, and dependencies change; consult each tool's current documentation before choosing one. Avoid interpreting “supports UI testing” as proof that a tool checks accessible names or keyboard order automatically.

**Example: testing a Roman-numeral function with Jest**

First implement or install a module exporting `romanNumberConverter`; this snippet is a *test of that module*, not a complete working project:

```javascript
const romanNumberConverter = require('./romanNumberConverter');

test('converts I to 1', () => {
  expect(romanNumberConverter('I')).toBe(1);
});

test('converts IV to 4', () => {
  expect(romanNumberConverter('IV')).toBe(4);
});

test('converts XL to 40', () => {
  expect(romanNumberConverter('XL')).toBe(40);
});

test('converts MCMXCIV to 1994', () => {
  expect(romanNumberConverter('MCMXCIV')).toBe(1994);
});
```

Explain *why* subtractive pairs work (`IV = 5 - 1`, `XL = 50 - 10`), then test negative cases: empty input, invalid symbols, and malformed subtractive notation. Decide whether invalid input throws or returns a sentinel and assert that contract. A test suite with only successful inputs cannot establish validation behavior.

#### End-to-end (E2E) testing

An E2E test verifies a user-visible path such as registration → login → profile update → deletion. It can reveal broken navigation, missing assets, API failures, and incorrect user-session behavior that isolated unit tests miss. It is generally more expensive and sensitive to environment and data setup.

**Illustrative Cypress scenario (NOT executable against `example.com`):** The application under test must first implement the named routes, controls and messages. Use a local test deployment with deterministic fixtures; never create disposable users or delete accounts on a public site you do not control.

```javascript
describe('User account lifecycle', () => {
  it('registers, signs in, updates a profile and deletes a test account', () => {
    cy.visit('/register'); // configure baseUrl to your own test deployment
    cy.findByRole('textbox', { name: /username/i }).type('testuser');
    cy.findByRole('textbox', { name: /email/i }).type('testuser@example.com');
    cy.findByLabelText(/^password$/i).type('a-fixture-password');
    cy.findByRole('button', { name: /create account/i }).click();
    cy.findByText(/welcome, testuser/i).should('be.visible');

    cy.findByRole('button', { name: /log out/i }).click();
    cy.findByRole('link', { name: /log in/i }).click();
    cy.findByRole('textbox', { name: /email/i }).type('testuser@example.com');
    cy.findByLabelText(/^password$/i).type('a-fixture-password');
    cy.findByRole('button', { name: /log in/i }).click();
    cy.findByRole('link', { name: /profile/i }).click();
    cy.findByRole('textbox', { name: /profile information/i }).type('Updated profile info');
    cy.findByRole('button', { name: /save profile/i }).click();
    cy.findByText(/profile updated successfully/i).should('be.visible');

    cy.findByRole('link', { name: /account settings/i }).click();
    cy.findByRole('button', { name: /delete account/i }).click();
    cy.findByRole('button', { name: /confirm deletion/i }).click();
    cy.findByText(/account has been deleted/i).should('be.visible');
  });
});
```

The `findByRole`, `findByLabelText`, and `findByText` commands above require the separate **Cypress Testing Library** integration; they are not built-in Cypress commands. Substitute supported `cy.contains()`/`cy.get()` selectors if that integration is absent. The example also assumes the application exposes a stable, test-only account workflow; adapt the accessible names to your real UI.

A maintainable suite resets fixtures between tests, avoids shared account state, waits for **observable conditions** rather than arbitrary sleep intervals, and cleans up even after failures. Check both success and error flows (duplicate account, network failure, insufficient permissions).

#### UI and browser-interaction tests

These tests exercise visible controls: clicking, typing, tabbing, opening a dialog, or submitting a form. For example, right-click a target button and verify that its contextual popup appears. Selenium can automate such an interaction:

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Illustrative only: replace this with a local test page that defines both IDs.
driver = webdriver.Chrome()
try:
    driver.get('http://localhost:8000/context-menu.html')
    button = driver.find_element(By.ID, 'rightClickButton')
    ActionChains(driver).context_click(button).perform()
    popup = driver.find_element(By.ID, 'popupWindow')
    assert popup.is_displayed()
finally:
    driver.quit()
```

The local page must implement the custom context-menu handler. Right-clicking a generic button does **not** automatically open an application popup. Prefer stable roles, accessible names, or documented test IDs over selectors tightly coupled to layout.

#### Visual regression tests: compare what actually renders

A screenshot comparison answers “did these pixels or regions change?” rather than “is the page correct?” Baseline images can catch unintended layout changes, but fonts, operating systems, dynamic timestamps, advertisements, and animations create noise. Fix viewport dimensions, font assets, device scale, data fixtures, and animation state before interpreting diffs. Review expected visual changes intentionally; do not update all baselines automatically just to make tests green.

A beginner-friendly set of comparisons is provided by the [before-and-after examples](../projects/visual-examples/README.md), with a runnable [browser project](../projects/visual-examples/README.md). These SVGs are *illustrative wireframes*, **not** real screenshot test baselines:

![Side-by-side comparison of a form with hidden versus explicit error feedback](../assets/visual-examples/form-validation.svg)

For an actual regression test, launch the demo at a fixed viewport, capture a screenshot, change one CSS property, capture it again, and explain the intended pixel differences. Also verify that the error text is announced or discoverable, since a screenshot cannot prove accessible behavior.

#### Mock servers and request interception

A controlled backend substitute helps test success, error responses, network delay, and malformed data without relying on an external service. Match the interception layer to the implementation: **Nock intercepts supported Node.js HTTP requests**; it is not a universal interceptor for `fetch` running in a real browser. For browser requests consider browser automation routing or a service-worker mocking library such as Mock Service Worker, depending on your environment.

**Node.js-focused example with Nock:**

```javascript
const nock = require('nock');
const api = require('./api'); // must call a Node-compatible HTTP client to api.example.com

test('fetches mock data', async () => {
  nock('https://api.example.com')
    .get('/data')
    .reply(200, { message: 'Success', data: { value: 42 } });

  const response = await api.fetchData();
  expect(response.message).toEqual('Success');
  expect(response.data.value).toEqual(42);
});
```

The module `./api` is an application dependency you must implement. Add a `500` response test to prove the application displays a recoverable error, and confirm that all expected HTTP mocks were consumed so a test cannot silently pass without making a request.

### Automated versus manual testing

**Automated checks** run repeatable scripted scenarios in development or CI. They are good for regression coverage and fast feedback, but cannot decide whether requirements are valuable or detect every usability issue. A flaky test needs investigation; repeated reruns are not a replacement for fixing the cause.

**Manual and exploratory checks** let testers notice confusing language, misleading hierarchy, unusual device behavior, and needs that scripted scenarios missed. Human observation is not the same as statistically representative user research; record the device, browser, task, and result so findings can be reproduced.

A practical release checklist combines: unit and integration tests; one or two essential E2E journeys; keyboard-only navigation and visible focus; semantic labels and readable error messages; narrow viewport and 200% zoom; realistic slow-network states; and security/performance evaluation appropriate to the project.

### Online resources for website testing

Use tools as evidence of specific properties, not as an overall quality score. A successful validator does not replace interaction testing; a performance lab score does not represent every user's network.

#### Code quality

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Links

- [Dr. Link Check](https://www.drlinkcheck.com/)
- [Check My Links on GitHub](https://github.com/PageModifiedOfficial/Check-My-Links)

#### Performance

- [Dareboost](https://www.dareboost.com/en)
- [Yellow Lab Tools](https://yellowlab.tools/)
- [PageSpeed Insights](https://pagespeed.web.dev/)

#### Security

- [Mozilla Observatory](https://observatory.mozilla.org/)
- [Webbkoll](https://webbkoll.dataskydd.net/en)

#### SEO

- [Ahrefs' Free SEO Tools](https://ahrefs.com/free-seo-tools)

**Further reading:** [MDN: testing](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing), [Cypress documentation](https://docs.cypress.io/), [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/), [Selenium documentation](https://www.selenium.dev/documentation/), [Playwright documentation](https://playwright.dev/docs/intro), [Nock documentation](https://github.com/nock/nock).