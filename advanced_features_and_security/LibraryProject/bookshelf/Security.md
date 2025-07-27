# Security Measures in LibraryProject

- XSS protection via `SECURE_BROWSER_XSS_FILTER`
- CSRF protection via `{% csrf_token %}` and `CSRF_COOKIE_SECURE`
- SQL injection prevented by using Django ORM
- HTTPS-only cookies: `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`
- CSP headers applied using `django-csp`
