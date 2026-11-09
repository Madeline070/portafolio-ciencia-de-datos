# Análisis y Gestión de Datos de Ventas con SQL Server

## 1. Descripción del proyecto

Este proyecto consiste en la creación, administración y consulta de una base de datos relacional para una empresa del sector de productos de consumo, utilizando SQL Server.

El objetivo es organizar la información comercial mediante un modelo de tablas dimensionales y una tabla de hechos, permitiendo integrar y analizar los datos de ventas por categoría, producto, segmento y periodo de tiempo.

## 2. Objetivos

- Crear una base de datos en SQL Server.
- Diseñar y definir la estructura de las tablas.
- Importar los conjuntos de datos proporcionados.
- Verificar la integridad y correcta carga de la información.
- Ejecutar consultas SQL básicas y avanzadas.
- Relacionar tablas mediante operaciones JOIN.
- Obtener información relevante sobre el comportamiento de las ventas.

## 3. Herramientas y tecnologías

- **SQL Server:** sistema de gestión de bases de datos.
- **SQL Server Management Studio (SSMS):** administración y ejecución de consultas.
- **SQL:** lenguaje utilizado para consultar y manipular los datos.

## 4. Estructura de la base de datos

Se trabajó con cinco tablas principales:

| Tabla | Descripción |
|---|---|
| DIM_CATEGORY | Información de categorías. |
| DIM_PRODUCT | Información de productos. |
| DIM_SEGMENT | Información de segmentos. |
| DIM_CALENDAR | Información del calendario. |
| FACT_SALES | Información de las transacciones de ventas. |

## 5. Desarrollo del proyecto

### Creación de la base de datos
Se creó una nueva base de datos en SQL Server para almacenar y administrar la información proporcionada.

### Definición de tablas
Se estableció la estructura de las cinco tablas, considerando sus columnas y tipos de datos.

### Importación de datos
Se cargaron los archivos correspondientes a cada tabla mediante las herramientas de importación de SQL Server.

### Consultas básicas
Se realizaron consultas para comprobar la carga de información, revisar registros y verificar la estructura de las tablas.

### Consultas avanzadas
Se ejecutaron consultas mediante JOIN y otras operaciones SQL para integrar información y analizar las ventas por productos, categorías, segmentos y periodos.

## 6. Resultados

La base de datos permitió organizar la información comercial en una estructura relacional y realizar consultas para obtener información relevante sobre el desempeño de las ventas.

Los registros cargados fueron:

- DIM_CATEGORY: 5 registros.
- DIM_PRODUCT: 505 registros.
- DIM_SEGMENT: 53 registros.
- DIM_CALENDAR: 156 registros.
- FACT_SALES: 122,002 registros.

## 7. Entregables

- Archivo SQL (.sql) con las consultas realizadas.
- Documento PDF con capturas de pantalla del proceso de creación, importación, consultas y resultados.

## 8. Conclusión

El desarrollo de esta práctica permitió aplicar conocimientos de bases de datos relacionales y SQL Server para organizar, integrar y consultar información comercial.

La estructura creada facilita el análisis de ventas y proporciona una base de información para posteriores procesos de visualización, análisis exploratorio y predicción de ventas.
