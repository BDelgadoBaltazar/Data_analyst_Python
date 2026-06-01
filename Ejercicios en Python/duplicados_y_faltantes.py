import pandas as pd

# 1) Cargar el conjunto de datos
ruta_local = 'Ejercicios en Python/data_clientes.xlsx'

try:
    df_clientes = pd.read_excel(ruta_local, engine='openpyxl')

    # Diagnostico inicial para el reporte
    total_inicial = len(df_clientes)
    nulos_inicial = df_clientes['Edad'].isnull().sum()
    duplicados_inicial = df_clientes.duplicated().sum()

    # 2) Identificar y eliminar las filas duplicadas
    # Filtro los duplicados para guardarlos en el reporte antes de borrarlos
    df_duplicados = df_clientes[df_clientes.duplicated(keep=False)]

    # Elimino duplicados manteniendo el primer registro
    df_limpio = df_clientes.drop_duplicates(keep='first')
    total_sin_duplicados = len(df_limpio)

    # 3) Evaluacion de estrategias para Datos Faltantes (Edad)

    # Funcion para agrupar por rangos etarios
    def agrupar_por_edad(edad):
        if edad <= 30: return 'Jovenes (18-30 años)'
        elif edad <= 50: return 'Adultos (31-50 años)'
        else: return 'Seniors (51+ años)'

    # Estrategia A: Eliminacion de nulos
    df_estrategia_a = df_limpio.dropna(subset=['Edad']).copy()
    df_estrategia_a['grupo_etario'] = df_estrategia_a['Edad'].apply(agrupar_por_edad)
    segmentacion_a = df_estrategia_a['grupo_etario'].value_counts()

    # Estrategia B: Imputacion con la media
    media_edad = df_limpio['Edad'].mean()
    df_estrategia_b = df_limpio.copy()
    df_estrategia_b['Edad'] = df_estrategia_b['Edad'].fillna(media_edad)
    df_estrategia_b['grupo_etario'] = df_estrategia_b['Edad'].apply(agrupar_por_edad)
    segmentacion_b = df_estrategia_b['grupo_etario'].value_counts()

    # REPORTE DE HALLAZGOS Y MODIFICACIONES
    print("   REPORTE GERENCIAL: CALIDAD Y SANEAMIENTO DE DATOS   ")
    print("--------------------------------------------------------")
    print(f"1. VOLUMEN INICIAL: el dataset original contenia {total_inicial} registros.")
    print(f"2. DIAGNOSTICO DE DUPLICADOS: Se detectaron {duplicados_inicial} filas repetidas")
    print(f"  -> Accion: Se removieron los duplicados. Base limpia: {total_sin_duplicados} registros.")
    print(f"3. DIAGNOSTICO DE NULOS: Existen {nulos_inicial} clientes sin edad registrada.")
    print("------------------------------------------------------------------------------")
    print("\n EVALUACION DE IMPACTO EN SEGMENTACION DE MARKETING")
    print(f"Nota de Matías: La edad media calculada es de {media_edad: .1f} años. \n")

    print("Estrategia A (Eliminar filas con edad nula):")
    print(segmentacion_a)
    print(f"Total registros utiles: {len(df_estrategia_a)}")
    print("-" * 50)
    print("Estrategia B (Rellenar edad con la media general):")
    print(segmentacion_b)
    print(f"Total registros utiles: {len(df_estrategia_b)}")

    if duplicados_inicial > 0:
        print("REGISTROS ELIMINADOS POR DUPLICACION (MUESTRA)")
        print(df_duplicados.head(5))
except FileNotFoundError:
    print(f"Error: No se encontro el archivo Excel en la ruta: {ruta_local}")
    print("Verifica que el archivo esté dentro de la carpeta 'Ejercicios en Python'.")