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

    def display_data(self):
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

    def use_app(self, app_name):
        self.battery_level -= 5
        return f"Using {app_name}. Battery level is now {self.battery_level}%."

    def charge_phone(self):
        self.battery_level = 100
        return f"Phone charged with the {self.charger} charger. Battery is at 100%."

    def change_case(self, new_case):
        self.case = new_case
        return f"The case was changed to a {self.case} case."

    def break_screen(self):
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

phone1.display_data()
print("-" * 30)
print(phone1.use_app("Instagram"))
print(phone1.break_screen())
print(phone1.change_case("Leather"))
print(phone1.charge_phone())