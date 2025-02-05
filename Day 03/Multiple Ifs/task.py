print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Kids Ticket price is $5.")
        bill = 5
    elif age <= 18:
        print("Youth Ticket price is $7.")
        bill = 7
    else:
        print("Adult Ticket price is $12.")
        bill = 12
    photo = input("Want the photo ?, if yes enter 'y' else 'n':")
    if photo == "y":
        bill +=3

        print(f"Your total bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
