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
        

    def occupy(self, guests):
        if guests <= self.capacity:
            self.is_occupied = True
            self.current_guests = guests
            return f"The table is now occupied by {self.current_guests} guests."
        return f"Cannot occupy. The table only has a capacity of {self.capacity}."

    def release(self):
        self.is_occupied = False
        self.current_guests = 0
        return "The table is now empty and clean."

    def change_color(self, new_color):
        self.color = new_color
        return f"The table has been painted {self.color}."

    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        return f"New price after a {percentage}% discount: ${self.price:.2f}"

    def extend(self):
        if self.is_extendable:
            self.capacity += 2
            self.length += 50
            return f"Table extended. New capacity: {self.capacity} guests. New length: {self.length}cm."
        return "This table cannot be extended."


my_table = Table("Oak Wood", "Brown", 4, 250.00, 75, 90, 140, "Rectangular", "HomeDecor", True)

print(my_table.occupy(3))
print(my_table.extend())
print(my_table.occupy(6))
print(my_table.apply_discount(15))
print(my_table.release())