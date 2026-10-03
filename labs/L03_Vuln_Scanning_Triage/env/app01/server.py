#!/usr/bin/env python3
"""Internal application front end.

Serves the files in ./www over HTTP. The Server: response header is set from
SERVER_BANNER so the value lives in one place and is easy to change.
"""
import http.server
import os
import socketserver

PORT = 8080
BANNER = os.environ.get("SERVER_BANNER", "Apache/2.2.14 (Unix)")
ROOT = "/srv/www"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def version_string(self):
        return BANNER

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


class Server(socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with Server(("0.0.0.0", PORT), Handler) as httpd:
        print("serving %s on 0.0.0.0:%d" % (ROOT, PORT), flush=True)
        httpd.serve_forever()
