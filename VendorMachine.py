
water = 400
milk = 540
beans = 120
cups = 9
money = 550



class LackResourceError(Exception):
    pass


def print_status():
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')

def select_action():
    return input("Write action (buy, fill, take, remaining, exit): ")

def can_make_coffe(water_needed = 0, milk_needed = 0, beans_needed = 0):
    if water_needed > water:
        print('Sorry, not enough water!\n')
        raise LackResourceError
    elif milk_needed > milk:
        print('Sorry, not enough milk!\n')
        raise LackResourceError
    elif beans_needed > beans:
        print('Sorry, not enough beans!\n')
        raise LackResourceError
    elif cups < 1:
        print('Sorry, not enough cups\n')
        raise LackResourceError
    print('I have enough resources, making you a coffee!\n')

def espresso():
    global money, water, beans, cups
    water -= 250
    beans -= 16
    money += 4
    cups -= 1

def latte():
    global money, water, beans, milk, cups
    water -= 350
    milk -= 75
    beans -= 20
    money += 7
    cups -= 1

def cappucino():
    global water, milk, beans, money, cups
    water -= 200
    milk -= 100
    beans -= 12 
    money += 6
    cups -= 1

def select():
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)

def buy_coffe():
    kind = select()
    try:
        if kind == 0:
            pass
        elif kind == 1:
            can_make_coffe(water_needed=250, beans_needed=16)
            espresso()
        elif kind == 2:
            can_make_coffe(water_needed=350, milk_needed=75, beans_needed=20)
            latte()
        elif kind == 3:
            can_make_coffe(water_needed=200, milk_needed=100, beans_needed=12)
            cappucino()
        else:
            raise ValueError(f"Uknown coffe {kind}")
    except LackResourceError:
        pass

def fill():
    global water, milk, beans, cups
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))

def take():
    global money
    print(f'I gave you ${money}')
    money = 0

def main():
    
    while True:   
        action = select_action()
        if action == "buy":
            buy_coffe()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "exit":
            break
        elif action == "remaining":
            print_status()    
        else:
            raise ValueError(f'Uknown command {action}')
if __name__ == '__main__':
    main()
