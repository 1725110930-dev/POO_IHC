class Car:
    def __init__(self, brand, model, year, color, price, fuel_type, transmission, num_doors, mileage, license_plate):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.num_doors = num_doors
        self.mileage = mileage
        self.license_plate = license_plate
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"The {self.brand} {self.model} has started."

    def stop(self):
        self.is_running = False
        return f"The {self.brand} {self.model} has stopped."

    def drive(self, distance):
        self.mileage += distance
        return f"You drove {distance} km. Total mileage: {self.mileage} km."

    def repaint(self, new_color):
        self.color = new_color
        return f"The car is now {self.color}."

    def applyDiscount(self, discount_amount):
        self.price -= discount_amount
        return f"New price after discount: ${self.price}"


my_car = Car("Toyota", "Tacoma", 2026, "Gray", 950000, "Hybrid", "Automatic", 4, 0, "TCM-2026")

print(my_car.start())
print(my_car.drive(120))
print(my_car.repaint("Black"))
print(my_car.applyDiscount(50000))
print(my_car.stop())
