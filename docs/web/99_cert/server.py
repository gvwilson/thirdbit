"""Certificate server."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl


MESSAGE = bytes("<html><body><p>server message</p></body></html>", "utf-8")
SERVER_ADDRESS = ("", 1443)
CERT_FILE = "server.pem"
KEY_FILE = "server.key"


class RequestHandler(BaseHTTPRequestHandler):
    """Request handler."""

    def do_GET(self):
        """Handle GET requests."""
        self.send_response(int(HTTPStatus.OK))
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(MESSAGE)))
        self.end_headers()
        self.wfile.write(MESSAGE)


def main():
    # If check_hostname is True, only the hostname that matches the certificate
    # will be accepted
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.check_hostname = False
    ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    server = HTTPServer(SERVER_ADDRESS, RequestHandler)
    server.socket = ssl_context.wrap_socket(server.socket, server_side=True)

    print(f"serving at {SERVER_ADDRESS} with certfile {CERT_FILE} and keyfile {KEY_FILE}...")
    server.serve_forever()


if __name__ == "__main__":
    main()
