import pandas as pd

# 1) Obtener los DataFrames de Recursos Humanos (Archivos CSV)

# Cargo la base de datos de datos personales
df_empleados = pd.read_csv('data_empleados.csv')

# Cargo la base de datos de la situacion contractual
df_situacion = pd.read_csv('situacion_empleados.csv')

# Reporte de Carga
print("SISTEMA DE RRHH - CONTROL DE INGESTION ")
print(f"DataFrame 'Personal' cargado. Empleados detectados: {len(df_empleados)}")
print(f"DataFrame 'Situacion' cargado. Contratos detectados: {len(df_situacion)}")
print("-" * 50)
print("Columnas de Datos Personales:")
print(list(df_empleados.columns))
print("\nMuestra de las primeras 3 filas (Ficha Personal):")
print(df_empleados.head(3))
print("-" * 50)
print("Columnas de Situacion Laboral:")
print(list(df_situacion.columns))
print("\nMuestra de las primeras 3 filas (Ficha Contractual):")
print(df_situacion.head(3))

# 2) Combinar DataFrames con pd.merge() y documentar justificaciones

# Realizo la union tipo INNER usando la columna ID como llave
df_maestro_empleados = pd.merge(
    df_empleados,
    df_situacion,
    on='ID',
    how='inner'
)

# Reporte de Consolidacion
print("SISTEMA DE RRHH - CRUCE MAESTRO OPTIMIZADO")
print(f"Registros en Base Personal: {len(df_empleados)}")
print(f"Registros en Base Contratos: {len(df_situacion)}")
print(f"TOTAL en DataFrame Maestro Unificado: {len(df_maestro_empleados)}")
print("-" * 50)
print("Estructura final de la ficha del empleado:")
print(list(df_maestro_empleados.columns))
print("\nPrimeros 3 registros de la nomina consolidada:")
print(df_maestro_empleados[['ID', 'Nombre', 'Departamento', 'Cargo', 'Salario']].head(3))
