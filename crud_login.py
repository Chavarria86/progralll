import crud_academico

db = crud_academico.crud()

class crud_usuario:
    def consultar(self, buscar):
       
        sql = "SELECT * FROM usuarios WHERE nombre LIKE '%" + buscar + "%' OR usuario LIKE '%" + buscar + "%'"
        return db.consultar(sql)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'])

        elif datos['accion'] == "modificar":
            sql = """
                UPDATE usuarios 
                SET usuario=%s, clave=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idUsuario=%s
            """
            valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'], datos['idUsuario'])

        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM usuarios WHERE idUsuario=%s"
            valores = (datos['idUsuario'],)

        else:
            return "Acción no reconocida"

        return db.ejecutar(sql, valores)
