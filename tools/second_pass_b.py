#!/usr/bin/env python3
"""One-time, anchored expansions of the ORIGINAL chapters 08–13."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'
modified = set()


def insert(filename, heading, body):
    path = NOTES / filename
    source = path.read_text(encoding='utf-8')
    assert source.count(heading + '\n') == 1, f'{filename}: missing or ambiguous heading {heading!r}'
    assert body.strip().splitlines()[0] not in source, f'{filename}: already inserted'
    path.write_text(source.replace(heading + '\n', heading + '\n\n' + body.strip() + '\n\n', 1), encoding='utf-8')
    modified.add(filename)


def correct(filename, old, new):
    path = NOTES / filename
    text = path.read_text(encoding='utf-8')
    assert old in text, f'{filename}: correction anchor missing: {old[:75]!r}'
    path.write_text(text.replace(old, new), encoding='utf-8')
    modified.add(filename)

# 08 protocols: HTTP lifecycle, transport/caching, diagnostics, security.
insert('08_protocols.md', '#### Browsers', """##### From URL to pixels: identify which layer failed

A browser navigation is not a single network operation. The browser may look at HTTP caches or a service worker; resolve DNS if needed; reuse an existing connection or establish TLS/QUIC; send an HTTP request; receive HTML; parse it; fetch CSS, images and scripts; construct layout; and paint. Steps may overlap, be skipped or repeat. The [request lifecycle diagram](../assets/diagrams/request-lifecycle.svg) is a conceptual teaching aid, not a promise that every request follows exactly the same path.

| Visible symptom | First inspection point | Example explanation |
|---|---|---|
| Browser cannot resolve host | DNS and authoritative record | Typo, missing record or cached old answer. |
| Certificate warning | HTTPS certificate and hostname | Expired certificate or wrong hostname. |
| HTML loads but appears unstyled | Network panel's CSS request | Wrong path, 404 or MIME mismatch. |
| Page looks fine but button does nothing | Console and event listeners | JavaScript exception or missing handler. |
| API request returns 401 | Server authentication contract | No valid credentials; not a DNS failure. |
| API response blocked in browser | Console and CORS headers | Cross-origin access not permitted to script. |

**Reproduce it:** serve the [visual examples project](../projects/visual-examples/README.md) over `http://localhost:8000`, open DevTools, disable cache, reload and identify the HTML, CSS and JavaScript requests. Change the stylesheet link temporarily to a nonexistent path: the HTML remains meaningful but loses styling. Restore the URL and verify recovery. The browser's Network panel reveals *observed* timing and requests; do not infer a particular TCP packet sequence from its waterfall.

A service worker can intercept requests and work offline, but is not present in every page. Browser storage, cache storage, HTTP cache, cookies and localStorage are distinct mechanisms with different scopes and lifetimes. Reference: [MDN how the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works).""")

insert('08_protocols.md', '#### DNS (Domain Name System)', """##### DNS record walkthrough: apex, www, mail, and verification

Suppose a hosting provider instructs you to point `www.example.com` at `site.host.example` and the domain's email provider already operates the mailbox. The website change and the email records are separate: modifying one should not erase the other. Names and values below are illustrative; **use your own provider's verified instructions**, not these demonstration targets.

```text
www.example.com.  300 IN CNAME site.host.example.
example.com.      300 IN A     192.0.2.25
example.com.     3600 IN MX    10 mail.example.net.
example.com.     3600 IN TXT   "verification-example"
```

`192.0.2.0/24` is a reserved documentation network, not a real hosting destination. Standard DNS generally does not permit a CNAME to coexist with other data at the same owner name, so check provider-specific apex alias/flattening support when configuring the zone apex. An MX target is a *mail-exchange hostname*, not a web-server IP. A TXT record may carry sender policies or site verification; overwriting one can affect mail or other integrations.

```bash
dig example.com NS
dig example.com A
dig www.example.com CNAME
dig example.com MX
```

These commands require `dig` and a reachable resolver. Inspect the answer section, queried record type, TTL and authoritative nameservers, not just whether some IP is printed. Recursive resolvers cache answers according to TTL, and a warm cache can bypass queries to root or TLD servers. DNS resolution does not validate the TLS certificate or prove the site is safe. **Exercise:** draw a table of the records you intend to change, current values, replacement values, TTL and rollback owner before editing a live zone. Reference: [MDN DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS).""")

insert('08_protocols.md', '#### HTTP (HyperText Transfer Protocol)', """##### Inspect a response, not merely the URL

```http
GET /courses HTTP/1.1
Host: example.com
Accept: text/html

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: public, max-age=60

<!doctype html><title>Courses</title>
```

This is a schematic request/response pair, not a raw packet capture: actual connections may use HTTP/2 or HTTP/3 with different wire representations. `Content-Type` describes the representation; `Cache-Control` gives caches instructions. A `200 OK` means the server returned a successful HTTP response, not that the HTML is valid, usable or free of application errors. A redirect such as `301` or `302` tells the client to follow another location according to method-specific rules; inspect the redirect chain instead of treating it as a missing file.

