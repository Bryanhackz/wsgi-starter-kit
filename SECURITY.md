# Security Policy

## Supported Versions
Currently, only the latest `main` branch is supported.

## Scope
This project is a foundational HTTP server built on WSGI. Its security posture focuses on HTTP response headers (CSP, HSTS, X-Frame-Options), path traversal prevention in static file serving, and Server-Side Rendering (SSR) safety. It is intended to be the base for internet-facing applications.

## Reporting a Vulnerability
Please do not report security vulnerabilities through public GitHub issues. Send an email to **br4yangil006@gmail.com**. You should receive a response within 48 hours.

Please include:
- Type of issue (e.g., path traversal, header injection, XSS via SSR)
- Full paths of source file(s) related to the issue
- Step-by-step instructions to reproduce the issue
- Impact of the issue
