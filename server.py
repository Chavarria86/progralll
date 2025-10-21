from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json
import crud_alumno
import crud_profesor
import crud_login 

port = 3000


crudLogin = crud_login.crud_usuario()
crudAlumno = crud_alumno.crud_alumno()
crudProfesor = crud_profesor.crud_profesor()

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        url_parseada = urlparse(self.path)
        path = url_parseada.path
        parametros = parse_qs(url_parseada.query)

        # Página principal: mostrar login
        if self.path == "/":
            self.path = "login.html"
            return SimpleHTTPRequestHandler.do_GET(self)

        # CRUD de alumnos
        if self.path == "/alumnos":
            alumnos = crudAlumno.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(alumnos).encode('utf-8'))
            return

        # CRUD de profesores
        if self.path == "/profesores":
            profesores = crudProfesor.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(profesores).encode('utf-8'))
            return

        # Vistas dinámicas (formularios)
        if path == "/vistas":
            self.path = '/modulos/' + parametros['form'][0] + '.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        # Cualquier otro archivo (HTML, JS, CSS, etc.)
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        longitud = int(self.headers['Content-Length'])
        datos = self.rfile.read(longitud).decode("utf-8")
        datos = parse.unquote(datos)
        datos = json.loads(datos)

        # 🔐 LOGIN
        if self.path == "/login":
            usuario = datos.get("usuario", "")
            clave = datos.get("clave", "")
            resultado = crudLogin.consultar(usuario, clave)
            if resultado:
                resp = {"ok": True, "msg": "Acceso concedido"}
            else:
                resp = {"ok": False, "msg": "Usuario o clave incorrectos"}
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode("utf-8"))
            return

        # CRUD ALUMNOS
        if "idAlumno" in datos or datos.get("tipo") == "alumno":
            resp = {"msg": crudAlumno.administrar(datos)}
        # CRUD PROFESORES
        elif "idDocente" in datos or datos.get("tipo") == "profesor":
            resp = {"msg": crudProfesor.administrar(datos)}
        # CRUD USUARIOS
        elif "idUsuario" in datos or datos.get("tipo") == "usuario":
            resp = {"msg": crudLogin.administrar(datos)}
        else:
            resp = {"msg": "Entidad no reconocida"}

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode("utf-8"))
        return

print("Servidor ejecutándose en el puerto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()
