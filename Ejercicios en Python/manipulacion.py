import pandas as pd
import seaborn as sns

# Cargo el conjunto de datos directamente desde seaborn
df_titanic = sns.load_dataset('titanic')

# 1) Obtener los nombres de las columnas del DataFrame

# Accedo al atributo .columns del DataFrame
nombres_columnas = df_titanic.columns

# Reporte
print("AUDITORIA DE ESTRUCTURA: COLUMNAS DEL TITANIC")
print(f"El DataFrame contiene un total de {len(nombres_columnas)} columnas.\n")

print("Lista oficial de etiquetas de columnas:")
print(nombres_columnas)

# Convierto a una lista comun de Python para que sea mas legible
print("Formato de lista limpia de Python:")
print(list(nombres_columnas))

# 2) Eliminar la columna 'deck' de forma segura

# Uso .drop() especificando el nombre de la columna y axis=1 (que significa 'columnas')
# errors='ignore' evita que el codigo falle si volvemos a correr la celda y la columna ya no existe
df_titanic_filtrado = df_titanic.drop(columns=['deck'], errors='ignore')

# Reporte de estructura 
print("MODIFICACION ANATOMICA: ELIMINACION DE DECK")
print(f"Columnas originales en df_titanic: {df_titanic.shape[1]}")
print(f"Columnas actuales en df_titanic_filtrado: {df_titanic_filtrado.shape[1]}")

# Verifico si 'deck' sigue estando en la lista de columnas
if 'deck' not in df_titanic_filtrado.columns:
    print("Exito. La columna 'deck' ha sido removida de la nueva estructura.")
else:
    print("Alerta: La columna aun permanece en el DataFrame.")

# 3) Reindexar / Reconfigurar los indices del DataFrame

# Caso A: Reinicio secuencial limpio (Reset Index)
# Elimina cualquier desorden previo en los numeros de las filas y asegura que arranquen de 0 a N-1
# drop=True evita que el indice viejo se guarde como una columna nueva.
df_titanic_reseteado = df_titanic_filtrado.reset_index(drop=True)

# Caso B: Indexacion por Variable Logica (Set Index)
# Como analistas, el indice por defecto (0, 1, 2, ...) no nos dice nada
# Voy a convertir una columna real en el nuevo "DNI" de cada fila
# Primero, creamos una columna simulada de 'id_pasajero' para tener un identificador unico claro
df_titanic_reseteado['id_pasajero'] = [f"PAS-{i+1000}" for i in range(len(df_titanic_reseteado))]

# Establezco esa nueva columna como el INDICE oficial de la tabla 
df_titanic_reindexado = df_titanic_reseteado.set_index('id_pasajero')

# Reporte de estructura
print("RECONFIGURACION DE INDICES COMPLETADA")
print("Muestra de la tabla final (Nota como el indice ya no son numeros, sino el ID):")
print("-" * 50)
print(df_titanic_reindexado[['survived', 'pclass', 'sex', 'age', 'fare']].head(5))