# Este código crea un archivo .ipynb listo con todas las visualizaciones, explicaciones y comentarios
import nbformat as nbf

# Crear un notebook
nb = nbf.v4.new_notebook()

# Celdas del notebook
celdas = [
    nbf.v4.new_markdown_cell('# Análisis Exploratorio de Datos (EDA) de Ventas\n\nEste notebook realiza un EDA completo del dataset de ventas, con visualizaciones y documentación de insights.'),
    nbf.v4.new_code_cell('''# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10,6)'''),
    nbf.v4.new_markdown_cell('## 1️⃣ Cargar los datos'),
    nbf.v4.new_code_cell('''# Cargar dataset de ventas
ventas = pd.read_csv("/data/ventas.csv")

# Información básica
ventas.head()
ventas.info()
ventas.describe()'''),
    nbf.v4.new_markdown_cell('## 2️⃣ Variables clave\n- Fecha: para análisis temporal\n- Producto / Categoría: para segmentación\n- Región: para análisis geográfico\n- Cantidad / Ventas: valores numéricos principales'),
    nbf.v4.new_code_cell('ventas.columns'),
    nbf.v4.new_markdown_cell('## 3️⃣ Distribución de ventas'),
    nbf.v4.new_code_cell('''# Histograma de ventas
sns.histplot(ventas["Ventas"], bins=30, kde=True)
plt.title("Distribución de ventas")
plt.xlabel("Monto de ventas")
plt.ylabel("Frecuencia")
plt.show()

# Boxplot por categoría
sns.boxplot(x="Categoría", y="Ventas", data=ventas)
plt.title("Distribución de ventas por categoría")
plt.xticks(rotation=45)
plt.show()'''),
    nbf.v4.new_markdown_cell('### Insights:\n- Algunas categorías tienen ventas muy altas comparadas con otras.\n- Posibles outliers en ciertas categorías que podrían requerir análisis adicional.'),
    nbf.v4.new_markdown_cell('## 4️⃣ Tendencia de ventas en el tiempo'),
    nbf.v4.new_code_cell('''# Convertir fecha a datetime
ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])

# Ventas totales por mes
ventas_mensuales = ventas.groupby(ventas["Fecha"].dt.to_period("M"))["Ventas"].sum().reset_index()
ventas_mensuales["Fecha"] = ventas_mensuales["Fecha"].dt.to_timestamp()

# Gráfico de línea
sns.lineplot(x="Fecha", y="Ventas", data=ventas_mensuales)
plt.title("Tendencia de ventas totales por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.show()

# Tendencia por región
sns.lineplot(x="Fecha", y="Ventas", hue="Región", data=ventas)
plt.title("Tendencia de ventas por región")
plt.show()'''),
    nbf.v4.new_markdown_cell('### Insights:\n- Se observan picos de ventas en ciertos meses, posiblemente temporadas altas.\n- La región X muestra consistentemente mayores ventas que otras regiones.'),
    nbf.v4.new_markdown_cell('## 5️⃣ Relación entre variables'),
    nbf.v4.new_code_cell('''# Scatterplot entre cantidad y ventas por categoría
sns.scatterplot(x="Cantidad", y="Ventas", hue="Categoría", data=ventas)
plt.title("Relación entre cantidad y ventas por categoría")
plt.show()'''),
    nbf.v4.new_markdown_cell('### Insights:\n- Relación positiva entre cantidad vendida y monto de ventas.\n- Algunas categorías tienen ventas altas incluso con pocas unidades vendidas, indicando productos de alto valor.'),
    nbf.v4.new_markdown_cell('## 6️⃣ Distribución geográfica de ventas'),
    nbf.v4.new_code_cell('''ventas_por_region = ventas.groupby("Región")["Ventas"].sum().sort_values(ascending=False)

# Barras
ventas_por_region.plot(kind="bar")
plt.title("Ventas totales por región")
plt.ylabel("Ventas")
plt.show()'''),
    nbf.v4.new_markdown_cell('### Insights:\n- Región con mayor rendimiento y regiones con menor desempeño.\n- Posibles oportunidades de crecimiento en regiones con ventas bajas.'),
    nbf.v4.new_markdown_cell('## 7️⃣ Identificación de valores atípicos'),
    nbf.v4.new_code_cell('''sns.boxplot(x="Región", y="Ventas", data=ventas)
plt.title("Valores atípicos de ventas por región")
plt.xticks(rotation=45)
plt.show()'''),
    nbf.v4.new_markdown_cell('### Insights:\n- Se observan ventas inusualmente altas en ciertas regiones, que podrían requerir revisión o explicación.'),
    nbf.v4.new_markdown_cell('## 8️⃣ Guardar visualizaciones'),
    nbf.v4.new_code_cell('''# Ejemplo de guardado de gráfico
plt.figure()
ventas_por_region.plot(kind="bar")
plt.title("Ventas totales por región")
plt.ylabel("Ventas")
plt.savefig("ventas_por_region.png", dpi=300, bbox_inches='tight')'''),
    nbf.v4.new_markdown_cell('## ✅ Conclusión\n- Se exploró la distribución de ventas, tendencias temporales y relaciones entre variables.\n- Se identificaron outliers y regiones/productos con desempeño destacado.\n- Todas las visualizaciones están listas para incluirse en reportes o dashboards.')
]

# Añadir celdas al notebook
nb['cells'] = celdas

# Guardar el notebook
with open('EDA_Ventas.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook EDA_Ventas.ipynb generado exitosamente.")
