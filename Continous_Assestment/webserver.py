from http.server import BaseHTTPRequestHandler, HTTPServer

class serverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Webserver Creted Using Python</h1>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
def main():
    PORT = 8000
    server = HTTPServer(('',PORT),serverHandler)
    print("Server running on port ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()