import subprocess
#Subprocesses with accessible I/O streams

#This module allows you to spawn processes, connect to their input/output/error pipes, and obtain their return codes.

#For a complete description of this module see the Python documentation.
#
class RespaldoRestauracionDB:
    def __init__(self, username, password, sid):
        self.username = username
        self.password = password
        self.sid = sid

    def respaldar_base_datos(self, ruta_archivo):
        try:
            comando = f"expdp {self.username}/{self.password}@{self.sid} dumpfile={ruta_archivo} full=y"
            subprocess.run(comando, shell=True, check=True)
            print(f"Base de datos respaldada correctamente en '{ruta_archivo}'")
        except subprocess.CalledProcessError as e:
            print(f"Error al realizar el respaldo de la base de datos: {e}")

    def restaurar_base_datos(self, ruta_archivo):
        try:
            comando = f"impdp {self.username}/{self.password}@{self.sid} dumpfile={ruta_archivo} full=y"
            subprocess.run(comando, shell=True, check=True)
            print(f"Base de datos restaurada correctamente desde '{ruta_archivo}'")
        except subprocess.CalledProcessError as e:
            print(f"Error al realizar la restauración de la base de datos: {e}")
