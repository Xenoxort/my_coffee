from MENU import menu
from money import Money
from resources import *

#Resource Class
res_class = Resources()
resources = res_class.resources

#Money Class
my_money = Money()
resources["Money"] = my_money.money

#Coffee loop
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
        print("AMAZING")
        enough_resources = res_class.check_resources(choice)

        #Money will be checked only if there is enough resources
        if enough_resources:
            enough_money = my_money.money_check(choice)

            #Deducting resources when there is enough resource and money
            if enough_money:
                res_class.deduct_resources()
                resources = res_class.resources
                resources["Money"] = my_money.money



