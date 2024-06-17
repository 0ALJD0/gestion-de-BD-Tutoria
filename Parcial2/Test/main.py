from db.conexion import ConexionDB
from interfaces.interfaz_generacion_disparadores import MenuGeneracionDisparadores
from interfaces.interfaz_cursores_automatizacion import MenuCursoresAutomatizacion
from interfaces.interfaz_comparacion_consultas import MenuComparacionConsultas
from interfaces.interfaz_visualizacion_logs import MenuVisualizacionLogs

def menu_principal():
    print("Bienvenido al sistema")
    print("1. Generación de disparadores de auditoria")
    print("2. Cursores y automatización")
    print("3. Comparación de consultas aplicando hilos")
    print("4. Visualización de logs y auditoría")
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
            elif opcion == '2':
                menu_automatizacion = MenuCursoresAutomatizacion(conexion)
                menu_automatizacion.ejecutar()
            elif opcion == '3':
                menu_comparacion = MenuComparacionConsultas(conexion)
                menu_comparacion.ejecutar()
            elif opcion == '4':
                menu_logs = MenuVisualizacionLogs(conexion)
                menu_logs.ejecutar()
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
