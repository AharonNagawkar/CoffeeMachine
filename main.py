from resources import COINS, MENU, resources


def report():
    print(f" Water:  {resources['water']}ml \n"
          f" Milk:   {resources['milk']}ml \n"
          f" Coffee: {resources['coffee']}g \n"
          f" Money:  ${profit}")


def prompt():
    options = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    user_selection = input('What would you like? (espresso/latte/cappuccino):\n').lower()
    while user_selection not in options:
        user_selection = input('What would you like? (espresso/latte/cappuccino):\n').lower()
    return user_selection


def process_coins():
    coins = [
        int(input("How many pennies?")),
        int(input("How many nickles?")),
        int(input("How many dimes?")),
        int(input("How many quarters?"))
    ]
    pennies = COINS['pennies']*coins[0]
    nickles = COINS['nickles']*coins[1]
    dimes = COINS['dimes']*coins[2]
    quarters = COINS['quarters']*coins[3]
    return round(pennies + nickles + dimes + quarters, 2)


def check_ingredients(selection):
    for ingredient in MENU[selection]['ingredients']:
        if resources[ingredient] < MENU[selection]['ingredients'][ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return False
    return True


def prepare_coffee(selection):
    for ingredient in MENU[selection]['ingredients']:
        resources[ingredient] -= MENU[selection]['ingredients'][ingredient]
    print(f"Here's your {selection} ☕. Enjoy! ")
    return MENU[selection]['cost']


def check_cost(selection):
    return MONEY >= MENU[selection]['cost']


profit = 0
while True:
    user = prompt()
    if user == 'off':
        break
    elif user == 'report':
        report()
    else:
        if check_ingredients(user):
            MONEY = process_coins()
            if check_cost(user):
                profit += prepare_coffee(user)
                change = MONEY - MENU[user]['cost']
                print(f"“Here is ${round(change, 2)} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
