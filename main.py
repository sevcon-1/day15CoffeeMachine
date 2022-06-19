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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for k, v in resources.items():
        print(f"{k}: {v}")

def check_resources(drink: str):

    resources_after = {}

    for ingredient, amount in MENU[drink]["ingredients"].items():
        remaining_amount = resources[ingredient] - amount
        #print(k)
        resources_after[ingredient] = remaining_amount

        if remaining_amount < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return {}

    resources_after["money"] = 0

    return resources_after

def check_money(amount_paid: dict, drink: str):

    total_amount = amount_paid["quarters"]*0.25 + amount_paid["dimes"]*0.1 \
        + amount_paid["nickels"]*0.05 + amount_paid["pennies"]*0.01

    return MENU[drink]["cost"] - total_amount

def vend(resources_after: object):
    global resources
    resources = resources_after
    print(f"mid-vend {resources}: resources")

def main():

    choice = input("Enter Choice: ").lower()

    if choice.lower() == "report":
        report()
        return
    elif choice == "off":
        exit(0)

    # TODO Simplify  and check only 1 of 3 correct choices supplied key exists in dict
    if choice in MENU.keys():

        resources_after = check_resources(choice)

        if resources_after:

            # TODO check money
            print("Please insert coins")
            try:
                money = {}
                # TODO check when amount has been reached?
                money["quarters"] = int(input("quarters = "))
                money["dimes"] = int(input("dimes = "))
                money["nickels"] = int(input("nickels = "))
                money["pennies"] = int(input("pennies = "))

                under_over_amt = check_money(money, choice)

                if under_over_amt > 0:
                    #Change is due
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${abs(under_over_amt)} change")
                    resources_after["money"] += MENU[choice]["cost"]
                    print("Vending ....")
                    print(f"Enjoy your {choice}!")
                    vend(resources_after)
                    print(f"post-vend {resources}: resources")

            except ValueError:
                print("Invalid coins ....")
                exit(1)

        else:
            print("Error - Please report to facilities")

    else:
        print("Please make another choice ")
        # TODO Offer a new choice or quit

if __name__ == "__main__":

    while True:
        main()
        print(resources)