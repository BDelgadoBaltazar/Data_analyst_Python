import pandas as pd

# 1) Obtener los dos DataFrames reales desde el archivo ventas.xlsx

# Cargo la pestaña 'Norte'
df_norte = pd.read_excel('ventas.xlsx', sheet_name='Norte')

# Cargo la pestaña 'Sur'
df_sur = pd.read_excel('ventas.xlsx', sheet_name='Sur')

# Reporte de Control de Calidad
print("SYNTHDATA - CONTROL DE CARGA REAL")
print(f"Hoja 'Norte' cargada. Registros encontrados: {len(df_norte)}")
print(f"Hoja 'Sur' cargada. Registros encontrados: {len(df_sur)}")
print("-" * 50)
print("Columnas de la Sucursal Norte:")
print(list(df_norte.columns))
print("\nMuestra de las primeras filas de Norte:")
print(df_norte.head(3))
print("-" * 50)
print("Columnas de la Sucursal Sur:")
print(list(df_sur.columns))
print("\nMuestra de las primeras filas de Sur:")
print(df_sur.head(3))

# Cambio las columnas de la sucursal Sur para que coincidan con la Norte 
df_sur_homologado = df_sur.rename(columns={
    'Sede': 'Sucursal',
    'Ventas': 'Ingresos'
})

# 2) Concatenar los DataFrames Verticalmente
# ignore_index=True recrea un indice limpio del 0 al N-1 para la nueva tabla unificada
df_consolidado = pd.concat([df_norte, df_sur_homologado], ignore_index=True)

print("SYNTHDATA - REPORTE DE CONCATENACION")
print(f"Registros en Norte: {len(df_norte)}")
print(f"Registros en Sur: {len(df_sur_homologado)}")
print(f"TOTAL en DataFrame Consolidado: {len(df_consolidado)}")
print("-" * 50)
print("¿Existen datos faltantes (nulos) en la nueva matriz?")
print(df_consolidado.isnull().sum())

# 3) Asegurar la estructura final: Sucursal, Producto, Ventas, Mes

# A. Renombro la columna 'Ingresos' a 'Ventas' en el DataFrame consolidado
df_reporte_final = df_consolidado.rename(columns={'Ingresos': 'Ventas'})

# B. Fuerzo el orden exacto de las columnas que solicitó el cliente
columnas_solicitadas = ['Sucursal', 'Producto', 'Ventas', 'Mes']
df_reporte_final = df_reporte_final[columnas_solicitadas]

# CONTROL DE CALIDAD GERENCIAL
print("SYNTHDATA - REPORTE FINAL CONSOLIDADO")
print("Columnas reestructuradas y validadas con exito")
print("-" * 50)
print("Estructura oficial de las columnas:")
print(list(df_reporte_final.columns))
print("\nPrimeros registros del informe final unificado:")
print(df_reporte_final.head(5))