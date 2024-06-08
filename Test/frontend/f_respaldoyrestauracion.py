from controllers.respaldo_restauracion import RespaldoRestauracionDB
def menu_respaldo_restauracion(db_manager):
    respaldo_restauracion = RespaldoRestauracionDB(username=db_manager.username, password=db_manager.password, sid=db_manager.sid)

    while True:
        print("Seleccione una opción:")
        print("1. Respaldar la base de datos")
        print("2. Restaurar la base de datos desde un archivo")
        print("0. Volver al menú principal")

        opcion = input("Opción: ")

        if opcion == "1":
            ruta_archivo = input("Ingrese la ruta donde guardar el respaldo: ").strip()
            respaldo_restauracion.respaldar_base_datos(ruta_archivo)
        elif opcion == "2":
            ruta_archivo = input("Ingrese la ruta del archivo de respaldo: ").strip()
            respaldo_restauracion.restaurar_base_datos(ruta_archivo)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
