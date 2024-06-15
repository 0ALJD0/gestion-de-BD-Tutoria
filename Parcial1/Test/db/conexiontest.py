import cx_Oracle

class OracleDBConnection:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(
                user='SYSTEM',
                password='Aljd4183',
                dsn='localhost:1521/xe'
            )
            print(f"Conectado a la base de datos: {self.connection.version}")
        except cx_Oracle.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            try:
                self.connection.close()
                print("Conexión a la base de datos cerrada.")
            except cx_Oracle.Error as e:
                print(f"Error al cerrar la conexión a la base de datos: {e}")
