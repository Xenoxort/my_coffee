from MENU import menu

base_resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}

resources = base_resources.copy()
is_on = True

while is_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    elif choice == "off":
        is_on = False


