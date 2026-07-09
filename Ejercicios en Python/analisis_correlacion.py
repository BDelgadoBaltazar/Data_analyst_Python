import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Cargo dataset
df = sns.load_dataset("diamonds")

# Filtro por color F y corte Premium
subset = df[(df["color"] == "F") & (df["cut"] == "Premium")]

# Calculo correlacion entre precio y quilates
correlacion = subset["price"].corr(subset["carat"])
print("Correlacion entre precio y quilates (color F, corte Premium):", correlacion)

# Grafico de dispersion
sns.scatterplot(x="carat", y="price", data=subset, alpha=0.6, color="blue")
plt.title("Relacion entre quilates y precio (color F, corte Premium)")
plt.xlabel("Quilates")
plt.ylabel("Precio")
plt.show()