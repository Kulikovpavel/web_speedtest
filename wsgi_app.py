from time import sleep


def app(environ, start_response):
    data = b"ok"
    start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))])
    if environ["PATH_INFO"] == "/delay":
        sleep(0.3)
    return iter([data])
