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
        
ramirez = Persona("Manuel",21)

nombre = ramirez.nombre
print(nombre)

ramirez.nombre = "Pepe"

nombre = ramirez.nombre
print(nombre)

del ramirez.nombre

print("Hola Mundo, estoy aprendiendo Python")