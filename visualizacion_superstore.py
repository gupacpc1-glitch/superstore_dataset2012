# ==========================================================
# ACTIVIDAD:
# Visualización de datos con Pandas, Matplotlib y Seaborn
# Dataset: superstore_dataset2012.csv
# ==========================================================

# ===============================
# Importación de bibliotecas
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# ===============================
# Cargar Dataset
# ===============================

df = pd.read_csv(r"C:\Users\guipa\OneDrive\Desktop\programación\proyecto\superstore_dataset2012.csv", encoding="latin1")

print("="*60)
print("Primeras filas")
print(df.head())

print("="*60)
print("Información del dataset")
print(df.info())

print("="*60)
print("Valores nulos")
print(df.isnull().sum())

# ==========================================================
# PREPARACIÓN DE LOS DATOS
# ==========================================================

# Convertir fecha si existe

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"])

# ==========================================================
# IDENTIFICAR NOMBRES DE COLUMNAS
# (para que funcione con distintas versiones del dataset)
# ==========================================================

print("\nColumnas disponibles:\n")
print(df.columns)

# Variables numéricas

ventas = "Sales"
beneficio = "Profit"

# Variables categóricas

categoria = "Category"
segmento = "Segment"

# ==========================================================
# 1. VISUALIZACIÓN UNIVARIANTE CON MATPLOTLIB
# Histograma de ventas
# ==========================================================

plt.figure(figsize=(10,6))

plt.hist(df[ventas], bins=30, color="steelblue", edgecolor="black")

plt.title("Distribución de Ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")

# Conclusión:
# La mayoría de las ventas corresponden a montos pequeños.

plt.savefig("histograma_ventas.png")

plt.show()

# ==========================================================
# 2. VISUALIZACIÓN UNIVARIANTE CON SEABORN
# Boxplot
# ==========================================================

plt.figure(figsize=(10,6))

sns.boxplot(data=df,
            x=categoria,
            y=ventas,
            palette="Set2")

plt.title("Distribución de Ventas por Categoría")

# Conclusión:
# Existen valores atípicos en las ventas.

plt.show()

# ==========================================================
# 3. GRÁFICO BIVARIANTE CON MATPLOTLIB
# Dispersión Ventas vs Beneficio
# ==========================================================

plt.figure(figsize=(10,6))

plt.scatter(df[ventas],
            df[beneficio],
            alpha=0.5,
            color="green")

plt.title("Ventas vs Beneficio")
plt.xlabel("Ventas")
plt.ylabel("Beneficio")

# Conclusión:
# Generalmente mayores ventas producen mayores beneficios,
# aunque existen ventas con pérdidas.

plt.show()

# ==========================================================
# 4. GRÁFICO BIVARIANTE CON SEABORN
# Regresión
# ==========================================================

plt.figure(figsize=(10,6))

sns.regplot(
    data=df,
    x=ventas,
    y=beneficio,
    scatter_kws={"alpha":0.4},
    line_kws={"color":"red"}
)

plt.title("Relación entre Ventas y Beneficios")

# Conclusión:
# Existe una correlación positiva entre ambas variables.

plt.show()

# ==========================================================
# 5. VISUALIZACIÓN MULTIVARIANTE
# Heatmap
# ==========================================================

plt.figure(figsize=(8,6))

variables = df.select_dtypes(include="number")

correlacion = variables.corr()

sns.heatmap(
    correlacion,
    annot=True,
    cmap="coolwarm",
    linewidths=.5
)

plt.title("Mapa de Calor de Correlaciones")

# Conclusión:
# Permite identificar relaciones entre variables numéricas.

plt.show()

# ==========================================================
# 6. SUBPLOTS
# ==========================================================

fig, ax = plt.subplots(2,2, figsize=(16,10))

# Histograma

ax[0,0].hist(df[ventas],
             bins=30,
             color="skyblue",
             edgecolor="black")

ax[0,0].set_title("Histograma de Ventas")

# Barras

conteo = df[categoria].value_counts()

ax[0,1].bar(conteo.index,
            conteo.values,
            color="orange")

ax[0,1].set_title("Cantidad por Categoría")

# Scatter

ax[1,0].scatter(df[ventas],
                df[beneficio],
                alpha=0.4,
                color="green")

ax[1,0].set_title("Ventas vs Beneficio")

# Boxplot

sns.boxplot(
    data=df,
    x=categoria,
    y=ventas,
    ax=ax[1,1],
    palette="Set3"
)

ax[1,1].set_title("Ventas por Categoría")

plt.suptitle("Análisis General del Dataset Superstore", fontsize=18)

plt.tight_layout()

plt.show()

# ==========================================================
# RESUMEN FINAL
# ==========================================================

print("="*60)
print("ANÁLISIS COMPLETADO")
print("="*60)

print("""
Conclusiones:

1. Las ventas presentan una distribución sesgada hacia valores pequeños.

2. Existen valores atípicos (outliers) importantes en las ventas.

3. La relación entre ventas y beneficio es positiva, aunque no todas
las ventas generan ganancias.

4. Las categorías presentan diferentes distribuciones de ventas.

5. El mapa de calor permite identificar las correlaciones entre las
variables numéricas.

6. Se guardó el histograma como:
   histograma_ventas.png
""")