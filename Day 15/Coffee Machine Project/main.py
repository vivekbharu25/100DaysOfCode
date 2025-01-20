MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

sources = ["water", "milk", "coffee"]

def check_input(inp):
    if inp == "a":
        flav = MENU["espresso"]
    elif inp == "b":
        flav = MENU["latte"]
    elif inp == "c":
        flav = MENU["cappuccino"]
    elif inp == "off":
        flav = False
    else:
        flav = "Wrong"
    return flav

def check_resources(item):
    for items in sources:
        if resources[items] < item["ingredients"][items]:
            print(f"There's no enough {items}.")
            return False
        else:
            return True

def deduct_resources(item):
    for items in sources:
        resources[items] -= item["ingredients"][items]
    return resources

def trading(item):
    print(f"Let's do some trading.\n The cost is ${item["cost"]}.")
    a = int(input("How many quarters ?"))*0.25
    b = int(input("How many dimes ?"))*0.10
    c = int(input("How many five cents ?"))*0.05
    d = int(input("How many pennies ?"))*0.01
    total = round(a+b+c+d,2)
    print(total)
    if total>= item["cost"]:
        change = round(total - item["cost"],2)
        print(f"Here's your change ${change}.")
        return True
    else:
        print("Not enough money")
        return False

def disp_flav(inp):
    if inp == "a":
        return "espresso"
    elif inp == "b":
        return "latte"
    else:
        return "cappuccino"

def disp_res():
    print("Available Resources are:")
    print(f"Water - {resources["water"]}, Milk  - {resources["milk"]}, Coffee - {resources["coffee"]}")

machine = True
disp_res()
while machine:
    user_input = input("What type of coffee do you want ?\n Type 'A' - Espresso, 'B' - Latte, 'C' - Cappuccino.").lower()
    try:
        coffee_input = check_input(user_input)
        if not coffee_input:
            machine = False
        else:
            if check_resources(coffee_input):
                if trading(coffee_input):
                    print(f"Enjoy your {disp_flav(user_input)}.")
                    resources = deduct_resources(coffee_input)
                    disp_res()
                else:
                    print("Try Again!")
    except TypeError:
        print("Give correct input.")