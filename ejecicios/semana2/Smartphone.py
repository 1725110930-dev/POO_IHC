class Smartphone:

    def __init__(self, material, tamaño, entrada, bocina,
                 pantalla, botones, resistencia, funda, cargador):

        self.material = material
        self.tamaño = tamaño
        self.entrada = entrada
        self.bocina = bocina
        self.pantalla = pantalla
        self.botones = botones
        self.resistencia = resistencia
        self.funda = funda
        self.cargador = cargador

    def mostrar_datos(self):

        print("Material:", self.material)
        print("Tamaño:", self.tamaño)
        print("Tipo de entrada:", self.entrada)
        print("Bocina:", self.bocina)
        print("Pantalla:", self.pantalla)
        print("Botones:", self.botones)
        print("Resistencia:", self.resistencia)
        print("Funda:", self.funda)
        print("Cargador:", self.cargador)

telefono1 = Smartphone(
    "Aluminio",
    "Mediano",
    "Tipo C",
    "Stereo",
    "LCD",
    3,
    "IP68",
    "Silicona",
    "45W"
)

telefono1.mostrar_datos()