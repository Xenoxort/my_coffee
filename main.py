from MENU import menu

espresso = menu["Espresso"]
latte = menu["Latte"]
cappuccino = menu["Cappuccino"]

base_resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}

resources = base_resources.copy()
resources["Money"] = 0

is_on = True

while is_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    elif choice == "espresso":

        #Money Check
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        money_in = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        cost = espresso["cost"]
        print(money_in)
        print(cost)
        if money_in < espresso["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${(money_in - cost):.2f} in change.")
            print("Here is your espresso. Enjoy!")
            resources["Money"] += cost


    elif choice == "off":
        is_on = False


