import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargo los archivos CSV
ventas = pd.read_csv('ventas12.csv')
productos = pd.read_csv('productos12.csv')
clientes = pd.read_csv('clientes12.csv')

# Exploro el DataFrame de ventas
print("Ventas - Información general")
print(ventas.info())
print("\nPrimeras filas:")
print(ventas.head())
print("Estadisticas descriptivas:") # Corregido: \Estadisticas -> Estadisticas
print(ventas.describe(include="all"))

# Exploro el DataFrame de productos
print("\nProductos - Información general")
print(productos.info())
print("\nPrimeras filas:")
print(productos.head())
print("\nEstadisticas descriptivas:")
print(productos.describe(include="all"))

# Exploro el DataFrame de clientes
print("\nClientes - Información general")
print(clientes.info())
print("\nPrimeras filas:")
print(clientes.head())
print("\nEstadisticas descriptivas:")
print(clientes.describe(include="all"))

# --- Ventas ---
# Elimino duplicados
ventas = ventas.drop_duplicates()

# Manejo valores nulos (ejemplo: elimino filas con nulos)
ventas = ventas.dropna()

# Convierto columna Fecha a formato datetime
ventas["Fecha"] = pd.to_datetime(ventas["Fecha"], dayfirst=True, errors="coerce")

# --- Productos ---
# Elimino duplicados
productos = productos.drop_duplicates()
productos = productos.dropna()

# Convierto Precio_Unitario y Stock a numericos (puede que esten como texto)
productos["Precio_Unitario"] = pd.to_numeric(productos["Precio_Unitario"], errors="coerce")
productos["Stock"] = pd.to_numeric(productos["Stock"], errors="coerce")

# --- Clientes ---
clientes = clientes.drop_duplicates()
clientes = clientes.dropna()

# Limpio columna Ingresos (quito simbolos de moneda y convierto a numerico)
clientes["Ingresos"] = clientes["Ingresos"].replace('[$,]', '', regex=True).astype(float) # Corregido: [$,] para el símbolo de dólar

# Convierto Edad a numerico
clientes["Edad"] = pd.to_numeric(clientes["Edad"], errors="coerce")

# Uno ventas con productos
ventas_productos = ventas.merge(productos, on="ID_Producto", how="left")

# Calculo gasto por venta
ventas_productos["Gasto"] = ventas_productos["Cantidad"] * ventas_productos["Precio_Unitario"]

# Agrupar por cliente
gasto_por_cliente = ventas_productos.groupby("ID_Cliente")["Gasto"].sum().reset_index()

# Unir con clientes para mas informacion
gasto_por_cliente = gasto_por_cliente.merge(clientes, on="ID_Cliente", how="left")

print(gasto_por_cliente.head())

# Calculo ventas totales por categoria
ventas_por_categoria = ventas_productos.groupby("Categoría")["Cantidad"].sum().reset_index()

# Ordeno por cantidad vendida
ventas_por_categoria = ventas_por_categoria.sort_values(by="Cantidad", ascending=False) # Corregido: "False" a False

print(ventas_por_categoria)

# Grafico de barras
plt.figure(figsize=(10,6))
sns.barplot(x="Categoría", y="Cantidad", data=ventas_por_categoria, palette="Set2")
plt.title("Ventas totales por categoría de producto")
plt.xlabel("Categoría de producto")
plt.ylabel("Cantidad vendida")
plt.xticks(rotation=45)
plt.show()