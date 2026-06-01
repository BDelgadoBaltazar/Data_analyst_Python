# Parte 1
import pandas as pd

df = pd.read_csv('Ejercicios en Python/ventas.csv')

print("Visualizacion de las primeras filas del dataset:")
print(df.head())

# Parte 2
import pandas as pd

id_planilla = "1fFSi_1rXXyVOEw4pjz4jBOO1E2criR_H_20kWb26W5k"

url = f"https://docs.google.com/spreadsheets/d/{id_planilla}/export?format=csv"

df_sheets = pd.read_csv(url)

print("Datos cargados desde Google Sheets:")
print(df_sheets.head())