| Status | Typical meaning | Frontend response |
|---|---|---|
| 200 | Resource provided | Parse/render expected content. |
| 204 | Successful, no response body | Do not call `response.json()` expecting JSON. |
| 304 | Cached representation remains valid | Browser reuses a stored representation when appropriate. |
| 400 | Request invalid | Show guidance; fix client input or contract. |
| 401 | Authentication needed or invalid | Reauthenticate through the intended flow. |
| 403 | Access denied | Do not blindly repeat a forbidden operation. |
| 404 | Resource not found | Render a useful missing-content state. |
| 429 | Too many requests | Respect `Retry-After` where provided. |
| 500/503 | Server failure/unavailable | Show recoverable feedback; avoid duplicate destructive retries. |

```js
async function getCourses(signal) {
  const response = await fetch('/api/courses', { signal });
  if (!response.ok) throw new Error(`Request failed: ${response.status}`);
  if (response.status === 204) return [];
  return response.json();
}
```

The snippet requires an actual `/api/courses` endpoint. A browser `fetch` promise generally resolves for HTTP error statuses; it rejects for network errors, aborts and certain other failures. Error bodies may not be JSON, so production code should handle invalid response formats. CORS determines whether a browser script can read a cross-origin response; **it is not a mechanism for protecting an endpoint from direct requests**. Authorization must be enforced on the server.

**Try it:** inspect the browser demo's Network tab, use DevTools throttling, observe a request with cache disabled, and explain the difference between a network failure and an HTTP 404. Reference: [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) and [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).""")

insert('08_protocols.md', '### Protocols in Action', """#### HTTP versions, transport, and TLS: avoid mixing responsibilities

| Layer/concept | What it provides | What it does not guarantee |
|---|---|---|
| DNS | Resolves names to records. | That a destination is trustworthy or available. |
| IP | Addresses and forwards packets. | Reliable, ordered application messages. |
| TCP | Reliable ordered byte stream. | Message boundaries matching `write()` calls. |
| UDP | Datagram transport. | Reliability or ordering on its own. |
| QUIC | Reliable streams and TLS 1.3 integration over UDP. | That a server supports every HTTP feature. |
| TLS | Authenticated, encrypted transport when correctly configured. | That application code or user content is safe. |
| HTTP | Request/response semantics and headers. | Automatic login or authorization. |

HTTP/1.1 and HTTP/2 commonly run over TCP with TLS for HTTPS; HTTP/3 runs over QUIC, which uses UDP. A TCP connection delivers bytes, not an array of `fetch()` results. Browser connection reuse and multiplexing can change network waterfalls considerably. A lock icon signals certain connection properties, **not** that a business or page is trustworthy.

**Diagnostic exercise:** start with “DNS works, but the browser refuses HTTPS.” Do not edit CSS or retry DNS blindly; inspect certificate chain, hostname, transport and the host's configuration. For a `403`, examine permissions and server policy. For a stalled CSS file, examine its request status and caching. Reference: [HTTP/3 RFC 9114](https://www.rfc-editor.org/rfc/rfc9114) and [MDN TLS](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security).""")

# 09 project structure: explain boundaries, implementation and deployment, not folder vanity.
insert('09_project_structure.md', '### What to optimize for', """#### Walk through an actual change before picking folders

Suppose a product owner asks for an email subscription form. Trace one task end to end: where does the HTML form live? Which stylesheet owns spacing and states? Where does client-side validation run? What endpoint receives the POST? Which tests cover invalid input and server rejection? If answering requires searching a dozen unrelated folders, the structure may need to change; if everything is in a five-file project, splitting into 20 directories makes it worse.

A useful change trace:

```text
User requirement
  -> HTML form and labels
  -> CSS state styles
  -> JavaScript event handler
  -> /api/subscribe contract (server, not public bundle)
  -> unit + integration + browser tests
  -> preview deployment -> production
```

The [actual browser form example](../assets/visual-examples/form-validation-browser.png) illustrates the *user-visible* end of that chain. The [project source](../projects/visual-examples/README.md) keeps markup, CSS and JavaScript small enough to inspect. It intentionally does **not** implement `/api/subscribe`, so it is not a production email service.

**Decision check:** when changing the label, should you edit the HTML or five duplicated component definitions? When changing validation, can you test it without launching the entire application? When changing the endpoint, can you preserve the frontend contract? Document boundaries in the README. Do not mistake folder count for architecture quality.""")

