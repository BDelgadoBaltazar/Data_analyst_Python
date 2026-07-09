import statistics as stats

ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas (millones)': [1.2, 2.5, 3.1, 18.3, 40.5, 52.1, 54.8, 46.2, 25.5, 13.8, 11.9, 9.2]
}

media = stats.mean(ventas['Ventas (millones)'])
mediana = stats.median(ventas['Ventas (millones)'])
moda = stats.mode(ventas['Ventas (millones)'])

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)