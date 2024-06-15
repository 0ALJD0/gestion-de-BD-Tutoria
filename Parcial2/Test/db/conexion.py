import cx_Oracle

class ConexionDB:
    def __init__(self, user="SYSTEM", password="Aljd4183", dsn="localhost:1521/xe"):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.connection = None

    def conectar(self):
        try:
            self.connection = cx_Oracle.connect(self.user, self.password, self.dsn)
            print("Base de datos conectada correctamente")
            return True
        except cx_Oracle.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def get_connection(self):
        return self.connection
