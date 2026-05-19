class Mesa:
    def __init__(self, material, color, capacidad):
        self.material = material
        self.color = color
        self.capacidad = capacity
        self.ocupada = False

    def ocupar(self):
        if not self.ocupada:
            self.ocupada = True
            return "La mesa ahora está ocupada."
        return "La mesa ya estaba ocupada."

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return "La mesa ahora está libre."
        return "La mesa ya estaba libre."

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"La mesa ha sido pintada de color {self.color}."


mi_mesa = Mesa("Madera", "Marrón", 4)

print(mi_mesa.ocupar())
print(mi_mesa.cambiar_color("Blanco"))
print(mi_mesa.liberar())