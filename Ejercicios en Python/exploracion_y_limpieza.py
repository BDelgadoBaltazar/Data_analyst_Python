import pandas as pd

# 1) Cargo el excel
ruta_archivo = ('Ejercicios en Python/Actividad 2.xlsx')

try:
    df = pd.read_excel(ruta_archivo)

    # a) Identifico y cuento duplicados
    total_duplicados = df.duplicated().sum()
    df_duplicados = df[df.duplicated(keep=False)]

    # b) Identificar y contar nulos por columna
    total_nulos = df.isnull().sum()

    # IMPRESION DEL INFORME
    print("   EXAMEN PRELIMINAR: CALIDAD DE LOS DATOS   ")
    print(f"Volumen del Dataset: {df.shape[0]} filas y {df.shape[1]} columnas.\n")

    print("a) Identificacion de Datos Duplicados:")
    print(f"  - Se encontraron {total_duplicados} filas completamente duplicadas.")

    print("b) Identificacion de Valores Nulos por columna:")
    print(total_nulos)

    # Mostrar detalle visual si existen problemas
    if total_duplicados > 0:
        print("DETALLE VISUAL DE REGISTROS DUPLICADOS")
        print(df_duplicados)
    else:
        print("No hay registros duplicados que requieran eliminacion")

except FileNotFoundError:
    print(f"Error: No se encontro el archivo Excel en la ruta: {ruta_archivo}")
    print("Verifica que el archivo esté dentro de la carpeta 'Ejercicios en Python'.")

