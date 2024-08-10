# Funciones Anidadas

def funcion_exterior():
    def funcion_interior():
        print("Esta es la función interior")
    funcion_interior()
    print("Esta es la función exterior")
funcion_exterior()