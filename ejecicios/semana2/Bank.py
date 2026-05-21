class Bank:
    def __init__(self, name, clients, atms, capital, color, schedule, branch_office, system, security_staff):
        self.name = name
        self.clients = clients
        self.atms = atms
        self.capital = capital
        self.color = color
        self.schedule = schedule
        self.branch_office = branch_office
        self.system = system
        self.security_staff = security_staff

    def displayData(self):
        print("Bank Name:", self.name)
        print("Clients:", self.clients)
        print("ATMs:", self.atms)
        print("Capital:", self.capital)
        print("Color:", self.color)
        print("Schedule:", self.schedule)
        print("Buildings:", self.branch_office)
        print("System:", self.system)
        print("Security Staff:", self.security_staff)

    def addClient(self):
        self.clients += 1
        return f"Client added. Total: {self.clients}"

    def addCapital(self, amount):
        self.capital += amount
        return f"Capital increased by {amount}. Total: {self.capital}"

    def hireSecurity(self, count):
        self.security_staff += count
        return f"Hired {count} guards. Total: {self.security_staff}"

    def loseCapital(self, amount):
        self.capital -= amount
        return f"Lost {amount} from capital. Remaining: {self.capital}"


bank1 = Bank(
    "Banco Azteca",
    5000,
    20,
    1000000,
    "Green",
    "9:00 to 17:00",
    12,
    "Linux Server",
    3
)

bank1.displayData()
print("-" * 30)
print(bank1.addClient())
print(bank1.addCapital(50000))
print(bank1.hireCecurity(4))
print(bank1.loseCapital(200000))
