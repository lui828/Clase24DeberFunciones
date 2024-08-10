# Añade una tercera operación (multiplicación) a la función y retorna su resultado también.

def operaciones_basicas(a, b,):
 suma = a + b
 resta = a - b
 multiplicación = a * b
 return suma, resta, multiplicación
resultado_suma, resultado_resta, resultado_multiplicación = operaciones_basicas(8, 3)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}, Multiplicación: {resultado_multiplicación}")