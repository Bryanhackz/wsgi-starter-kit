from security.headers import get_security_headers
from handlers import pages, static

ROUTES = {
    "/": pages.render_index,
    "/health": pages.health_check,
}

def application(environ: dict, start_response: callable) -> list[bytes]:
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")

    response_headers = []
    
    if method != "GET":
        status, content_type, body = "405 Method Not Allowed", "text/plain", "Method Not Allowed"
    else:
        if path in ROUTES:
            status, content_type, body = ROUTES[path]()
        else:
            static_result = static.serve_static(path)
            if static_result:
                status, content_type, body = static_result
            else:
                status, content_type, body = pages.not_found()

    response_headers.append(("Content-Type", content_type))
    
    for header, value in get_security_headers().items():
        response_headers.append((header, value))

    body_bytes = body.encode("utf-8") if isinstance(body, str) else body

    start_response(status, response_headers)
    return [body_bytes]