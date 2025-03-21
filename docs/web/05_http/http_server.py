from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<html><body><p>path: {path}</p></body></html>"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = PAGE.format(path=self.path)
        content = bytes(page, "utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

if __name__ == "__main__":
    server_address = ("localhost", 5000)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
