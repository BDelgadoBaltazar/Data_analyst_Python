from matplotlib import axes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creo el DataFrame con los datos de productos y precios
data = pd.DataFrame({
    'categoria': ['Electronica', 'Electronica', 'Ropa', 'Ropa', 'Alimentos', 'Alimentos'],
    'producto': ['Televisor', 'Radio', 'Camisa', 'Pantalon', 'Pan', 'Leche'],
    'precio': [300, 150, 20, 40, 2, 1.5]
})

print(data.head())

# Calculo precio promedio por categoria
precio_promedio = data.groupby("categoria")["precio"].mean().reset_index()

# Creo subplots
fig, axes = plt.subplots(1, 2, figsize=(14,6))

# Violin plot - distribucion de precios
sns.violinplot(x="categoria", y="precio", data=data, palette="Set2", ax=axes[0])
axes[0].set_title("Distribucion de precios por categoria")
axes[0].set_xlabel("Categoria")
axes[0].set_ylabel("Precio")

# Grafico de barras - precio promedio
sns.barplot(x="categoria", y="precio", data=precio_promedio, palette="Set2", ax=axes[1])
axes[1].set_title("Precio promedio por categoria")
axes[1].set_xlabel("Categoria")
axes[1].set_ylabel("Precio promedio")

plt.tight_layout()
plt.show()