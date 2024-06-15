from db.conection import OracleDBManager
from frontend.f_respaldoyrestauracion import menu_respaldo_restauracion
from frontend.f_adminuser_roles import AdminitrarUsariosRoles
from frontend.f_generar_consultas import menu_generar_reporte

def main():
    db_manager = OracleDBManager(username='SYSTEM', password='Aljd4183')
    db_manager.connect()
    while True:
        print("Seleccione una opción:")
        print("1. Gestionar usuarios y roles")
        print("2. Respaldo y restauración de la base de datos")
        print('3. Generar Reporte')
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            AdminitrarUsariosRoles(db_manager)
        elif opcion == "2":
            menu_respaldo_restauracion(db_manager)
        elif opcion == "3":
            menu_generar_reporte()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


    db_manager.disconnect()

if __name__ == "__main__":
    main()
