class Banco:

    def __init__(self, nombre, clientes, cajeros, capital, color):

        self.nombre = nombre
        self.clientes = clientes
        self.cajeros = cajeros
        self.capital = capital
        self.color = color

    def mostrar_datos(self):

        print("Nombre del banco:", self.nombre)
        print("Número de clientes:", self.clientes)
        print("Número de cajeros:", self.cajeros)
        print("Capital:", self.capital)
        print("Color del banco:", self.color)

banco1 = Banco(
    "Banco Azteca",
    5000,
    20,
    1000000,
    "Verde"
)

banco1.mostrar_datos()