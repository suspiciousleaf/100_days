# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_16/day_16_env/Scripts/Activate.ps1

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()

coffe_maker = CoffeeMaker()

menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    prompt = input(f"\nWhat would you like? ({options}): ")
    if prompt == "off":
        is_on = False
    elif prompt == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(prompt)
        if coffe_maker.is_resource_sufficient(drink):
            price = drink.cost
            print(f"Please insert: ${price:.2f}")
            if money_machine.make_payment(price):
                coffe_maker.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")
