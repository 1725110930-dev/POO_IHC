class Dog:
    def __init__(self, name, breed, age, color, size, weight, owner_name, rabies_vaccine, energy, hunger):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.size = size
        self.weight = weight
        self.owner_name = owner_name
        self.rabies_vaccine = rabies_vaccine
        self.energy = energy
        self.hunger = hunger
        self.is_sleeping = False

    def displayData(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Owner:", self.owner_name)
        print("Rabies Vaccine?:", self.rabies_vaccine)

    def bark(self):
        return f"{self.name} says Woof Woof!"

    def eat(self, food_amount):
        self.hunger -= food_amount
        self.weight += 0.2
        return f"{self.name} has eaten. Hunger level dropped to {self.hunger}."

    def play(self):
        self.energy -= 20
        self.hunger += 10
        return f"{self.name} ran around the park. Current energy: {self.energy}%."

    def sleep(self):
        self.is_sleeping = True
        self.energy = 100
        return f"{self.name} fell asleep and recovered all their energy."


my_dog = Dog("Max", "Labrador", 3, "Golden", "Large", 30.5, "Ivan", True, 80, 40)

print(my_dog.bark())
my_dog.displayData()
print("-" * 30)
print(my_dog.eat(15))
print(my_dog.play())
print(my_dog.sleep())
