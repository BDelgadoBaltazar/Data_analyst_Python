import pandas as pd
import unicodedata

# 1) Cargo el conjunto de datos
ruta_local = 'Ejercicios en Python/productos.xlsx'

try: 
    df_productos = pd.read_excel(ruta_local, engine='openpyxl')
    print("Dataset cargado con exito")
    print(f"Dimensiones del inventario: {df_productos.shape[0]} filas y {df_productos.shape[1]} columnas.")
    print("\nPrimeros 5 registros del catalogo:")
    print(df_productos.head())

    # Limpieza de caracteres de texto
    # Convierto a string, elimino el signo '$' y quito espacios vacios externos
    df_productos['Precio'] = df_productos['Precio'].astype(str).str.replace('$', '', regex=False).str.strip()

    # Conversion formal a tipo numerico (Float)
    # errors='coerce' es clave: si hay algun texto roto (ej: 'Consultar'), lo vuelve NaN en lugar de romper el codigo
    df_productos['Precio'] = pd.to_numeric(df_productos['Precio'], errors='coerce')

    # Verificacion de Control de Calidad
    print("VERIFICACION DE TIPO DE DATO")
    print(df_productos[['Producto', 'Precio']].dtypes)
    print("\nMuestra de los precios convertidos:")
    print(df_productos[['Producto', 'Precio']].head(10))

    def normalizar_texto(texto):
        if pd.isna(texto):
            return texto
        
        texto_limpio = str(texto).strip().lower()

        # Separar caracteres de sus acentos/tildes
        texto_descompuesto = unicodedata.normalize('NFD', texto_limpio)

        # Conservar solo los caracteres base
        return "".join([c for c in texto_descompuesto if unicodedata.category(c) != 'Mn'])
    
    df_productos['Producto'] = df_productos['Producto'].apply(normalizar_texto)

    print("NORMALIZACION DE TEXTO")
    print("Muestra del catalogo estandarizado en minusculas y sin acentos:")
    print(df_productos[['Producto', 'Precio']].head(10))
        
except FileNotFoundError:
    print(f"No se ha encontrado el archivo en la ruta {ruta_local}")
