divmod(10,3)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola {self.nombre}")
        
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"