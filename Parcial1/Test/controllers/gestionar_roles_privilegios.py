import cx_Oracle

class AdminRolesPrivilegios:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def crear_rol(self, nombre_rol):
        try:
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute(f"CREATE ROLE C##{nombre_rol}")
                self.db_manager.connection.commit()
                print(f"Rol 'C##{nombre_rol}' creado correctamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al crear el rol: {e}")

    def asignar_privilegio(self,nombre_rol):
        while True:
                print("Elija el privilegio:")
                print("1. Asingar privilegio lectura y escritura")
                print("2. Asingar privilegio solo lectura")
                print("3. Asingar privilegio eliminar usuarios")
                print("4. Asingar privilegio crear usuarios")
                print("0. Atrás")

                opcion1 = input("Seleccione una opción: ")
                print(nombre_rol)
                if opcion1 == "1":
                    
                    try:
                        with self.db_manager.connection.cursor() as cursor:
                            cursor.execute(f"GRANT SELECT ANY TABLE TO {nombre_rol}")
                            cursor.execute(f"GRANT INSERT ANY TABLE TO {nombre_rol}")
                            cursor.execute(f"GRANT UPDATE ANY TABLE TO {nombre_rol}")
                            cursor.execute(f"GRANT DELETE ANY TABLE TO {nombre_rol}")
                            self.db_manager.connection.commit()
                            print(f"Privilegio 'lectura y escritura' asignado al rol '{nombre_rol}' correctamente.")
                    except cx_Oracle.DatabaseError as e:
                        print(f"Error al asignar el privilegio: {e}")
                    break
                elif opcion1 == "2":
                    try:
                        with self.db_manager.connection.cursor() as cursor:
                            cursor.execute(f"GRANT SELECT ANY TABLE TO {nombre_rol}")
                            self.db_manager.connection.commit()
                            print(f"Privilegio 'solo lectura' asignado al rol '{nombre_rol}' correctamente.")
                    except cx_Oracle.DatabaseError as e:
                        print(f"Error al asignar el privilegio: {e}")
                    break
                elif opcion1 == "3":
                    try:
                        with self.db_manager.connection.cursor() as cursor:
                            cursor.execute(f"GRANT DROP USER TO {nombre_rol}")
                            self.db_manager.connection.commit()
                            print(f"Privilegio 'eliminar usuarios' asignado al rol '{nombre_rol}' correctamente.")
                    except cx_Oracle.DatabaseError as e:
                        print(f"Error al asignar el privilegio: {e}")
                    break
                elif opcion1 == "4":
                    try:
                        with self.db_manager.connection.cursor() as cursor:
                            cursor.execute(f"GRANT CREATE USER TO {nombre_rol}")
                            self.db_manager.connection.commit()
                            print(f"Privilegio 'crear usuarios' asignado al rol {nombre_rol}' correctamente.")
                    except cx_Oracle.DatabaseError as e:
                        print(f"Error al asignar el privilegio: {e}")
                    break
                elif opcion1 == "0":
                    break   
                else:
                    print("Opción no válida. Inténtelo de nuevo.")

        