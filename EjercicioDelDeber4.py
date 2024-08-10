# Intenta usar la variable global x dentro de la función sin crear una nueva variable local.

x = 10 # Variable global
def mi_funcion():

 print(f"Variable local x dentro de la función: {x}")
mi_funcion()
print(f"Variable global x fuera de la función: {x}")
