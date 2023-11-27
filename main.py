from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

working_now = True
coffee_maker = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()

while working_now:
    drink_list = coffee_menu.get_items()
    user_choice = input(f'What would you like from the list {drink_list})? Or choose manually: ')

    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice in ('espresso', 'latte', 'cappuccino'):
        drink = coffee_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f'Please pay {drink.cost}')
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        working_now = False
