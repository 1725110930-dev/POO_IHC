class Smartphone:
    def __init__(self, material, size, port_type, speaker, screen, buttons, resistance, case, charger, brand):
        self.material = material
        self.size = size
        self.port_type = port_type
        self.speaker = speaker
        self.screen = screen
        self.buttons = buttons
        self.resistance = resistance
        self.case = case
        self.charger = charger
        self.brand = brand
        self.battery_level = 100

    def displayData(self):
        print("Material:", self.material)
        print("Size:", self.size)
        print("Port Type:", self.port_type)
        print("Speaker:", self.speaker)
        print("Screen:", self.screen)
        print("Buttons:", self.buttons)
        print("Resistance:", self.resistance)
        print("Case:", self.case)
        print("Charger:", self.charger)
        print("Brand:", self.brand)

    def useApp(self, app_name):
        self.battery_level -= 5
        return f"Using {app_name}. Battery level is now {self.battery_level}%."

    def chargePhone(self):
        self.battery_level = 100
        return f"Phone charged with the {self.charger} charger. Battery is at 100%."

    def changeCasePhone(self, new_case):
        self.case = new_case
        return f"The case was changed to a {self.case} case."

    def breakScreen(self):
        self.screen = "Broken LCD"
        return "Oh no! The screen is now broken."


phone1 = Smartphone(
    "Aluminum",
    "Medium",
    "Type C",
    "Stereo",
    "LCD",
    3,
    "IP68",
    "Silicone",
    "45W",
    "Samsung"
)

phone1.displayData()
print("-" * 30)
print(phone1.useApp("Instagram"))
print(phone1.breakScreen())
print(phone1.changeCasePhone("Leather"))
print(phone1.chargePhone())
