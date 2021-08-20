from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
options = menu.get_items()

machine_on = True
while machine_on:
    customer = input(f'What would you like? ({options}):').lower()
    if customer == 'off':
        machine_on = False
    elif customer == 'report':
        coffee_maker.report()
    else:
        if customer in options:
            drink = menu.find_drink(customer)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print('Please type a valid request')




