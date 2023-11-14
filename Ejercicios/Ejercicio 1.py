class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre =  nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando...")

nombre = input("Introduce el nombre del alumno: ")
edad = input("Introduce la edad del alumno: ")
grado = input("Introduce el grado del alumno: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
    """)
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break