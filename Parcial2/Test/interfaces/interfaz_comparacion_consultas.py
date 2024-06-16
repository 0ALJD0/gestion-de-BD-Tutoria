from controllers.comparacion_consultas import ComparacionConsultas
from controllers.generacion_disparadores import GeneracionDisparadores

class MenuComparacionConsultas:
    def __init__(self, conexion):
        self.comparador = ComparacionConsultas(conexion)
        self.generador = GeneracionDisparadores(conexion)

    def menu_comparacion(self):
        print("1. Listar entidades y atributos")
        print("2. Ejecutar consultas en paralelo")
        print("0. Regresar al menú principal")

    def ejecutar(self):
        while True:
            self.menu_comparacion()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.listar_entidades_y_atributos()
            elif opcion == '2':
                self.ejecutar_comparacion()
            elif opcion == '0':
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

    def listar_entidades_y_atributos(self):
        entidades_y_atributos = self.generador.listar_entidades_y_atributos()
        for entidad, atributos in entidades_y_atributos.items():
            print(f"Entidad: {entidad}")
            for atributo in atributos:
                print(f"  - {atributo[0]} ({atributo[1]})")

    def ejecutar_comparacion(self):
        entidades_y_atributos = self.generador.listar_entidades_y_atributos()
        queries = []

        while True:
            entidad_seleccionada = self.seleccionar_entidad(entidades_y_atributos)
            if entidad_seleccionada is None:
                break
            atributos_seleccionados = self.seleccionar_atributos(entidades_y_atributos, entidad_seleccionada)
            if atributos_seleccionados:
                query = self.construir_consulta(entidad_seleccionada, atributos_seleccionados)
                queries.append(query)
        
        if queries:
            self.comparador.ejecutar_consultas_en_hilos(queries)

    def seleccionar_entidad(self, entidades_y_atributos):
        while True:
            print("Seleccione una entidad:")
            for i, entidad in enumerate(entidades_y_atributos.keys(), 1):
                print(f"{i}. {entidad}")
            print("0. Terminar selección de entidades")
            opcion = input("Ingrese el número de la entidad: ")
            if opcion == '0':
                return None
            if opcion.isdigit() and 1 <= int(opcion) <= len(entidades_y_atributos):
                return list(entidades_y_atributos.keys())[int(opcion) - 1]
            else:
                print("Opción no válida, intente nuevamente.")

    def seleccionar_atributos(self, entidades_y_atributos, entidad):
        atributos = entidades_y_atributos[entidad]
        seleccionados = []
        while True:
            print("Seleccione los atributos (ingrese '0' para terminar):")
            for i, atributo in enumerate(atributos, 1):
                print(f"{i}. {atributo[0]} ({atributo[1]})")
            opcion = input("Ingrese el número del atributo: ")
            if opcion == '0':
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(atributos):
                seleccionado = atributos[int(opcion) - 1][0]
                if seleccionado not in seleccionados:
                    seleccionados.append(seleccionado)
            else:
                print("Opción no válida, intente nuevamente.")
        return seleccionados

    def construir_consulta(self, entidad, atributos):
        select_clause = ', '.join(atributos)
        query = f"SELECT {select_clause} FROM {entidad}"
        return query
