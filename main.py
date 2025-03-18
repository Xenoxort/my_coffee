from MENU import menu
from money import Money

#espresso = menu["Espresso"]
#latte = menu["Latte"]
#cappuccino = menu["Cappuccino"]

base_resources = {
    "Water": 300,
    "Coffee": 100,
    "Milk": 200,

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

    #Checking Resources
    else:
        ingr = menu[choice.title()]["ingredients"]
        if resources["Water"] < ingr["Water"]:
            print("Sorry there is not enough water.")
        if resources["Coffee"] < ingr["Coffee"]:
            print("Sorry there is not enough coffee.")
        if resources["Milk"] < ingr["Milk"]:
            print("Sorry there is not enough milk.")

        else:
            print("AMAZING")

            #Money will be checked only if there is enough resources
            enough_money = my_money.money_check(choice)
            resources["Money"] = my_money.money

            #Deducting resources when there is enough resource and money
            if enough_money:
                resources["Water"] -= ingr["Water"]
                resources["Coffee"] -= ingr["Coffee"]
                resources["Milk"] -= ingr["Milk"]



