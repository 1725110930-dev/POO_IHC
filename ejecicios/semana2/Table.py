class Table:
    def __init__(self, material, color, capacity, price, height, width, length, shape, brand, is_extendable):
        self.material = material
        self.color = color
        self.capacity = capacity
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.shape = shape
        self.brand = brand
        self.is_extendable = is_extendable
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True
        return "The table is now occupied."

    def release(self):
        self.is_occupied = False
        return "The table is now free."

    def changeColor(self, new_color):
        self.color = new_color
        return f"The table color is now {self.color}."

    def applyDiscount(self, percentage):
        self.price -= self.price * (percentage / 100)
        return f"New price: ${self.price:.2f}"

    def extend(self):
        if self.is_extendable:
            self.capacity += 2
            return f"Table extended. New capacity: {self.capacity}."
        return "This table cannot be extended."


my_table = Table("Oak Wood", "Brown", 4, 250.00, 75, 90, 140, "Rectangular", "HomeDecor", True)

print(my_table.occupy())
print(my_table.extend())
print(my_table.applyDiscount(15))
print(my_table.release())
