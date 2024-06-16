import threading
import time
import cx_Oracle

class ComparacionConsultas:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar_consultas_en_hilos(self, queries):
        threads = []
        results = []

        for query in queries:
            thread = threading.Thread(target=self.ejecutar_consulta, args=(query, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for result in results:
            print(result)

    def ejecutar_consulta(self, query, results):
        try:
            cursor = self.conexion.get_cursor()
            start_time = time.time()
            cursor.execute(query)
            fetched_data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            end_time = time.time()
            elapsed_time = end_time - start_time
            cursor.close()

            # Determinamos el ancho máximo de cada columna
            col_widths = [len(col_name) for col_name in column_names]
            for row in fetched_data:
                for i, value in enumerate(row):
                    col_widths[i] = max(col_widths[i], len(str(value)))

            # Construimos el string del resultado alineado
            result_string = f'Consulta "{query}" ejecutada en {elapsed_time:.6f} segundos.\n'
            result_string += " | ".join(col_name.ljust(col_widths[i]) for i, col_name in enumerate(column_names)) + "\n"
            for row in fetched_data:
                result_string += " | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row)) + "\n"
            
            results.append(result_string)
        except cx_Oracle.Error as e:
            results.append(f"Error al ejecutar la consulta \"{query}\": {e}")
