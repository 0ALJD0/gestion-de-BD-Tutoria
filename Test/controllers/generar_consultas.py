import cx_Oracle
from fpdf import FPDF

class Listar:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def listar_entidades(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT table_name FROM dba_tables WHERE owner= 'SYSTEM' AND tablespace_name= 'SYSTEM'")
                entidades = [row[0] for row in cursor.fetchall()]
            return entidades
        except cx_Oracle.DatabaseError as e:
            print(f"Error al listar entidades: {e}")
            return []
    def listar_atributos(self, entidad):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT column_name FROM DBA_TAB_COLUMNS WHERE table_name= '{entidad}'")
                atributos = [row[0] for row in cursor.fetchall()]
            return atributos
        except cx_Oracle.DatabaseError as e:
            print(f"Error al listar atributos para la entidad '{entidad}': {e}")
            return []

class ReportGenerator:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.consulta = {}

    def agregar_consulta(self, entidad, atributos):
        if entidad in self.consulta:
            self.consulta[entidad].extend(atributos)
        else:
            self.consulta[entidad] = atributos

    def generar_reporte(self):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt="Reporte de Base de Datos", ln=True, align='C')

            for entidad, atributos in self.consulta.items():
                pdf.cell(200, 10, txt=f"Entidad: {entidad}", ln=True)
                pdf.cell(200, 10, txt="Atributos:", ln=True)
                for atributo in atributos:
                    pdf.cell(200, 10, txt=f"- {atributo}", ln=True)

            pdf.output("reporte.pdf")
            print("Reporte generado exitosamente en 'reporte.pdf'")
        except Exception as e:
            print(f"Error al generar el reporte: {e}")