insert('09_project_structure.md', '### Alternative: organize by feature', """#### Worked feature slice: cart with public and private boundaries

A feature-oriented tree is useful only when it reflects real ownership, not arbitrary directories:

```text
src/
  features/
    cart/
      CartButton.jsx
      cart.css
      cart.test.jsx
      cart-api.js
  shared/
    Button.jsx
    format-currency.js
server/
  routes/
    checkout.js
  services/
    payments.js
```

`cart-api.js` may send a request, but it **must not** contain a private payment-provider token: everything shipped in a client bundle can be inspected. The server checkout route validates prices and quantities against authoritative data and checks the user's permissions. The client can display a calculated subtotal for feedback, but the server must recompute amounts before charging. Tests at each boundary check different risks: rendering and keyboard focus, request contract, business rules, and the full checkout workflow.

For smaller sites, keep related files together without introducing an `index.js` re-export for every folder. A barrel file that imports unrelated modules may complicate dependency graphs; measure bundle output before claiming it makes tree shaking faster. Move a module to `shared/` only when actual consumers share stable behavior. Avoid circular imports: extract common interfaces or rethink ownership when A imports B and B imports A.

**Exercise:** on paper, implement a “Remove from cart” action: mark the UI module, state owner, API boundary and test. Then add an inaccessible alert as a simulated error and decide how to give a meaningful recovery message. An attractive folder diagram is not evidence that the feature works.""")

insert('09_project_structure.md', '### Best practices for a production build', """#### Deployment artifacts and environment variables are separate concerns

```text
source files (src/)
    | lint, type-check, tests
    v
build step -> output files (dist/)
    | copy/publish only expected artifacts
    v
hosting + HTTPS + routing + caching
```

A bundler may inline environment variables into JavaScript. Anything in the browser bundle should be treated as public, even if named `SECRET_KEY` or kept in a hidden folder. Server secrets belong in protected deployment configuration, and the server must authorize requests independently of frontend UI visibility.

A typical `package.json` might have explicit scripts for `lint`, `test`, `build`, and `preview`; their exact commands depend on project tools. The deployment host must publish the correct output directory and handle deep links appropriately. Do not upload `node_modules/`, `.env` secrets or local credential files merely because they exist in a repository checkout.

**Verification checklist:** inspect generated HTML and asset URLs; check route reloads on preview; view the browser Network tab for missing fonts/images; measure JS and CSS transfer size; check console errors; try keyboard and narrow viewports; verify rollback instructions. Compare [raw versus styled card output](../assets/visual-examples/card-styling-browser.png) to ensure the correct stylesheet reached production. Reference: [OWASP secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).""")

insert('09_project_structure.md', '### Boilerplates', """#### Template evaluation worksheet (before cloning)

| Question | Evidence to collect | Failure signal |
|---|---|---|
| Is it maintained? | Release history, current dependencies, issue activity. | Unsupported runtime or abandoned dependencies. |
| Can it build? | Documented setup and a clean install/build. | Undocumented manual edits. |
| Is it accessible? | Keyboard/focus/form tests on example pages. | Placeholder-only labels and hidden focus. |
| Is it appropriately licensed? | Repository license and asset licenses. | No grant for your intended use. |
| Is it deployable? | Output directory, routing, environment contract. | Works only on the author's machine. |
| Can we remove unused parts? | Dependency graph and generated output. | Unnecessary services or bundled secrets. |

Do not turn a tutorial's `git clone` example into an unverified recommendation. If a template teaches deprecated APIs, show the specific migration (such as moving from `ReactDOM.render` to `createRoot`) and keep its historical context. Record which upstream revision you actually inspected; labels like “latest best practices” expire quickly.

**Hands-on task:** run the repository's minimal [visual examples](../projects/visual-examples/README.md) without any install step, then inspect a chosen framework template's setup. List which extra behaviors (routing, server rendering, testing, linting) justify each new dependency. Reference: [React app setup](https://react.dev/learn/start-a-new-react-project).""")

# 10 testing: independently runnable example and behavior-oriented browser assertions.
insert('10_testing.md', '### What is testing?', """#### Turn a feature request into a test matrix

**Feature:** a newsletter form shows a useful error for invalid input and never falsely reports success. “The component exists” is not a strong assertion. Define observable conditions before writing automation:

| Input/action | Expected result | Test level |
|---|---|---|
| Blank email; submit | Required-field guidance; no success | Browser and validation unit. |
| `not-an-email`; submit | Specific visible error; invalid state | Browser interaction. |
| Valid syntax; submit | Demo confirmation or real request | Integration/browser. |
| Server rejects valid-looking address | Server error and recovery guidance | Integration and E2E. |
| Network goes offline | Clear retry option; no invented success | Integration/browser. |
| Keyboard only | All controls reachable, focus visible | Accessibility/manual/browser. |
| Narrow viewport | Labels and error stay readable | Visual and responsive. |

The [actual browser-rendered form states](../assets/visual-examples/form-validation-browser.png) are **examples**, not proof that all these cases are covered. The [live demo](../projects/visual-examples/index.html) deliberately sends no request, so server rejection and network failure require a separate application fixture.

**Exercise:** remove the form's `aria-describedby` and rerun an automated screenshot test. Pixels might stay identical while the association becomes worse. Test accessible names/relations and keyboard focus **in addition to** screenshots. Good tests state what failed: `invalid email should expose a descriptive error` is more useful than `expected true to be false`. Reference: [Testing Library guiding principles](https://testing-library.com/docs/guiding-principles/).""")

