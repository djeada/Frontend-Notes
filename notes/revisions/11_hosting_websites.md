# Hosting: deploy, secure, and operate a site

[Original hosting chapter](../11_hosting_websites.md) · [All chapter updates](README.md)

Publishing a website requires a place to serve files or run code, a route from a domain name to that service, and an operational plan for changes and failures. Separate domain registration, DNS hosting, web hosting, and application execution: one vendor can provide several, but they are different responsibilities.

## Corrections to the original

- The provider price table gives temporary-looking starting prices and sometimes labels **hosting prices as domain prices**. Rates, renewal costs, and plan limits change; do not compare them as permanent domain registration quotes. Verify the full renewal price, taxes, transfer policy, and features directly with the provider.
- A DNS configuration is **not always a single A record**. Platforms may require a CNAME, A/AAAA records, ALIAS/ANAME-like flattening, or nameserver delegation. Follow the hosting provider's actual instructions.
- “Propagation takes up to 48 hours” is an oversimplification. Observed behavior depends on prior TTLs, recursive cache state, authoritative updates, and clients. A cached old record can persist until its TTL expires.
- Managed hosting does not automatically guarantee backups, patches for application dependencies, security, or uptime; consult the service's division of responsibilities.
- A VPS is not necessarily more secure or predictably performant simply because it is isolated. The provider and customer share operational responsibilities; noisy neighbors and resource limits can still exist.
- HTTPS with a valid certificate protects the **connection**, not the business's trustworthiness. Confirm HTTPS redirects and certificate renewal, then check application security separately.

## A deployment checklist

1. Identify output: static HTML/CSS/JS, pre-rendered app, or application requiring a running server.
2. Choose a host that supports the required runtime, environment variables, logs, rollback, and expected traffic.
3. Configure DNS using the host's documented record values. Keep mail-related MX/TXT records intact.
4. Enable HTTPS, redirects, renewal, and secure headers where appropriate. Never expose secret API keys in a client bundle.
5. Use a preview or staging deployment to test forms, routes, assets, and cache headers before production.
6. Record rollback steps, backup responsibilities, and alerting; test restoration when backups are promised.

## Diagnose a broken custom domain

Run `dig example.com A` and `dig example.com AAAA` (if available), compare the authoritative DNS configuration with the platform instructions, and inspect the response with `curl -I https://example.com`. Look for certificate errors, incorrect redirects, missing assets, and wrong MIME types. If the DNS address looks correct but the host serves a different website, inspect the platform's domain mapping and virtual-host configuration rather than repeatedly changing DNS.

## Practice

Deploy a static demo to a preview URL, configure a custom domain in a controlled environment, capture a successful HTTPS response, then document how to roll back a broken deployment. Do not publish real credentials or commit `.env` secrets.

**References:** [MDN: DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS), [MDN: HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS), [web.dev: security](https://web.dev/secure/), [Let's Encrypt: getting started](https://letsencrypt.org/getting-started/).
