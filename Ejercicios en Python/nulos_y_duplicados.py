import pandas as pd

# 1) Cargar los datos y contar valores nulos por columna

# Cargo el archivo 
df_satis = pd.read_csv('Ejercicios en Python/satis_clientes.csv')

# Cuento los valores nulos por columna
valores_nulos = df_satis.isnull().sum()

# 2) Identificar y contar filas duplicadas en total
total_duplicados = df_satis.duplicated().sum()

# 3) Creo el informe solicitado
print("   INFORME DE CALIDAD Y DIAGNOSTICO: SATISFACCION DE CLIENTES    ")

# a) Cantidad total de registros
print(f"a. Cantidad total de registros analizados: {len(df_satis)} filas")

# b) Cantidad total de valores nulos por columna
print("b. Cantidad total de valores nulos detectados por columna:")
print(valores_nulos)

# c) Cantidad de filas duplicadas
print(f"c. Cantidad total de filas completamente duplicados: {total_duplicados}")

# 4) Crear un DataFrame de los registros duplicados para ver su contenido
df_duplicados = df_satis[df_satis.duplicated(keep=False)]

# 4) Mostrar el contenido del DataFrame de duplicados
print("DETALLE VISUAL DE LOS REGISTROS DUPLICADOS")
if not df_duplicados.empty:
    print(df_duplicados)
else:
    print("¡Buenas noticias! el dataset no contiene registros duplicados")