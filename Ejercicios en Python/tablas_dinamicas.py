import pandas as pd

# Cargo el conjunto de datos
df_ventas_marketing = pd.read_csv('ventas1.csv')

# Reporte de auditoria
print("LOGISTICA DE DATOS: CAMPAÑA DE MARKETING")
print("Archivo 'ventas.csv' auto-generado y localizado con exito")
print(f"Matriz de datos cargada: {df_ventas_marketing.shape[0]} registros listos")
print(df_ventas_marketing)

# 2) Utilizar la funcion pivot_table() para las ventas mensuales

# Construyo la tabla dinamica cruzando las dimensiones solicitadas
df_dinamica_ventas = df_ventas_marketing.pivot_table(
    index='producto', # Las filas de la tabla seran los Productos (A, B, C)
    columns='mes', # Las columnas seran los meses (Enero, Febrero, Marzo)
    values='ventas', # Los datos numericos a cruzar son las Ventas
    aggfunc='sum' # Operacion: Sumar las ventas en caso de que coincidan
)

# Reporte Analitico
print("MATRIZ DINAMICA DE VENTAS MENSUALES")
print("Resultado del pivoteo estructural de Pandas:")
print("-" * 50)
print(df_dinamica_ventas)

# 3) Asegurar la estructura final, rellenar vacios y ordenar ejes

# Vuelvo a generar la tabla asegurando que los vacios se muestren como 0
df_dinamica_final = df_ventas_marketing.pivot_table(
    index='producto', # Productos obligatoriamente en las filas
    columns='mes',    # Meses obligatoriamente en las columnas
    values='ventas',  # Ventas Totales como valores internos
    aggfunc='sum',    # Operacion matematica de acumulacion
    fill_value=0      # Reemplaza los vacios (NaN) por un 0 claro
)

# Ordeno las columnas para que sigan el orden del calendario
meses_ordenados = ['Enero', 'Febrero', 'Marzo']
df_dinamica_final = df_dinamica_final[meses_ordenados]

# PRESENTACION DE LA MATRIZ FINAL PARA MARKETING
print("TABLA DINAMICA DE RENDIMIENTO DE CAMPAÑA")
print("Estructura bidimensional final validada:")
print("-" * 50)
print(df_dinamica_final)
print("Resultados listos para las diapositivas de la presentacion")