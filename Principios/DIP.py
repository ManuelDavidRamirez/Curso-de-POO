# DIP (Dependency inversion principle) o Principio de inversión de dependencia
# Los módulos de alto nivel no deben depender de los de bajo nivel.
# También las abstracciones no deben depender de los detalles sino al revez

# NO cumple con el DIP

class Diccionario:
    def verificar_palabra(self,palabra):
        # Lógica para verificar palabras
        pass

class CorrectorOrtográfico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        # Usamos el diccionario para corregir el texto
        pass

# SI cumple con el DIP

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar si la palabra esa en el diccionario
        pass

class CorrectorOrtografico():
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # usamos el verificador para corregir texto
        pass

corrector = CorrectorOrtografico(Diccionario())