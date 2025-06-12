class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y mi matrícula es {self.matricula}.")
        