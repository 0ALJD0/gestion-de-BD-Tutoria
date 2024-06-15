from controllers.cursores_automatizacion import CursoresAutomatizacion

class MenuCursoresAutomatizacion:
    def __init__(self, conexion):
        self.automatizacion = CursoresAutomatizacion(conexion)

    def menu_automatizacion(self):
        print("1. Matricular niño y registrar actividad")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.menu_automatizacion()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                cedula = input("Ingrese la cédula del niño: ")
                self.automatizacion.matricular_y_registrar_actividad(cedula)
            elif opcion == '0':
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida, intente nuevamente.")
