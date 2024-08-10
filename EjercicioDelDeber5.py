# Crea una nueva variable global y modifícala dentro de una función.

x = 10
def modificar_global():
 global x
 x = 20
 print(f"Variable global x modificada dentro de la función: {x}")
modificar_global()
print(f"Variable global x fuera de la función: {x}")

