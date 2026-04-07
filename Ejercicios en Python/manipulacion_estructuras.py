# Lista llamada numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tupla llamada meses
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

# Diccionario con notas, los estudiantes (clave) y sus respectivas notas (valor)
notas = {
    "Matias": 10,
    "Luis": 8,
    "Silvia": 6
}

# Conjunto llamado numeros_unicos sin duplicados
numeros_unicos = {1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9}

print(numeros)
print(meses)
print(notas)
print(numeros_unicos)

# Modifico nota 
notas["Matias"] = 9
print(f"Notas actualizadas: {notas}")

# Utilizo bucle para mostrar los numeros pares de la lista numeros
for n in numeros:
    if n % 2 == 0:
        print(n)

# Accedo al primer y ultimo mes de la tupla
primer_mes = meses[0] # Indice 0 para el primero
ultimo_mes = meses[-1] # Indice -1 para el ultimo

print(f"El año comienza en {primer_mes} y termina en {ultimo_mes}.")

# Funcion normal
def multiplicar_por_2(n):
    return n * 2

# Creo la lista 'dobles' usando un bucle tradicional
dobles = []
for n in numeros:
    dobles.append(multiplicar_por_2(n))

# Funcion lambda
dobles_lambda = list(map(lambda n: n * 2, numeros))

# List comprehensions
cuadrados = [n**2 for n in numeros]

# Dict comprehensions
cubos = {n: n**3 for n in numeros}
print(f"Diccionario de cubos: {cubos}")

print (f"Lista dobles (normal): {dobles}")
print (f"Lista dobles (Lambda): {dobles_lambda}")
print (f"Lista cuadrados (Comp): {cuadrados}")

cubos_tradicional = {}
for n in numeros:
    cubos_tradicional[n] = n**3

print(f"Diccionario de cubos: {cubos}")
print(f"Diccionario de cubos tradicional: {cubos_tradicional}")