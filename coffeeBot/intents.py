# Define  functions

def coffee_bot():
    print("Welcome to the virtual cafe!")
    while True:
        size = get_size()
        drink_type = get_drink_type()
        milk_type, milk_price = '', 0.00  # Initialize milk type and price
        if drink_type == 'Latte':  # Check if the drink type is Latte
            milk_type, milk_price = get_milk_type()  # Get the selected milk type and its price
        price = get_price(size, drink_type) + milk_price  # Get the total price including the base price and milk price
        if milk_type:
            print('Alright, that\'s a {} {} with {}!'.format(size, drink_type, milk_type))
        else:
            print('Alright, that\'s a {} {}!'.format(size, drink_type))

        print('That will be ${:.2f} please.'.format(price))


        name = input('Can I get your name please? \n>').capitalize()
        print("Thanks, {}! Your drink will be ready shortly.".format(name))

        # Ask if the user wants to order again
        another_order = input("Would you like to place another order? (yes/no)\n").lower()
        if another_order not in ['yes', 'y']:  # Check if the response is neither 'yes' nor 'y'
            print("Thank you for visiting! Goodbye!")
            break


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>')

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_drink_type():
    res = input("What type of drink would you like? \n[a] Drip Coffee \n[b] Espresso \n[c] Latte \n>")

    if res == 'a':
        return 'Drip Coffee'
    elif res == 'b':
        return 'Espresso'
    elif res == 'c':
        return 'Latte'
    else:
        print_message()
        return get_drink_type()


def get_milk_type():
    milk_type = input("What kind of milk would you like? \n[a] Dairy \n[b] Soy (+$0.50) \n[c] Oat (+$0.75) \n>")
    if milk_type == 'a':
        return 'Dairy', 0.00  # No extra charge for dairy milk
    elif milk_type == 'b':
        return 'Soy', 0.50  # Additional charge of $0.50 for soy milk
    elif milk_type == 'c':
        return 'Oat', 0.75  # Additional charge of $0.75 for oat milk
    else:
        print_message()
        return get_milk_type()


def get_price(size, drink_type):
    prices = {
        'small': {'Drip Coffee': 2.00, 'Espresso': 3.00, 'Latte': 4.00},
        'medium': {'Drip Coffee': 2.50, 'Espresso': 3.50, 'Latte': 4.50},
        'large': {'Drip Coffee': 3.00, 'Espresso': 4.00, 'Latte': 5.00}
    }
    return prices[size][drink_type] if size in prices and drink_type in prices[size] else 0.00


# Call coffee_bot()!
coffee_bot()
