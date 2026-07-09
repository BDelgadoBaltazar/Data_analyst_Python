import statistics as stats

ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas (millones)': [1.2, 2.5, 3.1, 18.3, 40.5, 52.1, 54.8, 46.2, 25.5, 13.8, 11.9, 9.2]
}

# Rango
rango = max(ventas['Ventas (millones)']) - min(ventas['Ventas (millones)'])

# Varianza
varianza = stats.variance(ventas['Ventas (millones)'])

# Desviacion estandar
desviacion = stats.stdev(ventas['Ventas (millones)'])

print("Rango:", rango)
print("Varianza:", varianza)
print("Desviacion estandar:", desviacion)