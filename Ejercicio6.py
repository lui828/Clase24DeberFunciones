# Crear una función que acepte múltiples parámetros y retorne más de un valor

def operaciones_basicas(a, b):
 suma = a + b
 resta = a - b
 return suma, resta
resultado_suma, resultado_resta = operaciones_basicas(8, 3)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")