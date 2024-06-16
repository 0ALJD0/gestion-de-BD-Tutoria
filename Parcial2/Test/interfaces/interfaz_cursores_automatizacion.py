from controllers.cursores_automatizacion import ProcesoComplejo

class MenuCursoresAutomatizacion:
    def __init__(self, conexion):
        self.automatizacion = ProcesoComplejo(conexion)

    def menu_automatizacion(self):
        print("1. Matricular niño y registrar actividad")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.menu_automatizacion()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                cedula = input("Ingrese la cédula del niño: ")
                self.automatizacion.proceso_complejo(cedula)
            elif opcion == '0':
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida, intente nuevamente.")
