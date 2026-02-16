from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class InlineDemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/inline", "/inline.html"):
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        file_path = os.path.join(os.path.dirname(__file__), "inline.html")
        with open(file_path, "r", encoding="utf-8") as f:
            self.wfile.write(f.read().encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8010), InlineDemoHandler)
    print("Inline demo server running on http://localhost:8010")
    server.serve_forever()
