from MENU import menu

BASE_RESOURCES = {
    "Water": 300,
    "Coffee": 100,
    "Milk": 200,
}

class Resources:
    def __init__(self):
        self.resources = BASE_RESOURCES.copy()
        self.ingr = {}


    def check_resources(self, choice):
        enough = False
        self.ingr = menu[choice.title()]["ingredients"]
        if self.resources["Water"] < self.ingr["Water"]:
            print("Sorry there is not enough water.")
        if self.resources["Coffee"] < self.ingr["Coffee"]:
            print("Sorry there is not enough coffee.")
        if self.resources["Milk"] < self.ingr["Milk"]:
            print("Sorry there is not enough milk.")
        else:
            enough = True

        return enough

    def deduct_resources(self):
        self.resources["Water"] -= self.ingr["Water"]
        self.resources["Coffee"] -= self.ingr["Coffee"]
        self.resources["Milk"] -= self.ingr["Milk"]

