class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre = {self.nombre}, edad = {self.edad})"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

ramirez = Persona("Manuel",28)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 18)

nueva_persona = ramirez + pedro + maria
print(nueva_persona.edad)

### Más metodos especiales ###

# Aritméticos #

# __add__(self,other): Sobrecarga del operador de suma (+)
# __sub__(self,other): Sobrecarga del operador de resta (-)
# __mul__(self,other): Sobrecarga del operador de multiplicación (*)
# __div__(self,other): Sobrecarga del operador de división (/)
# __mod__(self,other): Sobrecarga del operador de módulo (%)
# __pow__(self,other): Sobrecarga del operador de exponenciación (**)

# Comparación #

# __eq__(self,other): Sobrecarga del operador de igualdad (==)
# __ne__(self,other): Sobrecarga del operador de desigualdad (!=)
# __it__(self,other): Sobrecarga del operador menor que (<)
# __gt__(self,other): Sobrecarga del operador mayor que (>)
# __le__(self,other): Sobrecarga del operador menor o igual que (<=)
# __ge__(self,other): Sobrecarga del operador mayor o igual que (>=)

# Asignación #

# __¡add__(self,other): Sobrecarga del operador de suma en asignación (+=)
# __¡sub__(self,other): Sobrecarga del operador de resta en asignación (-=)
# __¡mul__(self,other): Sobrecarga del operador de multiplicación en asignación (*=)
# __¡div__(self,other): Sobrecarga del operador de división en asignación (/=)
# __¡mod__(self,other): Sobrecarga del operador de módulo en asignación (%=)
# __¡pow__(self,other): Sobrecarga del operador de exponenciación en asignación (**=)

# Otros #

# __str__(self): Sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto.
# __len__(self): Sobrecarga del operador len(). Devuelve la longitud del objeto.
# __getitem__(self,index): Sobrecarga del operador de indexación ([]). Permite acceder a elementos del objeto por índice.