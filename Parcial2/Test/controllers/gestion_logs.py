# controllers/gestion_logs.py

import cx_Oracle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class GestorLogs:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_logs(self):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT OS_USERNAME AS USUARIO_OS, USERNAME AS USUARIO, TIMESTAMP AS FECHA, ACTION_NAME AS TIPO_ACCION, COMMENT_TEXT AS COMENTARIO FROM DBA_AUDIT_TRAIL")
            logs = cursor.fetchall()
            cursor.close()
            return logs
        except cx_Oracle.Error as e:
            print("Error al obtener los logs:", e)
            return []

    def obtener_usuarios(self):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT DISTINCT USERNAME FROM DBA_AUDIT_TRAIL")
            usuarios = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return usuarios
        except cx_Oracle.Error as e:
            print("Error al obtener los usuarios:", e)
            return []

    def obtener_acciones(self):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT DISTINCT ACTION_NAME FROM DBA_AUDIT_TRAIL")
            acciones = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return acciones
        except cx_Oracle.Error as e:
            print("Error al obtener las acciones:", e)
            return []

    def filtrar_logs_por_usuario(self, usuario):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT OS_USERNAME AS USUARIO_OS, USERNAME AS USUARIO, TIMESTAMP AS FECHA, ACTION_NAME AS TIPO_ACCION, COMMENT_TEXT AS COMENTARIO FROM DBA_AUDIT_TRAIL WHERE USERNAME = :usuario", usuario=usuario)
            logs = cursor.fetchall()
            cursor.close()
            return logs
        except cx_Oracle.Error as e:
            print("Error al filtrar logs por usuario:", e)
            return []

    def filtrar_logs_por_accion(self, accion):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT OS_USERNAME AS USUARIO_OS, USERNAME AS USUARIO, TIMESTAMP AS FECHA, ACTION_NAME AS TIPO_ACCION, COMMENT_TEXT AS COMENTARIO FROM DBA_AUDIT_TRAIL WHERE ACTION_NAME = :accion", accion=accion)
            logs = cursor.fetchall()
            cursor.close()
            return logs
        except cx_Oracle.Error as e:
            print("Error al filtrar logs por acción:", e)
            return []

    def filtrar_logs_por_usuario_y_accion(self, usuario, accion):
        try:
            cursor = self.conexion.connection.cursor()
            cursor.execute("SELECT OS_USERNAME AS USUARIO_OS, USERNAME AS USUARIO, TIMESTAMP AS FECHA, ACTION_NAME AS TIPO_ACCION, COMMENT_TEXT AS COMENTARIO FROM DBA_AUDIT_TRAIL WHERE USERNAME = :usuario AND ACTION_NAME = :accion", usuario=usuario, accion=accion)
            logs = cursor.fetchall()
            cursor.close()
            return logs
        except cx_Oracle.Error as e:
            print("Error al filtrar logs por usuario y acción:", e)
            return []
        
    def mostrar_logs_formateados(self, logs):
        if not logs:
            print("No se encontraron logs para los filtros aplicados.")
            return

        headers = ["USUARIO_OS", "USUARIO", "FECHA", "TIPO DE ACCIÓN", "COMENTARIO"]
        column_widths = [max(len(str(row[i])) for row in logs) for i in range(len(headers))]
        column_widths = [max(column_widths[i], len(headers[i])) for i in range(len(headers))]

        def format_row(row):
            return " | ".join(str(cell).ljust(column_widths[i]) for i, cell in enumerate(row))

        header_row = " | ".join(headers[i].ljust(column_widths[i]) for i in range(len(headers)))
        print(header_row)
        print("-" * len(header_row))
        for log in logs:
            print(format_row(log))

    def generar_pdf(self, logs):
        doc = SimpleDocTemplate("informe_logs.pdf", pagesize=letter)
        elements = []

        headers = ["OS_USERNAME", "USERNAME", "TIMESTAMP", "ACTION_NAME", "OBJ_NAME"]
        data = [headers] + logs

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        doc.build(elements)