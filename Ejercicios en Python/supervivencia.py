import pandas as pd
import seaborn as sns

# Cargo los datos
df_titanic = sns.load_dataset('titanic')

# 1) Filtrar pasajeros sobrevivientes

# Aplico la condicion: quiero las filas donde 'survived' sea igual a 1
# Uso .copy() al final para crear una base de datos nueva e independiente
df_sobrevivientes = df_titanic[df_titanic['survived'] == 1].copy()

# Verificacion para el historiador
total_pasajeros = len(df_titanic)
total_sobrevivientes = len(df_sobrevivientes)
porcentaje_rescate = (total_sobrevivientes / total_pasajeros) * 100

print("EXTRACCION INTERNA: GRUPO DE SOBREVIVIENTES")
print(f"Total de personas registradas a bordo: {total_pasajeros}")
print(f"Pasajeros extraidos con exito: {total_sobrevivientes}")
print(f"Tasa de supervivencia de la muestra: {porcentaje_rescate: .1f}")
print("Muestra de los primeros 5 sobrevivientes en la base de datos:")

# Muestro las columnas clave para verificar que en 'survived' solo haya unos (1)
print(df_sobrevivientes[['survived', 'pclass', 'sex', 'age', 'fare']].head())

# 2) Seleccionar columnas relevantes de los sobrevivientes

# Defino la lista de variables demograficas y socioeconomicas que me interesan
columnas_interes = ['sex', 'age', 'fare']

# Filtro la base de sobrevivientes para conservar solo esas columnas
# Uso .copy() para desvincular completamente esta estructura de la tabla madre
df_sobrevivientes_reducido = df_sobrevivientes[columnas_interes].copy()

# Verificacion
print("REESTRUCTURACION DEL PERFIL DE SOBREVIVIENTES")
print(f"Dimensiones de la nueva tabla: {df_sobrevivientes_reducido.shape[0]} filas y {df_sobrevivientes_reducido.shape[1]} columnas")
print("Primeros 5 registros del perfil seleccionado:")
print(df_sobrevivientes_reducido.head())

# 3) Crear una nueva columna categorica para la clase

# Recupero la columna 'pclass' de la base original de sobrevivientes 
# para poder hacer la traduccion (ya que en el paso anterior solo deje sex, age y fare)
df_sobrevivientes_reducido['pclass'] = df_sobrevivientes['pclass']

# Defino el diccionario de traduccion (Mapeo)
diccionario_clases = {
    1: 'Primera Clase',
    2: 'Segunda Clase',
    3: 'Tercera Clase'
}

# Creo la nueva columna 'categoria_clase' aplicando el mapeo
df_sobrevivientes_reducido['categoria_clase'] = df_sobrevivientes_reducido['pclass'].map(diccionario_clases)

# Convierto formalmente la columna a tipo 'category' para optimizar la memoria
df_sobrevivientes_reducido['categoria_clase'] = df_sobrevivientes_reducido['categoria_clase'].astype('category')

# Elimino la columna numerica 'pclass' para dejar la tabla impecable
df_sobrevivientes_reducido = df_sobrevivientes_reducido.drop(columns=['pclass'])

# REPORTE FINAL
print("DATASET FINALIZADO Y ENRIQUECIDO")
print("Estructura final con la nueva columna categorica:")
print(df_sobrevivientes_reducido.head(10))

# Cruzo la nueva columna con los sobrevivientes para mi primera estadistica real
print("Distribucion de los sobrevivientes por Clase Social:")
print(df_sobrevivientes_reducido['categoria_clase'].value_counts().to_string())