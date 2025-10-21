import crud_academico

db = crud_academico.crud()

class crud_profesor:
    def consultar(self, buscar):
        return db.consultar("SELECT * FROM profesores WHERE nombre LIKE '%" + buscar + "%'")
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO profesores (codigo, nombre, dui, telefono, direccion, correo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (
                datos['codigo'], 
                datos['nombre'], 
                datos['dui'], 
                datos['telefono'], 
                datos['direccion'], 
                datos['correo']
            )
        
        if datos['accion'] == "modificar":
            sql = """
                UPDATE profesores 
                SET codigo=%s, nombre=%s, dui=%s, telefono=%s, direccion=%s, correo=%s
                WHERE idDocente=%s
            """
            valores = (
                datos['codigo'], 
                datos['nombre'], 
                datos['dui'], 
                datos['telefono'], 
                datos['direccion'], 
                datos['correo'], 
                datos['idDocente']
            )
        
        if datos['accion'] == "eliminar":
            sql = "DELETE FROM profesores WHERE idDocente=%s"
            valores = (datos['idDocente'],)
        
        return db.ejecutar(sql, valores)
