# LCP (Liscov Substitution principle) o Principio de sustitución de Liscov
# Cada clase que hereda de otra debe poder usarse como su padre.
# En caso contrario se debe recategorizar las clases.

# NO cumple con el LCP

class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"

def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))

# SI cumple con el LCP

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass