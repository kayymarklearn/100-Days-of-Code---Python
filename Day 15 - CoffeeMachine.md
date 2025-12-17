2025-12-17 21:27

Status: Completed

Tags: 


# Coffe Machine

## Todo: Program Logic

## Code: Project Code
main.py 
```
import sys  
  
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
# Global variables to use  
machine_on = True  
money = 0  
sales = 0  
  
# TODO 2. display available resources when maintainers inputs report.  
def print_report():  
    print("Available resources")  
    for ingredient in resources:  
        print(f"{ingredient}: {resources[ingredient]}")  
    print(f"Money: ${sales}")  
  
# TODO 3. off the machine when maintainers input 'off'  
def off_machine():  
    sys.exit(0)  
  
  
# TODO 4. Check quantity for each type of coffee  
def check_resources(menu_choice):  
# 1. Espresso: 50ml water, 18g Coffee  
    if menu_choice == "espresso":  
        if resources["water"] >= 50 and resources["coffee"] >= 18:  
            return True  
        else:  
            return False  
    elif menu_choice == "latte":  
# 2. Latte:     200ml water, 24g coffee, 150ml milk  
        if resources["water"] >= 200 and resources["milk"] >= 100 and resources["coffee"] >= 24:  
            return True  
        else:  
            return False  
    else:  
# 3. Cappuccino: 250ml water, 24g coffee, 100ml milk  
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:  
            return True  
        else:  
            return False  
  
# TODO 6. Ask user for money and check.  
def take_money():  
    print("Please insert coins.")  
    try:  
        quarters = int(input("How many quarters?: "))  
        dimes = int(input("How many dimes?: "))  
        nickels = int(input("How many nickels?: "))  
        pennies = int(input("How many pennies?: "))  
        amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)  
        return amount  
    except ValueError:  
        print("Please insert a valid coin")  
  
# TODO 7. Check if the money coins can buy the coffee  
def check_money(amount: float, coffee: str):  
    change = 0  
    if amount < MENU[coffee]["cost"]:  
        return [None, False]  
    else:  
        if amount > MENU[coffee]["cost"]:  
            change = amount - MENU[coffee]["cost"]  
        return [change, True]  
  
# TODO 8. this function will update the resources in our resources dictionary  
def update_resources(menu_choice):  
    resources["water"] -= MENU[menu_choice]["ingredients"]["water"]  
    resources["coffee"] -= MENU[menu_choice]["ingredients"]["coffee"]  
    if menu_choice == "latte" or menu_choice == "cappuccino":  
        resources["milk"] -= MENU[menu_choice]["ingredients"]["milk"]  
  
  
  
# TODO 5. Keep running the machine till turned off  
while machine_on:  
    # TODO 1. prompt user for an order/command  
    prompt = input("What would you like? (espresso, latte, cappuccino): ").lower()  
    if prompt == "off":  
        off_machine()  
    elif prompt == "report":  
        print_report()  
    elif prompt in ['espresso', 'latte', 'cappuccino']:  
        if check_resources(prompt):  
            money = take_money()  
            transaction = check_money(money, prompt)  
            if transaction[1]:  
                if transaction[0] > 0:  
                    print(f"Here is ${round(transaction[0], 2)} in change.")  
                print(f"Here is your {prompt}. Enjoy!")  
                update_resources(prompt)  
                sales += money - transaction[0]  
            else:  
                print(f"Sorry, that's not enough money. ${money} refunded!")  
        else:  
            print("Ingredients not available! Money refunded.")  
    else:  
        print("Sorry! Not on the menu.")
```



## References

