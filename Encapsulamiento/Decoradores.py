def decorador(funcion):
    def funcion_decorada():
        print("Antes de llamar a la función")
        funcion()
        return funcion_decorada

# def saludo():
#     print("Hola Manu, ¿como andas?")

# saludo_decorado = decorador(saludo)
# saludo_decorado()

@decorador
def saludo():
    saludo("Hola Manu, ¿como andas?")

saludo()