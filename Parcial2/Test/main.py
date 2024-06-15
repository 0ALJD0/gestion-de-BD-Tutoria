from db.conexion import ConexionDB
from interfaces.interfaz_generacion_disparadores import MenuGeneracionDisparadores

def menu_principal():
    print("Bienvenido al sistema")
    print("1. Generación de disparadores de auditoria")
    print("0. Salir")

def ejecutar_menu_principal():
    conexion = ConexionDB()
    if conexion.conectar():
        while True:
            menu_principal()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                menu_disparadores = MenuGeneracionDisparadores(conexion)
                menu_disparadores.ejecutar()
            elif opcion == '0':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, intente nuevamente.")
        conexion.desconectar()
    else:
        print("No se pudo establecer la conexión con la base de datos.")

if __name__ == "__main__":
    ejecutar_menu_principal()
