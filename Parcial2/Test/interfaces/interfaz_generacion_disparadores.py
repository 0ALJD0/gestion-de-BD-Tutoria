from controllers.generacion_disparadores import GeneracionDisparadores

class MenuGeneracionDisparadores:
    def __init__(self, conexion):
        self.generador = GeneracionDisparadores(conexion)

    def menu_auditoria(self):
        print("1. Listar entidades con atributos")
        print("2. Crear tabla de Auditoria")
        print("3. Generar disparadores de una entidad")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.menu_auditoria()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                entidades_y_atributos = self.generador.listar_entidades_y_atributos()
                for entidad, atributos in entidades_y_atributos.items():
                    print(f"Entidad: {entidad}")
                    for atributo in atributos:
                        print(f"  - {atributo[0]} ({atributo[1]})")
            elif opcion == '2':
                self.generador.crear_tabla_auditoria()
            elif opcion == '3':
                entidad = input("Ingrese el nombre de la entidad: ")
                self.generador.generar_disparadores_entidad(entidad)
            elif opcion == '0':
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida, intente nuevamente.")
