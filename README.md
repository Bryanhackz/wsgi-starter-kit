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