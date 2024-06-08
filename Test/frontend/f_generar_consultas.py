from controllers.generar_consultas import Listar, ReportGenerator

def menu_generar_reporte(db_manager):
    report_generator = ReportGenerator(db_manager)

    while True:
        print("Seleccione una opción:")
        print("1. Listar entidades")
        print("2. Generar reporte")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            entidades = Listar.listar_entidades()
            if not entidades:
                print("No se encontraron entidades.")
                continue

            print("Entidades disponibles:")
            for entidad in entidades:
                print(f"- {entidad}")

            while True:
                entidad_seleccionada = input("Ingrese el nombre de la entidad (o '0' para volver al menú principal): ").strip().upper()
                if entidad_seleccionada == "0":
                    break
                if entidad_seleccionada not in entidades:
                    print("Entidad no válida, intente nuevamente.")
                    continue

                atributos = Listar.listar_atributos(entidad_seleccionada)
                if not atributos:
                    print(f"No se encontraron atributos para la entidad '{entidad_seleccionada}'.")
                    continue

                print(f"Atributos disponibles en la entidad '{entidad_seleccionada}':")
                for atributo in atributos:
                    print(f"- {atributo}")

                atributos_seleccionados = []
                while True:
                    atributo = input("Ingrese el nombre del atributo (o '0' para volver a la selección de entidades): ").strip().upper()
                    if atributo == "0":
                        break
                    if atributo not in atributos:
                        print("Atributo no válido, intente nuevamente.")
                        continue
                    atributos_seleccionados.append(atributo)
                    agregar_mas = input("¿Desea agregar otro atributo de esta entidad? (s/n): ").strip().lower()
                    if agregar_mas != "s":
                        break

                if atributos_seleccionados:
                    report_generator.agregar_consulta(entidad_seleccionada, atributos_seleccionados)
                    print(f"Atributos {atributos_seleccionados} de la entidad '{entidad_seleccionada}' agregados al reporte.")

        elif opcion == "2":
            report_generator.generar_reporte()

        elif opcion == "0":
            break

        else:
            print("Opción no válida, intente nuevamente.")