class Bank:
    def __init__(self, name, clients, atms, capital, color, schedule, num_buildings, system, security_staff):
        self.name = name
        self.clients = clients
        self.atms = atms
        self.capital = capital
        self.color = color
        self.schedule = schedule
        self.num_buildings = num_buildings
        self.system = system
        self.security_staff = security_staff

    def display_data(self):
        print("Bank Name:", self.name)
        print("Number of clients:", self.clients)
        print("Number of ATMs:", self.atms)
        print("Capital:", self.capital)
        print("Bank color:", self.color)
        print("Business hours:", self.schedule)
        print("Active buildings:", self.num_buildings)

    def register_client(self):
        self.clients += 1
        return f"New client registered! Total clients: {self.clients}"

    def process_deposit(self, amount):
        self.capital += amount
        return f"Deposit successful. New bank capital: {self.capital}"

    def upgrade_security(self, new_guards):
        self.security_staff += new_guards
        return f"Security reinforced. Total guards: {self.security_staff}"

    def simulate_robbery(self, stolen_amount):
        if self.security_staff >= 5:
            return "The robbery attempt was thwarted by security staff."
        else:
            self.capital -= stolen_amount
            return f"Alert: The robbery was successful. {stolen_amount} was lost. Remaining capital: {self.capital}"


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

bank1.display_data()
print("-" * 30)
print(bank1.register_client())
print(bank1.process_deposit(50000))
print(bank1.simulate_robbery(200000))
print(bank1.upgrade_security(4))
print(bank1.simulate_robbery(200000))