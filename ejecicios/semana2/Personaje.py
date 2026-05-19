class Personaje:

    def __init__(self, nombre, altura, edad, fuerza):

        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.fuerza = fuerza

    def mostrar_datos(self):

        print("Nombre:", self.nombre)
        print("Altura:", self.altura)
        print("Edad:", self.edad)
        print("Fuerza:", self.fuerza)


# Crear personaje
personaje1 = Personaje(
    "Steve",
    "1.80 m",
    25,
    100
)

# Mostrar datos
personaje1.mostrar_datos()