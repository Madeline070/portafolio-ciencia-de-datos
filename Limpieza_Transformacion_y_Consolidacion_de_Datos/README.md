# Limpieza, Transformación y Consolidación de Datos con Python

## 1. Descripción del proyecto

Este proyecto consiste en preparar y consolidar información de ventas de una empresa de productos de consumo mediante el uso de Python y la biblioteca Pandas.

El objetivo principal fue integrar diferentes fuentes de información en un solo conjunto de datos estructurado, limpio y consistente, listo para utilizarse en análisis exploratorios, consultas SQL, visualizaciones y modelos predictivos.

## 2. Objetivos

- Cargar diferentes tablas de datos utilizando Pandas.
- Examinar la estructura y características de los conjuntos de datos.
- Identificar y tratar valores faltantes.
- Detectar y eliminar registros duplicados.
- Corregir inconsistencias y estandarizar formatos.
- Relacionar diferentes tablas mediante operaciones de unión.
- Generar un conjunto de datos consolidado.
- Exportar la información procesada para su uso posterior.

## 3. Herramientas y tecnologías

- **Python:** lenguaje de programación utilizado para el procesamiento de datos.
- **Pandas:** manipulación, limpieza y transformación de DataFrames.
- **NumPy:** operaciones y manejo de datos numéricos.
- **Jupyter Notebook:** entorno de desarrollo y documentación del proceso.
- **CSV y Excel:** formatos utilizados para almacenar e intercambiar información.

## 4. Conjuntos de datos utilizados

Se trabajó con cinco tablas principales:

| Tabla | Descripción |
|---|---|
| DIM_CATEGORY | Información de categorías de productos. |
| DIM_PRODUCT | Información de productos. |
| DIM_SEGMENT | Información de segmentos. |
| DIM_CALENDAR | Información de fechas y calendario. |
| FACT_SALES | Registros de ventas. |

## 5. Proceso de desarrollo

### Carga y exploración
Se importaron los archivos en DataFrames utilizando Pandas y se revisaron sus características mediante funciones como `head()`, `info()` y `describe()`.

### Limpieza de datos
Se identificaron posibles valores faltantes, registros duplicados e inconsistencias en los conjuntos de datos.

### Transformación
Se estandarizaron formatos y estructuras para garantizar la consistencia de la información.

### Integración de datos
Se realizaron uniones entre las tablas para relacionar productos, categorías, segmentos, calendario y ventas.

### Consolidación y exportación
Se generó un conjunto de datos consolidado y se guardó en formato CSV para utilizarlo en etapas posteriores del análisis.

## 6. Resultados

Como resultado se obtuvo una estructura de datos integrada que permite trabajar con información de ventas desde diferentes dimensiones del negocio.

Esta preparación facilita el análisis del comportamiento comercial, la identificación de patrones y el desarrollo de modelos de predicción.

## 7. Entregable

- Notebook de Jupyter (.ipynb) con los scripts de carga, exploración, limpieza, transformación y consolidación.
- Archivo CSV con el conjunto de datos consolidado.

## 8. Conclusión

La limpieza y consolidación de datos constituye una etapa fundamental dentro del proceso de Ciencia de Datos. Mediante Python y Pandas fue posible organizar e integrar diferentes fuentes de información, preparando una base consistente para realizar análisis posteriores y generar información útil para la toma de decisiones empresariales.
