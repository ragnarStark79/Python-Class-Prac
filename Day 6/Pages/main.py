from http.server import HTTPServer, BaseHTTPRequestHandler

class UserHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("index.html", "r", encoding="utf-8") as f:
            self.wfile.write(f.read().encode("utf-8"))
if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8001), UserHandler)
    print("User server running on port 8001")
    server.serve_forever()
