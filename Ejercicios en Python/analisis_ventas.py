import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Cargo dataset
diamonds = sns.load_dataset("diamonds")

print(diamonds.head())

# Resumen estadistico de variables numericas
print(diamonds.describe())

# Grafico de distribucion del precio
sns.histplot(diamonds['price'], bins=50, kde=True)
plt.title("Distribucion de precios de diamantes")
plt.xlabel("Precio (USD)")
plt.ylabel("Frecuencia")
plt.show()

# Grafico de distribucion por color
sns.countplot(x='color', data=diamonds, palette='viridis')
plt.title("Distribucion de diamantes por color")
plt.xlabel("Color")
plt.ylabel("Cantidad de diamantes")
plt.show()