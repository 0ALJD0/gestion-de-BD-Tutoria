from db.conection import OracleDBManager
import cx_Oracle
class DBManager:
    def __init__(self):
        self.db =  OracleDBManager(username='SYSTEM', password='Aljd4183')
        self.db.connect()

    def listar_entidades(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT table_name FROM dba_tables WHERE owner = 'SYSTEM' AND tablespace_name = 'SYSTEM'")
            entidades = [row[0] for row in cursor.fetchall()]
            cursor.close()

            # Formatear entidades como lista
            entidades_formateadas = "\n".join([f"- {entidad}" for entidad in entidades])
            return entidades_formateadas
        except cx_Oracle.Error as e:
            print(f"Error al listar entidades: {e}")
            return "No se pudieron listar las entidades."

    def listar_atributos(self, entidad):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(f"SELECT COLUMN_NAME FROM DBA_TAB_COLUMNS WHERE table_name = '{entidad}'")
            atributos = [row[0] for row in cursor.fetchall()]
            cursor.close()

            # Formatear atributos como lista
            atributos_formateados = "\n".join([f"- {atributo}" for atributo in atributos])
            return atributos_formateados
        except cx_Oracle.Error as e:
            print(f"Error al listar atributos: {e}")
            return "No se pudieron listar los atributos."

    def ejecutar_consulta(self, entidad, atributos):
        try:
            cursor = self.db.connection.cursor()
            query = f"SELECT {', '.join(atributos)} FROM {entidad}"
            cursor.execute(query)
            datos = cursor.fetchall()
            cursor.close()
            return datos
        except cx_Oracle.Error as e:
            print(f"Error al ejecutar consulta: {e}")
            return []