insert('10_testing.md', '#### Unit testing in depth', """##### Executable example with Node's built-in test runner

The Roman-numeral example further down assumes an application module. Here is a complete, dependency-free example that runs on a Node.js version supporting `node:test`; create **both files** in an empty directory.

`price.js`:

```js
function totalCents(unitCents, quantity) {
  if (!Number.isSafeInteger(unitCents) || unitCents < 0) {
    throw new RangeError('unitCents must be a nonnegative safe integer');
  }
  if (!Number.isSafeInteger(quantity) || quantity < 1 || quantity > 100) {
    throw new RangeError('quantity must be between 1 and 100');
  }
  const result = unitCents * quantity;
  if (!Number.isSafeInteger(result)) throw new RangeError('total overflow');
  return result;
}
module.exports = { totalCents };
```

`price.test.js`:

```js
const test = require('node:test');
const assert = require('node:assert/strict');
const { totalCents } = require('./price');

test('multiplies integer cents', () => {
  assert.equal(totalCents(125, 3), 375);
});
test('rejects invalid quantities', () => {
  assert.throws(() => totalCents(125, 0), RangeError);
  assert.throws(() => totalCents(125, 1.5), RangeError);
});
test('rejects unsafe totals', () => {
  assert.throws(() => totalCents(Number.MAX_SAFE_INTEGER, 2), RangeError);
});
```

Run `node --test price.test.js`. Expected: **three passing tests**. No currency formatting, tax, discounts or payment processing is implemented; those would need separate business rules. This example uses integer cents to avoid a common floating-point mistake. Alter `quantity > 100` to `quantity > 10` and add a test for 11 to practice preserving an intentional requirement.

**Why this is a unit test:** no browser, network or database is required; the input-output contract is explicit. Do not generalize “unit tests are enough” to the checkout application that eventually consumes this function. Reference: [Node.js test runner](https://nodejs.org/api/test.html).""")

insert('10_testing.md', '#### End-to-end (E2E) testing', """##### Robust workflow assertions, fixtures, and cleanup

For a real login/checkout E2E test, create an isolated test account via a documented fixture rather than hardcoding a shared production user. Use a test environment with predictable data and reset it even when assertions fail. Favor observable signals over arbitrary delays:

```js
// Playwright Test example: requires @playwright/test and your own app fixture.
import { test, expect } from '@playwright/test';

test('invalid email displays an explanation', async ({ page }) => {
  await page.goto('http://localhost:8000/projects/visual-examples/');
  const email = page.getByRole('textbox', { name: 'Email address' }).last();
  await email.fill('not-an-email');
  await page.locator('#newsletter').getByRole('button', { name: 'Subscribe' }).click();
  await expect(email).toHaveAttribute('aria-invalid', 'true');
  await expect(page.locator('#email-feedback')).toContainText('valid email');
});
```

Start a local HTTP server at the repository root before running this example and check the demo's current error wording; the test is an instructional adaptation, not a checked-in configured Playwright suite. `.last()` disambiguates two visually compared inputs here, but in a production suite scope selectors to a named form or region rather than relying on positional selection. A correct E2E test must also assert the real backend's behavior when the journey includes one.

**Flakiness triage:** record browser version, viewport, fixture seed, failed network requests and screenshots on failure. A failure caused by a genuine race is a product signal; do not hide it with blanket retries. Reserve true external-service tests for a deliberately controlled environment. Reference: [Playwright assertions](https://playwright.dev/docs/test-assertions).""")

insert('10_testing.md', '#### Visual regression tests: compare what actually renders', """##### Make the screenshot baseline reproducible

A practical visual test needs an explicit *baseline contract*: page state, fixture content, viewport in CSS pixels, device scale, browser version, fonts, reduced-motion behavior, animations, locale and time zone when relevant. Capture the smallest meaningful region as well as a full-page view where appropriate. A percentage of changed pixels has no built-in semantic meaning: a changed logo and a clipped error message might affect very different amounts of the image.

For these notes, [eight before/after pairs](../projects/visual-examples/README.md) were rendered in Chromium, exported to PNG and placed near the concepts. See the [card rendering](../assets/visual-examples/card-styling-browser.png) and [narrow navigation](../assets/visual-examples/responsive-navigation-mobile.png). Their purpose is teaching, not an automatically approved baseline for your product.

**Suggested workflow:** (1) open the exact fixture, (2) set the viewport, (3) wait for fonts and stable content, (4) freeze animations as appropriate, (5) take the screenshot, (6) review differences *with the intended CSS change*, and (7) separately assert semantics and behavior. A baseline update should be reviewed like a code change, not performed automatically on every failure. Check horizontal overflow at narrow widths; a screenshot cropped to the viewport may hide off-screen content.

**Exercise:** remove the visible focus outline from the demo, capture the button section, and compare images *in the focused state*. Then verify the keyboard focus indicator independently: the screenshot cannot tell whether Tab actually reaches the link or which accessible name it exposes. Reference: [Playwright screenshots](https://playwright.dev/docs/screenshots).""")

