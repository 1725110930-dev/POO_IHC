class Chair:
    def __init__(self, material, color, price, weight_capacity, height, armrests, wheels, brand, model, style):
        self.material = material
        self.color = color
        self.price = price
        self.weight_capacity = weight_capacity
        self.height = height
        self.armrests = armrests
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.style = style
        self.is_occupied = False
        self.current_height = height

    def occupy(self):
        if not self.is_occupied:
            self.is_occupied = True
            return "The chair is now occupied."
        return "The chair is already occupied."

    def release(self):
        if self.is_occupied:
            self.is_occupied = False
            return "The chair is now free."
        return "The chair was already empty."

    def ajustHeight(self, new_height):
        if self.wheels or self.style == "Office":
            self.current_height = new_height
            return f"Height adjusted to {self.current_height} cm."
        return "This chair height cannot be adjusted."

    def changeColor(self, new_color):
        self.color = new_color
        return f"The chair color has been changed to {self.color}."

    def applyDiscount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        return f"Discount applied. New price: ${self.price:.2f}"


my_chair = Chair("Mesh Fabric", "Black", 150.00, 120, 100, True, True, "ErgoSeat", "X-200", "Office")

print(my_chair.occupy())
print(my_chair.ajustHeight(115))
print(my_chair.changeColor("Gray"))
print(my_chair.applyDiscount(10))
print(my_chair.vacate())
