import cx_Oracle 
class AdminUsuariosRoles:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def crear_usuario(self, username, password):
        try:
            with self.db_manager.connection.cursor() as cursor:
                # Establecer _ORACLE_SCRIPT en true
                cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
                cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
                
                # Crear el usuario
                cursor.execute(f"CREATE USER {username} IDENTIFIED BY {password}")
                cursor.execute(f"GRANT CONNECT TO {username}")
                self.db_manager.connection.commit()
                
                # Verificar si el usuario se ha creado correctamente
                cursor.execute(f"SELECT username FROM DBA_USERS WHERE username = '{username.upper()}'")
                usuario_creado = cursor.fetchone()
                if usuario_creado:
                    print(f"Usuario '{username}' creado correctamente.")
                else:
                    print(f"Error al crear el usuario '{username}'")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al realizar la operación: {e}")

    def modificar_usuario(self, username, new_password):
        if not new_password.isalnum():
            print("La contraseña solo puede contener letras y números.")
            return
        try:
            with self.db_manager.connection.cursor() as cursor:
               # Establecer _ORACLE_SCRIPT en true
                cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=false")
                cursor.execute("ALTER SESSION SET \"_ORACLE_SCRIPT\"=true")
                #cursor.execute("GRANT ALTER USER TO {username}")
                # Modificar la contraseña del usuario
                cursor.execute(f"ALTER USER {username} IDENTIFIED BY {new_password}")
                self.db_manager.connection.commit()
                print(f"Contraseña del usuario '{username}' modificada correctamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al realizar la operación: {e}")

    def eliminar_usuario(self, username):
        try:
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute(f"DROP USER {username} CASCADE")
                self.db_manager.connection.commit()
                print(f"Usuario '{username}' eliminado correctamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error: {e}")

    def asignar_rol_usuario(self, username, role):
        try:
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute(f"GRANT {role} TO {username}")
                self.db_manager.connection.commit()
                print(f"Rol '{role}' asignado al usuario '{username}' correctamente.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error: {e}")

    def consultar_usuarios(self):
        try:
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute("SELECT username FROM DBA_USERS")
                users = cursor.fetchall()
                print("Usuarios:")
                for user in users:
                    print(user[0])
        except cx_Oracle.DatabaseError as e:
            print(f"Error: {e}")

    def consultar_roles(self):
        try:
            with self.db_manager.connection.cursor() as cursor:
                cursor.execute("SELECT role FROM DBA_ROLES")
                roles = cursor.fetchall()
                print("Roles:")
                for role in roles:
                    print(role[0])
        except cx_Oracle.DatabaseError as e:
            print(f"Error: {e}")