# 11 hosting: practical deploy/rollback and DNS, with no fabricated provider pricing.
insert('11_hosting_websites.md', '## Hosting', """### Worked deployment: a static HTML/CSS/JavaScript site

Start with a local site containing `index.html`, `styles.css`, `script.js` and any image files. Confirm that each relative URL resolves from the route where it appears. For the repository's [visual demo](../projects/visual-examples/README.md), launch a local server from the **repository root**:

```bash
python3 -m http.server 8000
```

Visit `http://localhost:8000/projects/visual-examples/`, inspect DevTools → Network, and make sure all local assets return successfully. This tests local serving, not a production deployment. A static host can generally publish this directory without running a Node.js server, but the host must be configured to publish the right path or copy an appropriate `dist/` artifact. If links use absolute `/assets/...` paths and the site is deployed under a subpath, they may fail; test the actual public base URL.

| Step | Artifact or evidence | Failure worth catching |
|---|---|---|
| Build | Generated HTML/CSS/JS when required | Wrong output directory. |
| Preview | Unique preview URL | Missing image or CSS. |
| Interaction | Keyboard + form behavior | Client error hidden by successful HTTP 200. |
| Production | Correct custom hostname | Domain points to older deployment. |
| Monitor | Errors and uptime | Silent failures after release. |
| Rollback | Known working revision | Cannot restore previous artifact. |

**Hands-on exercise:** deliberately rename `styles.css` to `missing.css` in a throwaway copy and inspect the 404. Repair the link, deploy to a preview target you control, and test a direct refresh of any deep route. This is a genuine network behavior change even though the HTML source itself may look unchanged. Reference: [MDN publishing your website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website).""")

insert('11_hosting_websites.md', '### Deployment: from Git to a live site', """#### Production release and rollback checklist

A deployment may be automatic *after configuration* or manual. Separate the decision to merge code from the decision to publish it: regulated or high-traffic applications may require approvals, database migrations and a reversible release plan.

```text
Pull request + review
       |
Tests / lint / build
       |
Deploy preview -> manual smoke test
       |
Release approved commit
       |
Check live routing, HTTPS and key flows
       |
Monitor errors -> rollback or fix forward
```

**Static-site smoke test:** request `/`, a stylesheet, a JavaScript file, and an image; confirm their status and content type. Check a keyboard-only journey, a narrow viewport, the browser console, an unknown route and a direct reload of a valid deep route. For a server-backed application, add a safe test of its health endpoint and permissions. A green CI check does not prove a domain points to the newest revision: compare the deployed commit or asset hash when supported.

**Rollback plan:** identify the previous published artifact, who may trigger restoration, whether database migrations are backward compatible, and how to communicate an outage. Rollback of frontend assets alone may not restore compatibility with a changed backend API. Keep secrets in the hosting configuration and rotate them if exposed; removing a leaked secret from the latest commit does not erase it from history or deployed artifacts.

**Exercise:** describe how you would recover if the homepage loads but all CSS files return 404 after release. Identify the symptom in Network, correct the deployment path, and verify cache headers without assuming a DNS failure. Reference: [OWASP deployment and maintenance](https://owasp.org/www-project-developer-guide/).""")

insert('11_hosting_websites.md', '## Connecting a domain to hosting', """### Diagnose the complete chain with commands and observations

Use a domain that you own and have permission to test. The commands below demonstrate a **read-only** workflow; they do not change production DNS:

```bash
# Which nameservers are authoritative for your domain?
dig example.com NS
# Which IPv4 and IPv6 destinations does the resolver return?
dig example.com A
dig example.com AAAA
# Does the www host alias another hostname?
dig www.example.com CNAME
# What does the HTTP endpoint actually return?
curl -I https://example.com/
```

`example.com` is a documentation placeholder: substitute your actual domain. `curl -I` sends a HEAD request; a server may not support it even when a GET works, so retry with a normal GET when investigating an unexpected status. The IP alone does not identify which virtual host serves the website: TLS SNI and HTTP Host/authority also matter. For a certificate error, inspect hostname, expiry, chain and provisioning; do not disable certificate validation to make the error disappear.

**DNS sequence:** the registrar manages the registration, but authoritative nameservers may belong to a different DNS provider. Editing a zone that is not authoritative has no public effect. Cache TTL describes how long resolvers may reuse records; it is not a guarantee that a global change occurs at an exact time. A CNAME is not a general replacement for MX or TXT records. Take a snapshot of the existing zone and check mail records before modifying the apex or nameserver delegation.

**Troubleshooting exercise:** distinguish these cases: `dig` returns the old address; `dig` returns the new address but TLS fails; the homepage loads but the SPA's deep route 404s; the API responds with 403. Each points to a different layer and needs a different fix. See the [protocols request diagram](../assets/diagrams/request-lifecycle.svg).""")

