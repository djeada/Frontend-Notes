# Web Hosting Explained

A website on your computer is not automatically reachable by other people. **Hosting** makes its files or application available over a network; **DNS** helps browsers find the hostname's destination; **HTTPS** protects communication between client and server. These are different concerns, and publishing a page requires checking each one.

## Domain name

A domain such as `example.com` is a human-readable name. DNS resolves that name to records, which can provide an IP address or another hostname. `192.0.2.1` is a documentation-only example address, not a suggested production hosting address. A domain does not itself store your site, and a single domain may resolve to multiple addresses.

### Why register a domain?

- Choose a memorable name that represents the project and works well when spoken or typed.
- A custom domain gives you control over the name across hosting migrations **as long as you maintain its registration and DNS**.
- Branding and relevant content may help people recognize your site, but a keyword in the name does not by itself guarantee higher search rankings or make a site trustworthy.

### Registering a domain

A registrar registers names for a renewable term under a registry's rules; registration is not permanent ownership. Check the first-year **and renewal** price, transfer policy, WHOIS/privacy options where applicable, domain lock, two-factor authentication, and renewal reminders. A low introductory hosting price is not the same thing as a domain registration price.

Providers to compare (listed as examples, not endorsements or verified price offers):

| Provider | Site | Services to check |
| --- | --- | --- |
| Domain.com | [domain.com](https://www.domain.com/) | Registration and hosting; compare separate renewal terms. |
| Bluehost | [bluehost.com](https://www.bluehost.com/) | Hosting, WordPress and domain options. |
| HostGator | [hostgator.com](https://www.hostgator.com/) | Shared/VPS hosting and domain options. |
| GoDaddy | [godaddy.com](https://www.godaddy.com/) | Registration, DNS, hosting and email. |
| Namecheap | [namecheap.com](https://www.namecheap.com/) | Registration, DNS and hosting. |

The old table displayed unverified starting monthly hosting prices alongside a section about domain registration. Promotions, taxes, renewal costs, term lengths and included features change: obtain current figures from each provider's checkout before making a decision.

## Hosting

### Worked deployment: a static HTML/CSS/JavaScript site

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

**Hands-on exercise:** deliberately rename `styles.css` to `missing.css` in a throwaway copy and inspect the 404. Repair the link, deploy to a preview target you control, and test a direct refresh of any deep route. This is a genuine network behavior change even though the HTML source itself may look unchanged. Reference: [MDN publishing your website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website).


There are different hosting models, and the word *managed* describes the division of operational responsibility, not necessarily whether a plan is free or whether it runs a particular framework.

### Managed hosting

A managed provider operates some infrastructure and may supply deployments, TLS certificates, rollbacks, monitoring, backups, or automatic updates. **Exactly which responsibilities are included depends on the service and plan.** You still own application code, access controls, secret handling, content, and any duties the provider's shared-responsibility terms assign to you.

**Advantages:** less server administration; integration with Git; sometimes global content delivery, preview environments and support.

**Tradeoffs:** platform-specific deployment behavior; runtime/build limits; limits or charges for usage; some loss of low-level configuration control. Free tiers may exist but are not universal or guaranteed over time.

Examples:

- [Netlify](https://www.netlify.com/): deployment and hosting for web sites and supported application functions.
- [Vercel](https://vercel.com/): frontend-oriented deployment, including supported framework and function runtimes.
- [GitHub Pages](https://pages.github.com/): static site hosting from a repository; **not a general-purpose Node.js backend host**.

A static site often needs only built HTML, CSS, JavaScript and image assets. Server-rendered applications or API routes need a platform with a supported runtime. Read the build command, output directory and environment-variable documentation before selecting one.

### Virtual private server (VPS)

A VPS provides a virtual machine with an allocated amount of compute, memory and storage. Depending on the provider and plan, you may control the operating system and server software. Isolation and performance depend on the virtualization, host contention, resource limits and configuration; a VPS does **not guarantee** consistent performance or immunity from neighboring workloads.

**Advantages:** control over runtime, web server, logging, scheduled jobs and deployment approach; adjustable resources on many platforms.

**Tradeoffs:** you may be responsible for operating-system patches, user permissions, firewall, TLS renewal, intrusion monitoring, backups and restoration. A VPS is not automatically cheaper than managed hosting once administration time is included.

Examples worth comparing: [Vultr](https://www.vultr.com/), [Hostinger VPS](https://www.hostinger.com/vps-hosting), [GoDaddy VPS](https://www.godaddy.com/hosting/vps). Review region, bandwidth billing, support, backup/restore, and managed versus unmanaged responsibility for the specific plan.

### Deployment: from Git to a live site

#### Production release and rollback checklist

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

**Exercise:** describe how you would recover if the homepage loads but all CSS files return 404 after release. Identify the symptom in Network, correct the deployment path, and verify cache headers without assuming a DNS failure. Reference: [OWASP deployment and maintenance](https://owasp.org/www-project-developer-guide/).


A Git push does not automatically deploy every site: **deployment must be configured**, and many teams only deploy production from a protected branch after reviews and checks.

1. **Identify the application type.** A static site might publish `dist/`; a server application may need an image or executable plus a running process.
2. **Build locally.** Read `package.json` scripts or the project's README; run its tests and build instead of assuming every repository uses `npm run build`.
3. **Configure the host.** Connect the appropriate repository and branch, or set up your own CI deployment credentials. Set its build command, runtime version, output folder, route/fallback rules, and deployment region as required.
4. **Set secrets on the server/platform.** Never commit private API keys to the repository or bundle them into public browser JavaScript. Browser-exposed environment variables are not secret.
5. **Deploy a preview.** Check navigation and deep links, static assets, API calls, error pages, keyboard interaction, mobile layout, and browser console/network errors.
6. **Release deliberately.** Confirm production domain, run migrations when applicable, and know how to roll back. An automatic deployment is not always instantaneous or error-free.
7. **Operate.** Monitor uptime, errors, certificates, resource usage and backups. Practice restoration; a backup you cannot restore is not a reliable recovery plan.

## Connecting a domain to hosting

### Diagnose the complete chain with commands and observations

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

**Troubleshooting exercise:** distinguish these cases: `dig` returns the old address; `dig` returns the new address but TLS fails; the homepage loads but the SPA's deep route 404s; the API responds with 403. Each points to a different layer and needs a different fix. See the [protocols request diagram](../assets/diagrams/request-lifecycle.svg).


The record type depends on **what your host actually instructs you to configure**. Do not invent an IP address or create a conflicting record simply because a tutorial says every deployment needs an `A` record.

1. In your hosting dashboard, add the intended custom domain (for example, `www.example.com`) and read the provider's exact DNS instructions.
2. Determine which DNS provider is **authoritative** for your domain. DNS settings may live with a separate provider, not the registrar.
3. Add the required records: `A` maps a hostname to an IPv4 address, `AAAA` maps to IPv6, and `CNAME` aliases one hostname to another where allowed. Some DNS providers support `ALIAS`/`ANAME` or CNAME flattening at the zone apex; these are provider-specific conveniences, not interchangeable standard record types. `MX` is for mail routing, and `TXT` commonly conveys verification or mail-policy information; do not overwrite existing mail records when setting up a website.
4. Check for conflicting records on the same name and configure any `www` ↔ apex redirect deliberately. Avoid routing a domain to two unrelated hosting services accidentally.
5. Verify records and HTTPS. Request a certificate through the hosting provider or configure one yourself and test the final hostname over `https://`.
6. Wait for cached DNS answers to expire according to their time-to-live (**TTL**) and resolver behavior. There is **no universal 48-hour propagation period**: an authoritative change may be available quickly while prior answers remain cached until their TTL, and some changes take longer for other operational reasons.

![From a browser request through DNS and HTTPS to a server response](../assets/diagrams/request-lifecycle.svg)

**Practical check:** a DNS lookup such as `dig example.com A` checks an IPv4 response, while `dig www.example.com CNAME` checks a possible alias. Not every valid site needs both. Then use browser DevTools → Network to inspect the HTTPS request and response; verify that a deep route reloads rather than returning a hosting 404. See the detailed [protocols chapter](08_protocols.md) for DNS, TLS, caching and HTTP semantics.

**Before changing production DNS:** document existing records, reduce the relevant TTL in advance *if useful and permitted*, identify what can be rolled back, and preserve mail settings. Domain configuration errors can disrupt website **or email** even when deployment code is correct.

## DIY: home server hosting

A home server can teach operating systems, networking, and deployment, but it introduces reliability, privacy, and security responsibilities. Prefer a throwaway learning service without personal data before exposing a real application to the public Internet.

### Advantages

1. Learn server installation, reverse proxies, network routes, logging and monitoring firsthand.
2. Reuse available hardware for experimentation while accounting for electricity, backups, bandwidth and time.
3. Control hardware and operating system within the limits of your internet provider and router.

### Challenges

1. Consumer connections and electricity may be less reliable; traffic and hardware failure need recovery plans.
2. Public ports expose software to unsolicited traffic. Patch promptly, use least-privilege accounts, and do not expose administrative interfaces without protection.
3. Hardware, upload bandwidth and storage may be constrained; a small device does not automatically mean poor performance for every static site.
4. Some home connections use dynamic IP addresses, carrier-grade NAT (CGNAT), or ISP restrictions that prevent inbound public connections. Dynamic DNS handles changing address records but **does not bypass CGNAT**.
5. Hosting can expose your home IP and create privacy and operational risks that a hosted platform would handle differently.

### Educational setup

1. Choose hardware and a maintained server operating system appropriate to it. For Raspberry Pi, consult [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/); do not rely on outdated distribution names or unsupported releases.
2. Install and update the OS. Create a non-root administrator account with secure authentication.
3. Install a web server or reverse proxy, such as [Apache HTTP Server](https://httpd.apache.org/) or [Nginx](https://nginx.org/), and confirm it serves an innocuous page on the local network **before** making it public.
4. Verify whether your ISP supplies reachable public addressing. If you plan public access, understand router forwarding, firewall rules, and IPv6 as applicable. Avoid forwarding SSH/admin interfaces merely to get a website working.
5. Set up HTTPS and certificate renewal; separate application secrets from browser assets; arrange updates, monitoring, backup and restore.
6. Publish only when the security and operational plan is adequate for your use case. A VPN or managed tunnel can be more suitable for a private personal lab, depending on its trust model.

### Troubleshooting by layer

| Symptom | Investigate |
| --- | --- |
| DNS lookup returns the old address | Authoritative nameservers, record and TTL/caches. |
| Domain resolves but connection fails | Host/service availability, routing, firewall, required port. |
| Browser warns about HTTPS | Certificate hostname, expiry, provisioning and redirects. |
| Homepage works but reloading `/about` returns 404 | Static host routing or SPA fallback configuration. |
| Page loads but API call fails | Browser Network tab, API URL, CORS, authentication and server logs. |
| New CSS does not appear | Deployment artifact, browser/CDN cache, cache headers and versioned assets. |

**References:** [MDN: DNS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name), [MDN: publishing a website](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website), [Cloudflare: DNS record types](https://www.cloudflare.com/learning/dns/dns-records/), [Let's Encrypt](https://letsencrypt.org/).