class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

yumi = Persona("Manuel",21)

nombre = yumi.get_nombre()
print(nombre)
yumi.set_nombre("Manolo")

nombre = yumi.get_nombre()
print(nombre)