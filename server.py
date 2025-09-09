from http.server import HTTPServer, SimpleHTTPRequestHandler
port = 3000
class miservidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"
            return SimpleHTTPRequestHandler.do_GET(self)

print("Servidor ejecutandose en el puerto 3000",port)       
server = HTTPServer({"localhost",port},miservidor)
server.serve_forever() 