import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='orclpdb1')

try:
    connection = cx_Oracle.connect(user='your_username', password='your_password', dsn=dsn_tns)
    cursor = connection.cursor()
    cursor.execute("SELECT SYS_CONTEXT('USERENV', 'DB_NAME') FROM DUAL")
    db_name = cursor.fetchone()[0]
    print(f"Conectado exitosamente a la base de datos: {db_name}")
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print(f"Error al conectar a la base de datos: {error.message}")
    exit(1)

