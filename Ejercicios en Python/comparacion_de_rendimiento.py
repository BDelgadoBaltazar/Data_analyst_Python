import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creo el DataFrame con los datos de clientes y compras
data = pd.DataFrame({
    'cliente': ['Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4', 'Cliente 5'],
    'importe_compra': [200, 450, 120, 700, 30],
    'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Febrero']
})

print(data.head())

# Creo boxplot de compras por mes
plt.figure(figsize=(8,6))
sns.boxplot(x="mes", y="importe_compra", data=data, palette="Set3")

# Personalizacion
plt.title("Distribucion de compras por mes")
plt.xlabel("Mes")
plt.ylabel("Importe de compra")
plt.show()