# Ejercicio 1 (Parametros posicionales)
def multiplicar(a, b):
    return a * b

resultado_1 = multiplicar(5, 4)
resultado_2 = multiplicar(10, 0.5)
resultado_3 = multiplicar(-3, 7)

print(f"Resultado 1 (5 * 4): {resultado_1}")
print(f"Resultado 2 (10 * 0.5): {resultado_2}")
print(f"Resultado 3 (-3 * 7): {resultado_3}")

# Ejercicio 2 (Parametros por defecto)
def bienvenida(nombre, mensaje="¡Bienvenido!"):
    return f"{mensaje}, {nombre}."

saludo_estandar = bienvenida("Matias")
saludo_personalizado = bienvenida("Luis", "¡Hola, que tal!")

print(f"Resultado Prueba 1: {saludo_estandar}")
print(f"Resultado Prueba 2: {saludo_personalizado}")

# Ejercicio 3 (Parametros indefinidos (*args))
def calcular_promedio(*notas):
    if not notas:
        return 0

    total = sum(notas)
    promedio = total / len(notas)
    return promedio;

promedio_3_notas = calcular_promedio(8, 9, 10)
promedio_5_notas = calcular_promedio(7, 7, 8, 9, 10)
promedio_1_nota = calcular_promedio(6)

print(f"Promedio de 3 notas (8, 9, 10): {promedio_3_notas: .2f}")
print(f"Promedio de 5 notas (7, 7, 8, 9, 10): {promedio_5_notas: .2f}")
print(f"Promedio de 1 nota (6): {promedio_1_nota}")

# Ejercicio 4 (Parametros de palabras clave indefinidas (**kwargs))
def concatena_info(nombre, **datos):
    resumen = f"Informacion de {nombre}:"

    for clave, valor in datos.items():
        resumen += f" | {clave.capitalize()}: {valor}"

    return resumen

perfil_matias = concatena_info("Matias", edad=30, ciudad="Buenos Aires", ocupacion="Data Analyst")
perfil_sabrina = concatena_info("Sabrina", ciudad="Cordoba", especialidad="Big Data")
perfil_luis = concatena_info("Luis", antiguedad="5 años")

print(perfil_matias)
print(perfil_sabrina)
print(perfil_luis)