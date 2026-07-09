import matplotlib.pyplot as plt

# Datos
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
ventas = [100, 120, 130, 150, 180, 170, 200, 210, 250, 270, 300, 320]

# Creo grafico de lineas
plt.figure(figsize=(10,6))
plt.plot(meses, ventas, marker='o', linestyle='-', color='b')

# Personalizacion
plt.title("Ventas mensuales en el último año")
plt.xlabel("Meses")
plt.ylabel("Unidades vendidas")
plt.grid(True)
plt.show()