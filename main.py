from MENU import menu
from money import Money

#espresso = menu["Espresso"]
#latte = menu["Latte"]
#cappuccino = menu["Cappuccino"]

base_resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}

resources = base_resources.copy()
my_money = Money()
resources["Money"] = my_money.money
is_on = True

while is_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    elif choice == "off":
        is_on = False

    #Checking and updating money
    else:
        my_money.money_check(choice)
        resources["Money"] = my_money.money


