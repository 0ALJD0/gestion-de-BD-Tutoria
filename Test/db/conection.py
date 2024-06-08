import cx_Oracle

class OracleDBManager:
    def __init__(self, username, password, host='localhost', port=1521, sid='xe'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.sid = sid
        self.connection = None

    def connect(self):
        dsn_tns = cx_Oracle.makedsn(self.host, self.port, sid=self.sid)
        try:
            self.connection = cx_Oracle.connect(user=self.username, password=self.password, dsn=dsn_tns)
            print(f"Conectado exitosamente a la base de datos: {self.username, self.password, dsn_tns}")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error al conectar a la base de datos: {error.message}")
            exit(1)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Desconectado de la base de datos")
