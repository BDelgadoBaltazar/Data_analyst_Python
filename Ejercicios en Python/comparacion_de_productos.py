import matplotlib.pyplot as plt

# Datos 
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
ventas = [300, 250, 400, 350]

# Creo grafico de barras
plt.figure(figsize=(8,6))
plt.bar(productos, ventas, color=['blue', 'green', 'orange', 'red'])

# Personalizacion
plt.title("Ventas por producto en la campaña")
plt.xlabel("Productos")
plt.ylabel("Unidades vendidas")
plt.show()