# 12 quizzes: add applied scenarios, do not inflate with recycled definitions.
insert('12_quizes.md', '## HTML', """### Applied HTML scenarios — predict, then verify

<details><summary>1. A document has a viewport meta tag but a 900px-wide image overflows on a 320px phone. Why?</summary>

The viewport declaration changes viewport sizing behavior; it does not constrain fixed-width content. Use a responsive rule such as `img { max-width: 100%; height: auto; }`, inspect the container, and test with actual content. Try the [responsive browser demo](../projects/visual-examples/index.html) at narrow widths.
</details>

<details><summary>2. A form has placeholder="Email" but no label. What disappears when someone types?</summary>

The visible prompt disappears; the input may also lack a reliable accessible name. Use `<label for="mail">Email</label><input id="mail" name="email" type="email">`. Helper text is separate from the label. The [form comparison screenshot](../assets/visual-examples/form-validation-browser.png) shows what feedback changes visually.
</details>

<details><summary>3. Should a clickable logo that navigates home be a button or link?</summary>

Use a link with a real `href` and an accessible name representing the destination. Use a button for an action that does not navigate. If the logo image is the link's only content, meaningful `alt` text can supply its name.
</details>

<details><summary>4. Does replacing every div with section make the page automatically accessible?</summary>

No. Choose elements by meaning; `section` generally needs an accessible identifying heading when used as a region. A page needs sensible heading order, link text, forms, keyboard behavior and testing. Compare the [semantic structure browser capture](../assets/visual-examples/semantic-html-browser.png) and inspect its two underlying HTML documents.
</details>

<details><summary>5. A data table has visually bold first-row cells written as td. What information is missing?</summary>

The cells are not explicitly headers. Use `<th scope="col">` for simple column headers, `<th scope="row">` for row headers, and a `<caption>` when useful. CSS can style `td` bold, but that does not give it header semantics.
</details>
""")

insert('12_quizes.md', '## CSS', """### Applied CSS scenarios — inspect the computed result

<details><summary>1. A card declares width: 320px, padding: 24px on each side and a 2px border on each side. How wide is its border box by default?</summary>

With default `box-sizing: content-box`, it is `320 + 48 + 4 = 372px`, excluding margins. With `border-box`, a declared width of 320px includes padding and borders when layout can resolve the dimension. Inspect the Box Model in DevTools.
</details>

<details><summary>2. An ID selector and a class selector set different colors. Does the last rule always win?</summary>

No. If origin, importance, layer and other earlier cascade stages tie, specificity decides; an ID selector is more specific than a class selector. Source order resolves ties at the relevant stage. Important declarations and cascade layers complicate this, so inspect computed styles.
</details>

<details><summary>3. flex-direction changes from row to column. Does justify-content still mean horizontal alignment?</summary>

No. `justify-content` uses the main axis, which changes with `flex-direction`; `align-items` uses the cross axis. Experiment with the [actual Flexbox comparison](../assets/visual-examples/flex-alignment-browser.png).
</details>

<details><summary>4. What does a size container query measure that a media query does not?</summary>

A size container query tests an eligible ancestor container's dimensions, not the viewport. Declare a container such as `container-type: inline-size`, then use `@container`. The query styles descendants, not the query container itself. See the [responsive navigation captures](../assets/visual-examples/responsive-navigation-browser.png).
</details>

<details><summary>5. Why is outline: none dangerous on interactive controls?</summary>

It can hide keyboard focus. Replace it with a strong `:focus-visible` outline when styling focus, test Tab navigation and forced-colors mode. Compare the [browser focus image](../assets/visual-examples/keyboard-focus-browser.png).
</details>
""")

