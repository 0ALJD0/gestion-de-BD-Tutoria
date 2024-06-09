# Sistema de Gestión de Base de Datos

## Autor: Alejandro Arce

Este sistema de gestión de base de datos proporciona una serie de funcionalidades para interactuar con una base de datos Oracle. A continuación se describe la lógica del sistema y sus principales funciones, así como los detalles técnicos del proyecto:

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Base de Datos:** Oracle
- **Librerías y Paquetes Utilizados:**
  - cx_Oracle: Para la conexión con la base de datos Oracle.
  - PyPDF2: Para la generación de archivos PDF.
  - tkinter: Para la interfaz gráfica de usuario.
  
## Funcionalidades

### 1. Generar Consultas

Permite al usuario generar consultas SQL personalizadas. El sistema proporciona una interfaz donde el usuario puede seleccionar las tablas y los atributos que desea consultar.

### 2. Generar Reportes

Permite al usuario generar reportes a partir de las consultas realizadas. Los reportes se generan en formato PDF y pueden incluir información detallada sobre los registros de la base de datos.

### 3. Administrar Usuarios y Roles

Proporciona funcionalidades para administrar usuarios y roles en la base de datos Oracle. El usuario puede crear, modificar y eliminar usuarios, así como asignar y revocar privilegios de usuario.

### 4. Respaldo y Restauración

Permite al usuario realizar respaldo y restauración de la base de datos. El sistema facilita la realización de copias de seguridad periódicas y la restauración de datos en caso de fallos o pérdidas de información.

### 5. Procedimientos Almacenados

Se han desarrollado procedimientos almacenados (CRUD) para todas las entidades de la base de datos. Estos procedimientos se han implementado en un script SQL que se puede ejecutar desde Oracle Developer para generar automáticamente los procedimientos almacenados.

## Menús

El sistema cuenta con los siguientes menús principales:

### 1. Menú de Generar Consultas

Permite al usuario generar consultas personalizadas seleccionando las tablas y los atributos de la base de datos.

### 2. Menú de Generar Reportes

Permite al usuario generar reportes a partir de las consultas realizadas. Los reportes se generan en formato PDF y pueden ser personalizados según las necesidades del usuario.

### 3. Menú de Administración de Usuarios y Roles

Proporciona funcionalidades para administrar usuarios y roles en la base de datos. El usuario puede crear, modificar y eliminar usuarios, así como asignar y revocar privilegios de usuario.

### 4. Menú de Respaldo y Restauración

Permite al usuario realizar respaldo y restauración de la base de datos. El sistema facilita la realización de copias de seguridad periódicas y la restauración de datos en caso de fallos o pérdidas de información.

## Uso del Sistema

Para utilizar el sistema, el usuario puede navegar a través de los diferentes menús utilizando las opciones proporcionadas. Cada menú ofrece una serie de funcionalidades que pueden ser ejecutadas según las necesidades del usuario. Además, se incluye un script SQL con procedimientos almacenados para realizar operaciones CRUD en todas las entidades de la base de datos.

