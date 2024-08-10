# Modifica el código para que la función interior reciba un parámetro y lo imprima.
def funcion_exterior():
    def funcion_interior(mensaje):
        print(f"Esta es la función interior. mensaje: {mensaje}")
    funcion_interior("Que tal, aqui hablando desde la funcion interior")
    print("Esta es la función exterior")
funcion_exterior()

