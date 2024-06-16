import cx_Oracle

class ProcesoComplejo:
    def __init__(self, conexion):
        self.connection = conexion.get_connection()

    def verificar_ninio(self, ci_ninio):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT ID_NINIO FROM NINIO WHERE CI_NINIO = :ci_ninio", {'ci_ninio': ci_ninio})
            result = cursor.fetchone()
            
            cursor.close()
            return result[0] if result else None
        except cx_Oracle.Error as e:
            print("Error al verificar el niño:", e)
            return None

    def obtener_id_ano_lectivo_2024(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT ID_ANO_LECTIVO FROM ANO_LECTIVO WHERE ANO = '2024'")
            result = cursor.fetchone()
            cursor.close()
            result=[21]
            return result[0] if result else None
        except cx_Oracle.Error as e:
            print("Error al obtener el ID del año lectivo 2024:", e)
            return None

    def matricular_ninio(self, id_ninio, id_ano_lectivo):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO MATRICULA (ID_NINIO, ID_ANO_LECTIVO, PRECIO_MATRICULA)
                VALUES (:id_ninio, :id_ano_lectivo, 10)
                """, {'id_ninio': id_ninio, 'id_ano_lectivo': id_ano_lectivo}
            )
            self.connection.commit()
            cursor.close()
            print("Niño matriculado correctamente.")
        except cx_Oracle.Error as e:
            print("Error al matricular el niño:", e)
            self.connection.rollback()
            

    def listar_actividades(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
            cursor.execute("SELECT NOMBRE_AVTIVI FROM ACTIVIDAD")
            actividades = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return actividades
        except cx_Oracle.Error as e:
            print("Error al listar actividades:", e)
            return []

    def obtener_id_actividad(self, nombre_actividad):
        try:
            cursor = self.connection.cursor()
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
            cursor.execute("SELECT ID_ACTIVIDAD FROM ACTIVIDAD WHERE NOMBRE_AVTIVI = :nombre_actividad", {'nombre_actividad': nombre_actividad})
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except cx_Oracle.Error as e:
            print("Error al obtener el ID de la actividad:", e)
            return None

    def registrar_rendimiento(self, id_ninio, id_actividad):
        try:
            cursor = self.connection.cursor()
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
            cursor.execute(
                f"""
                INSERT INTO RENDIMIENTO (ID_NINIO, ID_ACTIVIDAD, ID_TIPO_RENDIMIENT, OBSERVACIONES)
                VALUES ({id_ninio}, {id_actividad}, 2, 'Sin Observaciones')
                """
            )
            self.connection.commit()
            cursor.close()
            print("Registrado correctamente.")
        except cx_Oracle.Error as e:
            print("Error al registrar el rendimiento:", e)
            self.connection.rollback()

    def proceso_complejo(self, ci_ninio):
        try:
            # Inicio de la transacción
            self.connection.begin()

            # Verificar la existencia del niño
            id_ninio = self.verificar_ninio(ci_ninio)
            if not id_ninio:
                print("El niño no existe. Por favor, ingrese una cédula válida.")
                return

            # Obtener el ID del año lectivo 2024
            #id_ano_lectivo = self.obtener_id_ano_lectivo_2024()
            #print(id_ano_lectivo)
            #if not id_ano_lectivo:
            #    print("No se encontró el año lectivo 2024.")
            #    return
            
            # Matricular al niño
            #self.matricular_ninio(id_ninio, 21)
            print(f"Niño matriculado con CI: {ci_ninio} correctamente en año lectivo 2024")
            # Listar actividades y solicitar al usuario que seleccione una
            while True:
                actividades = self.listar_actividades()
                if not actividades:
                    print("No hay actividades disponibles.")
                    return

                print("Escriba la actividad a la que quiera registrar al niño")
                print("Actividades disponibles:")
                for actividad in actividades:
                    print(actividad)

                nombre_actividad = input("Ingrese el nombre de la actividad para registrar al niño (o 0 para regresar): ")
                if nombre_actividad == '0':
                    print("Regresando al menú anterior...")
                    return

                id_actividad = self.obtener_id_actividad(nombre_actividad)
                if not id_actividad:
                    print("Actividad no encontrada. Por favor, ingrese un nombre válido.")
                    continue

                # Registrar rendimiento
                self.registrar_rendimiento(id_ninio, id_actividad)

                # Confirmar la transacción
                self.connection.commit()
                print("Proceso completado exitosamente.")
                return
        except cx_Oracle.Error as e:
            print("Error durante el proceso complejo:", e)
            self.connection.rollback()
