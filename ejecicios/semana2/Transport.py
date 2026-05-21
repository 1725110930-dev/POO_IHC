class Transport:
    def __init__(self, brand, model, color, year, fuel_type, max_speed, num_doors, num_passengers, license_plate, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.num_doors = num_doors
        self.num_passengers = num_passengers
        self.license_plate = license_plate
        self.price = price

    def turnOn(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turnOff(self):
        print(f"{self.brand} {self.model} is turned off.")

    def accelerate(self):
        print(f"{self.brand} {self.model} is accelerating.")

    def brake(self):
        print(f"{self.brand} {self.model} is braking.") 

    def honk(self):
        print(f"{self.brand} {self.model} is honking the horn.")


tacoma = Transport(
    "Toyota",
    "Tacoma",
    "Magnetic Gray",
    "2026",
    "Hybrid / Gas",
    "180 km/h",
    4,
    "5 passengers",
    "TCM-2026",
    "950,000"
)

tacoma.turnOn()
tacoma.accelerate()
tacoma.brake()
tacoma.honk()
tacoma.turnOff()
