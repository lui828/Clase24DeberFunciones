# Función Recursiva.
 
def factorial(n):
 if n == 1:
  return 1
 else:
  return n * factorial(n - 1)
print(f"El factorial de 5 es: {factorial(5)}")