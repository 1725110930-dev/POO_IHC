class Coche:
    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} {self.modelo} ha sido encendido."
        return "El coche ya está encendido."

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            return f"Vas a {self.velocidad} km/h."
        return "No puedes acelerar, el coche está apagado."

    def frenar(self):
        self.velocidad = 0
        return "El coche se ha detenido por completo."


mi_coche = Coche("Toyota", "Corolla", "Gasolina")

print(mi_coche.encender())
print(mi_coche.acelerar(50))
print(mi_coche.frenar())