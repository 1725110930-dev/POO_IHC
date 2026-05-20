class Chair:
    def __init__(self, material, color, price, weight_capacity, height, has_armrests, has_wheels, brand, model, style):
        self.material = material
        self.color = color
        self.price = price
        self.weight_capacity = weight_capacity
        self.height = height
        self.has_armrests = has_armrests
        self.has_wheels = has_wheels
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

    def vacate(self):
        if self.is_occupied:
            self.is_occupied = False
            return "The chair is now vacant."
        return "The chair was already empty."

    def adjust_height(self, new_height):
        if self.has_wheels or self.style == "Office":
            self.current_height = new_height
            return f"Height adjusted to {self.current_height} cm."
        return "This chair height cannot be adjusted."

    def change_color(self, new_color):
        self.color = new_color
        return f"The chair color has been changed to {self.color}."

    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        return f"Discount applied. New price: ${self.price:.2f}"


my_chair = Chair("Mesh Fabric", "Black", 150.00, 120, 100, True, True, "ErgoSeat", "X-200", "Office")

print(my_chair.occupy())
print(my_chair.adjust_height(115))
print(my_chair.change_color("Gray"))
print(my_chair.apply_discount(10))
print(my_chair.vacate())