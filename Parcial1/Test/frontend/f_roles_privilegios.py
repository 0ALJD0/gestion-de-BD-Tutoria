from controllers.gestionar_roles_privilegios import AdminRolesPrivilegios
def asignar_privilegio_rol(db_manager):
    admin_roles = AdminRolesPrivilegios(db_manager)

    while True:
        print("\nCrear Rol o Asignar Privilegio:")
        print("1. Crear un rol")
        print("2. Asignar un privilegio")
        print("0. Atrás")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_rol = input("Ingrese el nombre del nuevo rol: ").strip()
            admin_roles.crear_rol(nombre_rol)
        elif opcion == "2":
            nombre_rol = input("Ingrese el nombre del rol al que asignar el privilegio: ").strip()
            admin_roles.asignar_privilegio(nombre_rol)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")