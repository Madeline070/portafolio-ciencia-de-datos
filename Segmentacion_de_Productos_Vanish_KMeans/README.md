# Segmentación de Productos Vanish mediante K-Means

## 1. Descripción del proyecto

Este proyecto tiene como objetivo aplicar técnicas de aprendizaje no supervisado para identificar segmentos de productos o regiones relacionados con la marca Vanish, utilizando información histórica de ventas de una empresa de productos de consumo.

Mediante el algoritmo K-Means se busca agrupar elementos con características similares, identificar patrones de comportamiento comercial y detectar oportunidades de mejora en la estrategia de ventas.

## 2. Objetivos

- Analizar los datos relacionados con la marca Vanish.
- Identificar las variables relevantes para la segmentación.
- Preparar y estandarizar los datos.
- Aplicar el algoritmo K-Means.
- Determinar el número óptimo de clusters.
- Identificar patrones y diferencias entre los segmentos.
- Interpretar los resultados para generar recomendaciones comerciales.

## 3. Herramientas y tecnologías

- **Python:** programación y análisis de datos.
- **Pandas:** manipulación de información.
- **NumPy:** operaciones numéricas.
- **Scikit-learn:** implementación de K-Means y StandardScaler.
- **Matplotlib:** visualización de resultados.
- **Seaborn:** análisis gráfico.
- **Jupyter Notebook:** desarrollo y documentación del proyecto.

## 4. Metodología

### Carga y preparación de datos
Se importaron los datos de ventas mediante Pandas y se revisaron las variables disponibles para seleccionar las características relevantes.

### Selección y estandarización de variables
Se eligieron las características necesarias para realizar la segmentación y se aplicó StandardScaler para llevarlas a una escala comparable.

### Aplicación de K-Means
Se implementó el algoritmo K-Means para agrupar productos o regiones con características similares.

### Selección del número óptimo de clusters
Se utilizó el método del codo para comparar diferentes cantidades de clusters y determinar una configuración adecuada para la segmentación.

### Visualización e interpretación
Se generaron gráficos de dispersión, barras y diagramas de caja para analizar los grupos obtenidos e identificar patrones comerciales.

## 5. Resultados e insights

El análisis de clusters permite identificar grupos con diferentes comportamientos de ventas y características comerciales.

La interpretación de los segmentos facilita la identificación de productos o regiones con alto rendimiento, así como aquellos que pueden representar oportunidades de mejora para la marca Vanish.

## 6. Entregables

- Notebook de Jupyter (.ipynb) con el código de implementación.
- Gráficos del método del codo y visualización de clusters.
- Análisis e interpretación de los segmentos identificados.
- Archivo CSV con los resultados de la asignación de clusters, si corresponde.

## 7. Conclusión

La aplicación de K-Means permitió explorar técnicas de aprendizaje no supervisado para segmentar información comercial. Este enfoque ayuda a descubrir patrones que no siempre son evidentes mediante un análisis tradicional y proporciona información útil para orientar estrategias de ventas y oportunidades de crecimiento de la marca Vanish.
