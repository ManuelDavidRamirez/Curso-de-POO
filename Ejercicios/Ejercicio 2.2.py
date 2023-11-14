class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")

class Murcielago(Mamifero,Ave):
    pass

# Animal 1
murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

# Animal 2
ave = Ave()

ave.comer()
ave.volar()

# Mostrar el orden del MRO
print(Murcielago.mro())