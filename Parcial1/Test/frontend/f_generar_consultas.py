from controllers.generar_consultas_listar import DBManager
from controllers.generar_consultas_reporte import ReportGenerator

def menu_generar_reporte():
    db_manager = DBManager()
    entidades = db_manager.listar_entidades()
    if not entidades:
        print("No se encontraron entidades.")
        return

    consultas = {}
    while True:
        print("Seleccione una opción:")
        print("1. Listar entidades")
        print("2. Listar atributos por entidad")
        print("3. Agregar entidad y atributos a la consulta")
        print("4. Generar reporte")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("Entidades disponibles:", entidades)
        elif opcion == "2":
            entidad = input("Ingrese el nombre de la entidad: ").upper()
            if entidad in entidades:
                atributos = db_manager.listar_atributos(entidad)
                print(f"Atributos de la entidad {entidad}:", atributos)
            else:
                print("Entidad no encontrada.")
        elif opcion == "3":
            entidad = input("Ingrese el nombre de la entidad: ").upper()
            if entidad in entidades:
                atributos_seleccionados = []
                while True:
                    atributos = db_manager.listar_atributos(entidad)
                    print(f"Atributos de la entidad {entidad}:", atributos)
                    atributo = input("Ingrese el nombre del atributo (o '0' para terminar): ").upper()
                    if atributo == "0":
                        break
                    if atributo in atributos:
                        atributos_seleccionados.append(atributo)
                        print(f"Atributo {atributo} agregado.")
                    else:
                        print("Atributo no encontrado.")
                if atributos_seleccionados:
                    consultas[entidad] = atributos_seleccionados
            else:
                print("Entidad no encontrada.")
        elif opcion == "4":
            if consultas:
                report_generator = ReportGenerator(db_manager)
                report_generator.generar_reporte(consultas)
                print("Reporte generado.")
            else:
                print("No hay consultas seleccionadas para generar el reporte.")
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")