class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau, guau!"

    def caminar(self, pasos):
        return f"{self.nombre} caminó {pasos} pasos."

    def cumplir_anos(self):
        self.edad += 1
        return f"¡Feliz cumpleaños {self.nombre}! Ahora tiene {self.edad} años."


mi_perro = Perro("Firulais", "Labrador", 3)

print(mi_perro.ladrar())
print(mi_perro.caminar(20))
print(mi_perro.cumplir_anos())