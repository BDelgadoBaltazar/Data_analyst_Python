import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Cargo dataset
titanic = sns.load_dataset("titanic")

print(titanic.head())

# Calculo tasa de supervivencia por clase
supervivencia_por_clase = titanic.groupby("pclass")["survived"].mean().reset_index()

print(supervivencia_por_clase)

# Grafico de barras
sns.barplot(x="pclass", y="survived", data=supervivencia_por_clase, palette="viridis")
plt.title("Tasa de supervivencia por clase de pasajero")
plt.xlabel("Clase de pasajero")
plt.ylabel("Tasa de supervivencia")
plt.ylim(0,1) # Escala de 0 a 1 para mostrar proporciones
plt.show()

# Boxplot de edad vs supervivencia
sns.boxplot(x="survived", y="age", data=titanic, palette="Set2")
plt.title("Distribucion de edades segun supervivencia")
plt.xlabel("Supervivencia (0 = No, 1 = Si)")
plt.ylabel("Edad")
plt.show()