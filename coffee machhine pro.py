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

money = 0
working = True


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def coin():
    print("Please insert coin!")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def successful(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is the extra change {change}")
        global money
        money += cost
        return True
    else:
        print("Sorry the money is refunded!")


def resource_deduct(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your{drink_name}")


while working:
    user_choice = input("What would you like to have? Espresso/ Latte/ Cappuccino").lower()
    if user_choice == "off":
        working = False
    elif user_choice == "report":
        print(f" Water:{ resources['water']}ml\n"
              f" Milk: {resources['milk']}ml\n"
              f" Coffee: {resources['coffee']}g\n"
              f" Money: {money} $")
    else:
        drink = MENU[user_choice]
        if resource_sufficient(drink["ingredients"]):
            bill = coin()
            if successful(bill, drink["cost"]):
                resource_deduct(user_choice, drink["ingredients"])





