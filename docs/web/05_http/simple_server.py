"""Basic socket server."""

import socketserver


CHUNK_SIZE = 1024
SERVER_ADDRESS = ("localhost", 5000)


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(CHUNK_SIZE)
        cli = self.client_address[0]
        msg = f"server received {len(data)} bytes from {cli}"
        print(msg)
        print(data)
        self.request.sendall(bytes(msg, "utf-8"))


if __name__ == "__main__":
    server = socketserver.TCPServer(SERVER_ADDRESS, MyHandler)
    server.serve_forever()
