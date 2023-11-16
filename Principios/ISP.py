# ISP (Interface segregation principle) o Principio de segregación de la interfaz
# Ningún cliente debe ser forzado a depender de interfaces que no utilice

from abc import ABC, abstractclassmethod

# NO cumple con el ISP

class Trabajador(ABC):

    @abstractclassmethod
    def comer(self):
        pass

    @abstractclassmethod
    def trabajar(self):
        pass

    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador):

    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):

    def comer(self):
        pass

    def trabajar(self):
        print("El robot esta trabajando")

    def dormir(self):
        pass

# SI cumple con el ISP

class Trabajador(ABC):

    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):

    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):

    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):

    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):

    def trabajar(self):
        print("El robot esta trabajando")