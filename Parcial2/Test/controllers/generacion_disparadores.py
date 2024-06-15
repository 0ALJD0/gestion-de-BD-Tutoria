import cx_Oracle
import os
class GeneracionDisparadores:
    def __init__(self, conexion):
        self.connection = conexion.get_connection()

    def listar_entidades_y_atributos(self):
        entidades = {}
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT table_name FROM dba_tables WHERE owner = 'SYSTEM' AND tablespace_name = 'SYSTEM'")
            for row in cursor.fetchall():
                table_name = row[0]
                cursor.execute("SELECT column_name, data_type FROM all_tab_columns WHERE table_name = :table_name AND owner = 'SYSTEM'", {'table_name': table_name})
                atributos = cursor.fetchall()
                entidades[table_name] = atributos
            cursor.close()
        except cx_Oracle.Error as e:
            print("Error al listar entidades y atributos:", e)
        return entidades

    def crear_tabla_auditoria(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
            cursor.execute(
                """
                    DECLARE
                        tabla_existe NUMBER;
                    BEGIN
                        -- Verifica si la tabla existe
                        SELECT COUNT(*)
                        INTO tabla_existe
                        FROM all_tables
                        WHERE table_name = 'AUDITORIA' AND owner = 'SYSTEM';

                        -- Si la tabla existe, la elimina
                        IF tabla_existe > 0 THEN
                            EXECUTE IMMEDIATE 'DROP TABLE AUDITORIA';
                        END IF;
                    END;

                """
            )
            cursor.execute("""
            CREATE TABLE AUDITORIA (
                ID NUMBER GENERATED AS IDENTITY PRIMARY KEY,
                NOMBRE_TABLA_AFECTADA VARCHAR2(100) NOT NULL,
                FECHA_HORA TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                USUARIO_ACTUAL VARCHAR2(50) NOT NULL,
                DETALLE_ACCION VARCHAR2(4000) NOT NULL
            )
            """)
            cursor.close()
            print("Tabla AUDITORIA creada correctamente")
        except cx_Oracle.Error as e:
            print("Error al crear la tabla AUDITORIA:", e)

    def generar_disparadores_entidad(self, entidad):
        try:
            entidad=entidad.upper()
            cursor = self.connection.cursor()
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
            cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
            cursor.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name = '{entidad}' AND owner = 'SYSTEM'")
            columnas = [row[0] for row in cursor.fetchall()]
            columnas_str = ", ".join(columnas)
            insert=f"""
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_INSERT
            AFTER INSERT ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                    'Inserto el nuevo dato con el ID: ' || :NEW.ID_{entidad});
            END;
            """
            update=f"""
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_UPDATE
            AFTER UPDATE ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                    'Actualizo el dato con el ID: ' || :NEW.ID_{entidad});
            END;
            """
            delete=f"""
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_DELETE
            AFTER DELETE ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                     'Se eliminó la fila con el ID' || :OLD.ID_{entidad});
            END;
            """
            plantilla_disparadores = f"""
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_INSERT
            AFTER INSERT ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                    'Inserto el nuevo dato con el ID: ' || :NEW.ID_{entidad});
            END;
            /
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_UPDATE
            AFTER UPDATE ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                    'Actualizo el dato con el ID: ' || :NEW.ID_{entidad});
            END;
            /
            CREATE OR REPLACE TRIGGER {entidad}_AFTER_DELETE
            AFTER DELETE ON {entidad}
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('{entidad}', USER, SYSTIMESTAMP,
                    'Se eliminó la fila con el ID' || :OLD.ID_{entidad});
            END;
            /
            """

            # Ejecutar la plantilla de disparadores en la base de datos
            cursor.execute(insert)
            self.connection.commit()  # Confirmar los cambios en la base de datos
            cursor.execute(update)
            self.connection.commit()
            cursor.execute(delete)
            self.connection.commit()

            # Guardar la plantilla en un archivo SQL
            nombre_archivo = f"{entidad}_disparadores.sql"
            self.guardar_plantilla_en_archivo(nombre_archivo, plantilla_disparadores)
             # Ejecutar el archivo SQL mediante sqlplus
            #self.ejecutar_sqlplus('SYSTEM', 'Aljd4183', 'XE', nombre_archivo)
            
            cursor.close()

            print(f"Disparadores para la entidad {entidad} generados y aplicados correctamente")
        except cx_Oracle.Error as e:
            print(f"Error al generar disparadores para la entidad {entidad}: {e}")


    def guardar_plantilla_en_archivo(self, nombre_archivo, contenido):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)

    def ejecutar_sqlplus(self, username, password, database, archivo_sql):
            comando = f"sqlplus {username}/{password}@{database} @{archivo_sql}"
            os.system(comando)