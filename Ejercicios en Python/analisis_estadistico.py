import seaborn as sns
import matplotlib.pyplot as plt

# Cargo dataset
penguins = sns.load_dataset("penguins")

# Grafico de caja (boxplot) para distribucion de pesos por especie
sns.boxplot(x="species", y="body_mass_g", data=penguins, palette="Set2")
plt.title("Distribucion del peso de los pingüinos segun especie")
plt.xlabel("Especie")
plt.ylabel("Peso corporal (g)")
plt.show()

# Grafico de distribucion de la longitud del pico
sns.histplot(data=penguins, x="bill_length_mm", hue="species", kde=True, palette="Set2")
plt.title("Distribucion de la longitud del pico por especie")
plt.xlabel("Longitud del pico (mm)")
plt.ylabel("Frecuencia")
plt.show()

# Grafico de distribucion de la longitud de la aleta
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", kde=True, palette="Set2")
plt.title("Distribucion de la longitud de la aleta por especie")
plt.xlabel("Longitud de la aleta (mm)")
plt.ylabel("Frecuencia")
plt.show()

# a. Distribucion de ejemplares por sexo segun ubicacion
sns.countplot(x="island", hue="sex", data=penguins, palette="Set2")
plt.title("Distribucion de pingüinos por sexo en cada isla")
plt.xlabel("Isla")
plt.ylabel("Cantidad de ejemplares")
plt.show()

# b. Distribucion de ejemplares por especie segun ubicacion
sns.countplot(x="island", hue="species", data=penguins, palette="Set1")
plt.title("Distribucion de pingüinos por especie en cada isla")
plt.xlabel("Isla")
plt.ylabel("Cantidad de ejemplares")
plt.show()

# c. Desafio: distribucion por especie y sexo segun ubicacion
sns.catplot(x="island", hue="sex", col="species", kind="count", data=penguins, palette="Set3")
plt.subplots_adjust(top=0.85)
plt.suptitle("Distribucion de pingüinos por especie y sexo en cada isla")
plt.show()

# Selecciono solo variables numericas
numericas = penguins[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]

# Calculo matriz de correlacion
corr_matrix = numericas.corr()

# Visualizo con heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlacion de caracteristicas de pingüinos")
plt.show()

# a. Mayor correlacion: peso vs longitud de la aleta
sns.scatterplot(x="flipper_length_mm", y="body_mass_g", hue="species", data=penguins, palette="Set2")
sns.regplot(x="flipper_length_mm", y="body_mass_g", data=penguins, scatter=False, color="black")
plt.title("Mayor correlacion: Peso vs Longitud de la aleta")
plt.xlabel("Longitud de la aleta (mm)")
plt.ylabel("Peso corporal (g)")
plt.show()

# b. Menor correlacion: longitud del pico vs profundidad del pico
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", hue="species", data=penguins, palette="Set1")
sns.regplot(x="bill_length_mm", y="bill_depth_mm", data=penguins, scatter=False, color="black")
plt.title("Menor correlacion: Longitud vs Profundidad del pico")
plt.xlabel("Longitud del pico (mm)")
plt.ylabel("Profundidad del pico (mm)")
plt.show()