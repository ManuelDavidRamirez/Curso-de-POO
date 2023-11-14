class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

ramirez = Persona("Manuel",21)

nombre = ramirez.get_nombre()
print(nombre)
ramirez.set_nombre("Manolo")

nombre = ramirez.get_nombre()
print(nombre)