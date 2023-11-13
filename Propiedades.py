class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre
        
yumi = Persona("Manuel",21)

nombre = yumi.nombre
print(nombre)

yumi.nombre = "Pepe"

nombre = yumi.nombre
print(nombre)

del yumi.nombre

print("Hola Mundo, estoy aprendiendo Python")