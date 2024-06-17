# interfaces/interfaz_visualizacion_logs.py

from controllers.gestion_logs import GestorLogs

class MenuVisualizacionLogs:
    def __init__(self, conexion):
        self.conexion = conexion
        self.gestor_logs = GestorLogs(self.conexion)

    def ejecutar(self):
        while True:
            print("Menú de Visualización de Logs y Auditoría")
            print("1. Ver todos los logs")
            print("2. Filtrar por Usuario")
            print("3. Filtrar por Acción")
            print("4. Filtrar por Usuario y Acción")
            print("0. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.mostrar_todos_los_logs()
            elif opcion == '2':
                self.filtrar_por_usuario()
            elif opcion == '3':
                self.filtrar_por_accion()
            elif opcion == '4':
                self.filtrar_por_usuario_y_accion()
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente nuevamente.")
    
    def mostrar_todos_los_logs(self):
        logs = self.gestor_logs.obtener_logs()
        self.gestor_logs.mostrar_logs_formateados(logs)
        self.opcion_generar_pdf(logs)

    def filtrar_por_usuario(self):
        usuarios = self.gestor_logs.obtener_usuarios()
        print("Usuarios disponibles:")
        for usuario in usuarios:
            print(usuario)
        usuario_seleccionado = input("Ingrese el nombre de usuario para filtrar: ")
        logs = self.gestor_logs.filtrar_logs_por_usuario(usuario_seleccionado)
        self.gestor_logs.mostrar_logs_formateados(logs)
        self.opcion_generar_pdf(logs)

    def filtrar_por_accion(self):
        acciones = self.gestor_logs.obtener_acciones()
        print("Acciones disponibles:")
        for accion in acciones:
            print(accion)
        accion_seleccionada = input("Ingrese el nombre de la acción para filtrar: ")
        logs = self.gestor_logs.filtrar_logs_por_accion(accion_seleccionada)
        self.gestor_logs.mostrar_logs_formateados(logs)
        self.opcion_generar_pdf(logs)

    def filtrar_por_usuario_y_accion(self):
        usuarios = self.gestor_logs.obtener_usuarios()
        print("Usuarios disponibles:")
        for usuario in usuarios:
            print(usuario)
        usuario_seleccionado = input("Ingrese el nombre de usuario para filtrar: ")

        acciones = self.gestor_logs.obtener_acciones()
        print("Acciones disponibles:")
        for accion in acciones:
            print(accion)
        accion_seleccionada = input("Ingrese el nombre de la acción para filtrar: ")

        logs = self.gestor_logs.filtrar_logs_por_usuario_y_accion(usuario_seleccionado, accion_seleccionada)
        self.gestor_logs.mostrar_logs_formateados(logs)
        self.opcion_generar_pdf(logs)

    def opcion_generar_pdf(self, logs):
        while True:
            opcion = input("¿Desea generar un informe PDF de los logs filtrados? (s/n): ")
            if opcion.lower() == 's':
                self.gestor_logs.generar_pdf(logs)
                print("Informe PDF generado con éxito.")
                break
            elif opcion.lower() == 'n':
                break
            else:
                print("Opción no válida, intente nuevamente.")
