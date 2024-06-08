from controllers.Admi_Users_Rol import AdminUsuariosRoles
from frontend.f_roles_privilegios import asignar_privilegio_rol
def AdminitrarUsariosRoles(db_manager):
    admin = AdminUsuariosRoles(db_manager)

    while True:
        print("Seleccione una opción:")
        print("1. Crear un usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Crear un rol")
        print("5. Asignar un rol a un usuario")
        print("6. Consultar los usuarios creados")
        print("7. Consultar los roles creados")
        print("0. Volver al menú principal")

        opcion = input("Opción: ")

        if opcion == "1":
            username = input("Ingrese el nombre del nuevo usuario: ").strip()
            password = input("Ingrese la contraseña del nuevo usuario: ").strip()
            admin.crear_usuario(username, password)
        elif opcion == "2":
            username = input("Ingrese el nombre del usuario a modificar: ").strip()
            new_password = input("Ingrese la nueva contraseña: ").strip()
            admin.modificar_usuario(username, new_password)
        elif opcion == "3":
            username = input("Ingrese el nombre del usuario a eliminar: ").strip()
            admin.eliminar_usuario(username)
        elif opcion == "4":
            asignar_privilegio_rol(db_manager)
        elif opcion == "5":
            username = input("Ingrese el nombre del usuario: ").strip()
            role = input("Ingrese el nombre del rol: ").strip()
            admin.asignar_rol_usuario(username, role)
        elif opcion == "6":
            admin.consultar_usuarios()
        elif opcion == "7":
            admin.consultar_roles()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")