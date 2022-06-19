MENU = {
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    # TODO report
    print(f"Money taken: {profit}\n{resources}")



def check_resources(choice):
    for key, amount_required in MENU[choice]["ingredients"].items():
        if amount_required >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return True

def process_coins():
    total = int(input("How many quarters .. "))*0.25
    total += int(input("How many nickels .. "))*0.1
    total += int(input("How many dimes .. "))*0.05
    total += int(input("How many pennies .. "))*0.01

    return total

def check_money(cost, coins):

    if cost > coins:
        print("Sorry that's not enough money. Money refunded.")
        status = False
    elif cost < coins:
        print(f"Here is ${coins - cost} dollars in change.")
        status = True
    else:
        status = True

    return status

def vend(choice):
    print("Vending .... ")
    global profit
    global resources
    profit += MENU[choice]["cost"]
    for item, qty in MENU[choice]["ingredients"].items():
        resources[item] -= qty

def main():

    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice.lower() == "off":
        exit()
    elif choice.lower() == "report":
        report()
        return

    if choice in MENU:
        print(choice)
        if check_resources(choice):
            total = process_coins()
            if check_money(MENU[choice]["cost"], total):
                vend(choice)
    else:
        print("Please choose a drink from the list")
        return

if __name__ == "__main__":
    while True:
        main()