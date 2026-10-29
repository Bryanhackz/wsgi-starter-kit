# WSGI Starter Kit

## Problem
Starting a new web project from scratch usually means setting up frameworks, dependencies, and security boilerplates. This introduces bloat and often results in inconsistent security practices.

## Solution
A minimalist, zero-dependency starter kit based on Python's standard `wsgiref`. It provides a secure, single-threaded baseline with strict HTTP security headers (CSP, HSTS, etc.) injected at the router level, and Server-Side Rendering (SSR) out of the box.

## Stack
- Python 3.11+
- `wsgiref`, `json`, `os`
- No external dependencies.

## Setup
```bash
python server.py
```
Open `http://localhost:8000` in your browser.

## Architectural decisions
- **No third-party frameworks:** The standard library is more than capable of serving HTTP requests securely. By avoiding Flask/Django, the surface area for vulnerabilities is dramatically reduced.
- **Security headers at the router level:** By applying headers centrally in `router.py`, it is impossible for a developer to accidentally deploy a route without a strict Content-Security-Policy.
- **SSR over static files:** Serving HTML through Python allows for dynamic variable injection (like `{{APP_NAME}}`), which is necessary for the upcoming i18n and SEO requirements.

- ## Content Security Policy (CSP) Rationale

This starter kit enforces a strict Content Security Policy by default. Here is the justification for the chosen directives:

- `default-src 'self'`: Denies everything by default unless explicitly allowed.
- `script-src 'self'`: Prevents inline scripts (`<script>...</script>`) and XSS injection.
- `style-src 'self'`: Prevents inline styles and relies entirely on external CSS files.
- `img-src 'self' data:`: The `data:` URI is explicitly permitted to allow for inline SVG icons and small base64 placeholders, reducing unnecessary HTTP requests in a starter kit context.
- `connect-src 'self'`: Restricts `fetch()` and `XMLHttpRequest` to the same origin.
- `frame-ancestors 'none'`: Prevents clickjacking by disabling iframe embedding.
- `object-src 'none'`: Disables legacy plugins like Flash.
- `upgrade-insecure-requests`: Forces browsers to automatically upgrade any HTTP subresource requests (images, scripts) to HTTPS, complementing the HSTS header.

### Future Production Considerations
- **`report-uri` / `report-to`**: Currently omitted. In a production environment, an endpoint should be configured to collect CSP violation reports (via a service like Sentry or a custom backend endpoint).
- **`worker-src` / `manifest-src`**: Currently inherited from `default-src 'self'`. If this kit is extended to include Progressive Web App (PWA) manifests or Web Workers, these directives should be explicitly reviewed.