insert('12_quizes.md', '## JavaScript', """### Applied JavaScript scenarios — explain each output

<details><summary>1. What do Number('12px') and parseInt('12px', 10) produce?</summary>

`Number('12px')` is `NaN`; `parseInt('12px', 10)` returns 12 because it accepts a valid integer prefix. A form that requires the whole string to be an integer should validate the entire input, not silently accept trailing text.
</details>

<details><summary>2. Is Number.MIN_VALUE the most negative finite Number?</summary>

No. It is the smallest **positive nonzero** representable Number. The finite negative value with greatest magnitude is `-Number.MAX_VALUE`, while `-Infinity` is not finite.
</details>

<details><summary>3. Why can fetch('/missing') resolve even when the server returns 404?</summary>

The Fetch promise generally resolves to a `Response` for HTTP errors. Check `response.ok` or `response.status`; reject/throw explicitly for application handling. Network failures and aborts are different cases.
</details>

<details><summary>4. What logs first: a synchronous statement, a Promise.then callback, or setTimeout(..., 0)?</summary>

The synchronous statement runs during the current job, then the Promise reaction microtask, then the timer task (assuming a typical browser event-loop case). A zero-delay timer does not execute immediately in the middle of the current job.
</details>

<details><summary>5. Does assigning a React state variable immediately change its value in the current render?</summary>

No. A state setter schedules an update; code in the current render/event sees that render's state snapshot. Use a functional updater like `setCount(c => c + 1)` when next state depends on previous state. React's old `ReactDOM.render` API should be replaced with `createRoot` for current examples.
</details>
""")

insert('12_quizes.md', '## Protocols', """### Applied network scenarios — choose the right layer

<details><summary>1. Does HTTP/3 require a TCP connection?</summary>

No. HTTP/3 runs over QUIC, which uses UDP and provides reliable streams with TLS 1.3 integration. HTTP/1.1 and HTTP/2 commonly use TCP. The HTTP semantics are not identical to the underlying transport format.
</details>

<details><summary>2. The DNS A record is correct but HTTPS shows a certificate warning. Which layer needs investigation?</summary>

DNS resolution alone cannot validate the TLS certificate. Inspect certificate hostname, expiry, provisioning and chain, as well as the server's HTTPS configuration. Do not disable certificate verification to hide a problem.
</details>

<details><summary>3. Does CORS prevent another client from calling a public API?</summary>

No. CORS mediates cross-origin access by browser scripts. It is not authentication or authorization; the API must enforce permissions server-side regardless of origin.
</details>

<details><summary>4. Why might a cached page return 304?</summary>

A conditional request allows a server to indicate the cached representation is still valid. The client can reuse an appropriate stored body; 304 does not carry a new normal representation body. Inspect validators and Cache-Control instead of calling every cached response an error.
</details>

<details><summary>5. Why is curl -I insufficient proof that a site's GET route works?</summary>

`curl -I` sends HEAD; some applications handle HEAD differently. Verify the actual GET request and response body/content type when debugging a page. Check status, redirects and network failures separately.
</details>
""")

insert('12_quizes.md', '## Hosting', """### Applied deployment scenarios — justify the next action

<details><summary>1. A static host serves index.html, but a direct reload of /profile returns 404. Is DNS necessarily broken?</summary>

No. A client-side router may need an appropriate hosting rewrite/fallback rule, or the route may not exist on the server. Inspect the host's routing behavior and route design rather than changing DNS at random.
</details>

<details><summary>2. Can a frontend environment variable named SECRET_API_KEY be considered private?</summary>

No, not when its value is shipped in browser JavaScript. Move secret-dependent operations and authorization to a protected backend; storing a secret in a different frontend directory does not hide it.
</details>

<details><summary>3. A provider says to create a CNAME for www. Should you overwrite existing MX records at the apex?</summary>

No. Mail records have separate purposes. Follow the host's exact hostname instructions, identify the authoritative DNS provider, preserve mail and verification records, and check the applicable record restrictions.
</details>

<details><summary>4. Are DNS changes guaranteed to take exactly 48 hours?</summary>

No. Recursive caches may retain earlier answers until their TTL; authority changes and operational factors vary. Inspect authoritative records and cached responses rather than quoting a universal duration.
</details>

<details><summary>5. The site works locally but styles are missing after deployment. What should you inspect first?</summary>

Open DevTools Network, find the CSS request, check its URL, status and content type, and inspect the host's build output path and asset base URL. The error may have nothing to do with JavaScript frameworks or SSL configuration.
</details>
""")

# 13 resources: preserve every existing directory link while making selection actionable.
insert('13_additional_resources.md', '## Additional Resources', """### How to choose a resource without copying a polished mistake

This chapter is a **directory, not a certification program**. The sites below may offer free and paid assets, incompatible versions, or changing terms. When a resource looks useful, open its source and license, run the demo where possible, then test how it behaves in *your own* layout. Do not treat a beautiful screenshot as evidence of accessibility, performance or permission to redistribute its assets.

| Question | Check in practice | Document for future maintainers |
|---|---|---|
| Is reuse allowed? | Read the exact asset/template license and attribution conditions. | License URL and version/date. |
| Will it work in our stack? | Check peer dependencies, build output and supported framework version. | Package and version. |
| Can all users operate it? | Keyboard, focus, contrast, zoom, labels and errors. | Reproducible test notes. |
| Can it be modified? | Examine source, export format and component boundaries. | Local customization and owner. |
| Is it lightweight enough? | Inspect real transferred size and third-party requests. | Performance budget and tradeoffs. |
| Will it remain supported? | Review maintenance and update process. | Upgrade and replacement plan. |

**Mini case study:** choose a card design from an inspiration site. Rebuild its content with semantic `<article>`, a heading and real link. First inspect the [unstyled browser rendering](../assets/visual-examples/card-styling-browser.png), then apply its spacing and typography in the [live demo](../projects/visual-examples/index.html). Verify keyboard focus and mobile width. You may copy *ideas* while still needing permission to copy icons, photos, source code or trade dress.

**Suggested asset log:** `asset`, `source URL`, `author`, `license`, `attribution location`, `date checked`, `local filename`, `reason used`. This makes later audits and replacement feasible. Do not record “free” as a license: free price and reuse rights are different questions.""")

