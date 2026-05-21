class RpgCharacter:
    def __init__(self, name, character_class, level, health, energy, strength, defense, agility, weapon, coins):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.health = health
        self.energy = energy
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.weapon = weapon
        self.coins = coins
        self.is_alive = True

    def takeDamage(self, damage):
        self.health -= damage
        return f"{self.name} took {damage} damage. Remaining health: {self.health}"

    def heal(self, amount):
        self.health += amount
        return f"{self.name} healed {amount} HP. Current health: {self.health}"

    def levelUp(self):
        self.level += 1
        self.strength += 5
        self.defense += 3
        return f"{self.name} leveled up to Level {self.level}! Stats increased."

    def winCoins(self, amount):
        self.coins += amount
        return f"Earned {amount} coins. Total coins: {self.coins}"

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon
        return f"{self.name} equipped a new weapon: {self.weapon}"


hero = RpgCharacter("Aragorn", "Warrior", 1, 100, 30, 15, 10, 8, "Iron Sword", 50)

print(hero.takeDamage(20))
print(hero.heal(10))
print(hero.levelUp())
print(hero.winCoins(100))
print(hero.changeWeapon("Excalibur"))
