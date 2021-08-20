menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

bank = 0


def refill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


def is_resource_sufficient(order_ingredients):
    """"Checks to see if you the coffee machine has enough resources for the order that was given """
    for item in menu[order_ingredients]['ingredients']:
        if resources[item] >= menu[order_ingredients]['ingredients'][item]:
            print(f'sufficient {item}')
            resources[item] -= menu[order_ingredients]['ingredients'][item]
        else:
            print(f'insufficient {item}')
            return False
    return True


def coin_machine(coffee):
    """Calculates the coins that you put in and checks if they are enough for the asked coffee"""
    global bank
    money = int(input('posa 0.05?')) * 0.05
    money += int(input('posa 0.10?')) * 0.1
    money += int(input('posa 0.20?')) * 0.2
    money += int(input('posa 0.50?')) * 0.5
    money += int(input('posa 1?')) * 1
    money += int(input('posa 2?')) * 2

    if money >= menu[coffee]['cost']:
        payment = money - menu[coffee]['cost']
        print("Your payment is complete\n"
              f"Here is your change {payment}")
        bank += money - payment
    else:
        need_another = menu[coffee]['cost'] - money
        print(f"Sorry mate that was {need_another} sort ")
        print(f"Returning {money}")


machine_open = True
while machine_open:
    customer = input('ti teleis a?').lower()
    if customer == 'off':
        print('Machine shutting down')
        machine_open = False
    elif customer == 'report':
        print(f"Water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {bank}")
    elif is_resource_sufficient(customer):
        print(f'preparing your {customer} Sir')
        coin_machine(customer)
    elif not is_resource_sufficient(customer):
        print(f"Sorry Sir we can't prepare your {customer} because we don't have enough resources")
        want_to_refill = input("Would you like to refill?\n"
                               "Type YES if so").upper()
        if want_to_refill == 'YES':
            refill()




















