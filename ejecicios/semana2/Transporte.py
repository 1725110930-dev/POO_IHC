class Transporte:
    def __init__(self, modelo, color, ano, tipo_combustible, velocidad_maxima, num_puertas, num_pasajeros, placa, precio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.precio = precio
        self.tipo_combustible = tipo_cumbistible
        self.velocidad_maxima = velocidad_maxima
        self.num_puertas = num_puertas
        self.num_pasajeros = num_pasajeros

    def encender(self):
        print(f"{self.marca}{self.modelo} esta encendido")
    def apagar(self):
        print(f"{self.marca}{self.modelo} esta apagado")
    def acelerar(self):
        print(f"{self.marca}{self.modelo} esta acelerado")
    def frenar(self):
        print(f"{self.marca}{self.modelo} esta frenada") 
    def tocar(self):
        print(f"{self.marca}{self.modelo} esta tocando el claxon")

wrx = Transport("Subaru","WRX","Azul","2025","Gasolina","320 km/h", "5 pasajeros", "WRX", "2025","750,000")

subaru.encender()
subaru.apagar()
subaru.acelerar()
subaru.frenar()
subaru.tocar()

    

