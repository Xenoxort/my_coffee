from MENU import menu

class Money:
    def __init__(self):
        self.money = 0


    def money_check(self, choice):
        coffee = menu[choice.title()] #get the ingredients and cost
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        money_in = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        cost = coffee["cost"]

        if money_in < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${(money_in - cost):.2f} in change.")
            print("Here is your espresso. Enjoy!")
            self.money += cost
