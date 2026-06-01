import pandas as pd

# Replico el diccionario exacto del set de datos
data = {
    'producto': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Marzo', 'Marzo', 'Marzo', 'Enero', 'Febrero'],
    'ventas': [150, 200, 250, 300, 100, 400, 350, 200, 300]
}

# Convierto el diccionario a un DataFrame inicial
df_origen = pd.DataFrame(data)

# Guardo el archivo como 'ventas.csv' en mi entorno local
# index=false evita que se guarde una columna extra con los numeros de fila
df_origen.to_csv('ventas1.csv', index=False)

# 1) Cargar el conjunto de datos llamado ventas.csv
df_ventas = pd.read_csv('ventas1.csv')

# Reporte de control
print("SISTEMA DE CONTROL DE VENTAS")
print("Archivo 'ventas1.csv' detectado y cargado con exito.\n")
print(f"Total de registros comerciales cargados: {len(df_ventas)}")
print("-" * 50)
print("Vista preliminar de la base de datos de la campaña:")
print(df_ventas)

# 2) Agrupar las ventas por producto y sumar las ventas totales

# Agrupo por la columna 'producto' y aplicamos la suma sobre la columna 'ventas'
# Uso [[ 'ventas' ]] para que el resultado devuelva un DataFrame limpio y elegante
df_ventas_totales = df_ventas.groupby('producto')[['ventas']].sum()

# Reporte gerencial
print("RENDIMIENTO CONSOLIDADO POR PRODUCTO")
print("Resultados de la suma total acumulada por cada linea:")
print("-" * 50)
print(df_ventas_totales)

# 3) Generar un nuevo DataFrame formal y mostrarlo en pantalla

# Tomo el resultado anterior y reseteo el indice para recuperar la columna
df_informe_final = df_ventas_totales.reset_index()

# Renombro la columna 'ventas' a 'ventas_totales'
# para que el reporte sea 100% explicito y corporativo
df_informe_final = df_informe_final.rename(columns={'ventas': 'ventas_totales'})

# PRESENTACION EN PANTALLA
print("DATAFRAME OFICIAL: TOTAL DE VENTAS")
print("Estructura final del nuevo DataFrame generado:")
print("-" * 50)
print(df_informe_final)
print("Reporte consolidado. Listo para definicion de estrategia.")