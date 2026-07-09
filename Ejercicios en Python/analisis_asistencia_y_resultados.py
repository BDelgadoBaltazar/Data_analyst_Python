import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargo los archivos CSV
talleres = pd.read_csv("talleres.csv")
participantes = pd.read_csv("participantes.csv")
resultados = pd.read_csv("resultados_taller.csv")

# Exploro el DataFrame de talleres
print("Talleres - Informacion general")
print(talleres.info())
print("\nPrimeras filas:")
print(talleres.head())
print("\nEstadisticas descriptivas:")
print(talleres.describe(include="all"))

# Exploro el DataFrame de participantes
print("\nParticipantes - Informacion general")
print(participantes.info())
print("\nPrimeras filas:")
print(participantes.head())
print("\nEstadisticas descriptivas:")
print(participantes.describe(include="all"))

# Exploro el DataFrame de resultados
print("\nResultados - Informacion general")
print(resultados.info())
print("\nPrimeras filas:")
print(resultados.head())
print("\nEstadisticas descriptivas:")
print(resultados.describe(include="all"))

# --- Talleres ---
# Elimino duplicados
talleres = talleres.drop_duplicates()

# Manejo valores nulos (si hubiera)
talleres = talleres.dropna()

# --- Participantes ---
participantes = participantes.drop_duplicates()
participantes = participantes.dropna()

# Convierto Edad a numerico
participantes["Edad"] = pd.to_numeric(participantes["Edad"], errors="coerce")

# --- Resultados ---
resultados = resultados.drop_duplicates()
resultados = resultados.dropna()

# Convierto columna Asistió a tipo booleano
resultados["Asistió"] = resultados["Asistió"].astype(bool)

# Convierto Puntaje a numerico (float)
resultados["Puntaje"] = pd.to_numeric(resultados["Puntaje"], errors="coerce")

# uno resultados con talleres (por ID_Taller)
resultados_talleres = resultados.merge(talleres, on="ID_Taller", how="left")

# uno con participantes (por ID_Participante)
df_final = resultados_talleres.merge(participantes, on="ID_Participante", how="left")

print(df_final.head())

# Calculo asistencia promedio por taller
asistencia_promedio = df_final.groupby("Nombre_Taller")["Asistió"].mean().reset_index()
print(asistencia_promedio)

# Calculo puntaje promedio por taller
puntaje_promedio = df_final.groupby("Nombre_Taller")["Puntaje"].mean().reset_index()
print(puntaje_promedio)

# Grafico de asistencia promedio
plt.figure(figsize=(10,6))
sns.barplot(x="Nombre_Taller", y="Asistió", data=asistencia_promedio, palette="Blues")
plt.title("Asistencia promedio por taller")
plt.xlabel("Taller")
plt.ylabel("Asistencia promedio")
plt.xticks(rotation=45)
plt.show()

# Grafico de puntaje promedio
plt.figure(figsize=(10,6))
sns.barplot(x="Nombre_Taller", y="Puntaje", data=puntaje_promedio, palette="Greens")
plt.title("Puntaje promedio por taller")
plt.xlabel("Taller")
plt.ylabel("Puntaje promedio")
plt.xticks(rotation=45)
plt.show()