insert('13_additional_resources.md', '### 🎨 CSS Generators', """#### Inspect generated output and make it responsive

A generator may produce attractive declarations that behave poorly under different widths or color schemes. Rather than pasting a preset and stopping, rewrite the smallest reproducible test:

```html
<div class="generated-card">
  <h2>News</h2>
  <p>A very long translated description belongs here.</p>
  <a href="/news">Read the news</a>
</div>
```

```css
.generated-card {
  box-sizing: border-box;
  width: min(100%, 28rem);
  padding: clamp(1rem, 2vw, 1.5rem);
  border-radius: 1rem;
  background: #fff;
  color: #0f172a;
}
.generated-card a:focus-visible {
  outline: 3px solid #1d4ed8;
  outline-offset: 3px;
}
```

Compare the [actual styled-card capture](../assets/visual-examples/card-styling-browser.png). A generated blur or shadow may have contrast and performance costs; a CSS-only animation should respect reduced-motion preferences when motion is nonessential. Neumorphic controls sometimes lack clear boundaries, so check affordances and focus instead of selecting them purely by appearance. Test at 320px, zoom to 200%, add long text, and inspect computed styles. Keep the generated source and its original license where the tool provides one.""")

insert('13_additional_resources.md', '### 🎨 Graphical Elements', """#### Images, icons and illustrations: use the right alternative text

The correct alternative depends on the **purpose in context**:

```html
<!-- Content image: describe information not otherwise present. -->
<img src="chart.png" alt="Revenue increased from January to March"
     width="640" height="360">

<!-- Decorative flourish: empty alternative, not the filename. -->
<img src="divider.svg" alt="" width="120" height="16">

<!-- An icon-only action still needs a name. -->
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" viewBox="0 0 24 24" width="24" height="24">
    <path d="M5 5 19 19M19 5 5 19" stroke="currentColor"/>
  </svg>
</button>
```

Meaningful chart content often deserves an adjacent table or longer text explanation, not a 150-word `alt` attribute. Give content images dimensions or an aspect ratio to reserve layout space, and choose `loading="lazy"` for suitable below-the-fold images rather than applying it blindly to the hero image. An image's source URL, screenshot appearance and file extension do not establish its license.

**Try it:** take the [semantic browser screenshot](../assets/visual-examples/semantic-html-browser.png); write alternative text describing *the difference it teaches*, not every color or decorative rectangle. Compare this with an icon-only button's accessible name. Reference: [W3C image tutorial](https://www.w3.org/WAI/tutorials/images/).""")

insert('13_additional_resources.md', '### 🎨 Color palettes', """#### Test a palette on real interface states

A hex value must contain three, four, six or eight hexadecimal digits as supported by CSS; characters such as `K`, `S`, `G` or `%` are invalid in a hex color. The malformed codes in the older palette list were corrected in the earlier revision; do not assume that makes every remaining combination readable. A palette with five attractive swatches may fail when applied to small text, form errors, focus outlines and disabled controls.

```css
:root {
  --surface: #fff;
  --ink: #0f172a;
  --link: #1d4ed8;
  --focus: #0f172a;
}
body { background: var(--surface); color: var(--ink); }
a { color: var(--link); }
a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
```

These are **example roles**, not a guarantee for every background or text size. Check actual foreground/background combinations against the applicable WCAG contrast criteria (commonly at least 4.5:1 for ordinary text and 3:1 for large text under WCAG 2.x AA), with separate evaluation for non-text UI boundaries and focus indicators. Test both light/dark variants, forced colors and invalid/disabled states. Color must not be the only way to identify a form error.

**Exercise:** choose one palette above, assign a surface, text, link, error and focus role, and test the [form and button browser screenshots](../assets/visual-examples/form-validation-browser.png) and [button states](../assets/visual-examples/button-states-browser.png). If a combination fails contrast, adjust the role value and document what changed. Reference: [WCAG contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).""")

assert modified == {'08_protocols.md', '09_project_structure.md', '10_testing.md', '11_hosting_websites.md', '12_quizes.md', '13_additional_resources.md'}, modified
print('Second-pass B: expanded six ORIGINAL chapters, retaining existing content.')
