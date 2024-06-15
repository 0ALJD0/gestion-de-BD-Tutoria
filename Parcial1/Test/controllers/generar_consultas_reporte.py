from fpdf import FPDF

class ReportGenerator:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def generar_reporte(self, consultas):
        pdf = FPDF()
        pdf.set_title('Reporte de Base de Datos')
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        # Agregar título
        pdf.cell(200, 10, txt='Reporte de Base de Datos', ln=True, align='C')
        pdf.ln(10)  # Espacio después del título
        
        pdf.set_font("Arial", size=12)

        for entidad, atributos in consultas.items():
            # Agregar entidad
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt=f"Entidad: {entidad}", ln=True, align='L')
            pdf.ln(5)  # Espacio después de la entidad
            
            # Generar encabezado de la tabla
            pdf.set_fill_color(200, 220, 255)
            pdf.set_font("Arial", 'B', 10)
            
            # Calcular el ancho de cada columna basado en el contenido
            column_widths = [pdf.get_string_width(atributo) + 10 for atributo in atributos]
            
            for idx, atributo in enumerate(atributos):
                pdf.cell(column_widths[idx], 10, atributo, 1, 0, 'C', 1)
            pdf.ln()

            # Obtener y mostrar datos
            datos = self.db_manager.ejecutar_consulta(entidad, atributos)
            pdf.set_font("Arial", size=10)
            if datos:
                for row in datos:
                    for idx, cell in enumerate(row):
                        cell_text = str(cell)
                        cell_width = pdf.get_string_width(cell_text) + 10
                        if cell_width > column_widths[idx]:
                            column_widths[idx] = cell_width
                        
                        pdf.cell(column_widths[idx], 10, cell_text, 1)
                    pdf.ln()
            else:
                pdf.cell(200, 10, txt="No se encontraron datos.", ln=True, align='L')

            pdf.ln(10)  # Espacio después de cada tabla

        pdf.output("reporte.pdf")
        print("Reporte PDF generado exitosamente.")
