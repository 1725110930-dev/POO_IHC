class Banco:
    def __init__(self, nombre, clientes, cajeros, capital, color, horario, num_edificios, sistema, personal_seg):
        self.nombre = nombre
        self.clientes = clientes
        self.cajeros = cajeros
        self.capital = capital
        self.color = color
        self.horario = horario
        self.num_edificios = num_edificios
        self.sistema = sistema
        self.personal_seg = personal_seg

    def mostrar_datos(self):
        print("Nombre del banco:", self.nombre)
        print("Número de clientes:", self.clientes)
        print("Número de cajeros:", self.cajeros)
        print("Capital:", self.capital)
        print("Color del banco:", self.color)
        print("Horario de atención:", self.horario)
        print("Edificios activos:", self.num_edificios)

    def registrar_cliente(self):
        self.clientes += 1
        return f"¡Nuevo cliente registrado! Total de clientes: {self.clientes}"

    def procesar_deposito(self, monto):
        self.capital += monto
        return f"Depósito exitoso. Nuevo capital del banco: {self.capital}"

    def actualizar_seguridad(self, nuevos_guardias):
        self.personal_seg += nuevos_guardias
        return f"Seguridad reforzada. Total de guardias: {self.personal_seg}"

    def simular_asalto(self, monto_robado):
        if self.personal_seg >= 5:
            return "El intento de asalto fue frustrado por el personal de seguridad."
        else:
            self.capital -= monto_robado
            return f"Alerta: El asalto tuvo éxito. Se perdieron {monto_robado}. Capital restante: {self.capital}"


banco1 = Banco(
    "Banco Azteca",
    5000,
    20,
    1000000,
    "Verde",
    "9:00 a 17:00",
    12,
    "Linux Server",
    3
)

banco1.mostrar_datos()
print("-" * 30)
print(banco1.registrar_cliente())
print(banco1.procesar_deposito(50000))
print(banco1.simular_asalto(200000))
print(banco1.actualizar_seguridad(4))
print(banco1.simular_asalto(200000))