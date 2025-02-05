import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def rand_card(ar):
    return ar[random.randint(0,12)]

def sum_check(ar):
    if sum(ar)>=22:
        if ar[0] == 11:
            ar[0]=1
    else:
        ar[1]=1
    return ar

def comp_game(ar):
    check = True
    while check:
        if sum(ar) <= 17:
            ar.append(rand_card(cards))
            check = True
            print("Computer picked a card!")
        elif 18 <= sum(ar) < 21:
            a = random.randint(0,1)
            if a == 0:
                ar.append(rand_card(cards))
                check = True
                print("Computer picked a card!")
            else:
                check = False
        else:
            check = False
    return ar

def win_check(ar,br):
    br = comp_game(br)
    br_dis = abs(21 - sum(br))
    ar_dis = abs(21 - sum(ar))
    if br_dis == ar_dis:
        print(f"Your Cards are :{ar}, The total is {sum(ar)}.")
        print(f"Computer Cards are :{br}, The total is {sum(br)}.")
        print("It's a Draw!")
    elif br_dis > ar_dis:
        print(f"Your Cards are :{ar}, The total is {sum(ar)}.")
        print(f"Computer Cards are :{br}, The total is {sum(br)}.")
        print("You Won!!!")
    else:
        print(f"Your Cards are :{ar}, The total is {sum(ar)}.")
        print(f"Computer Cards are :{br}, The total is {sum(br)}.")
        print("Computer Won!!!")

check2 = True
while check2:
    start_game = input("Do you want to play a game of Blackjack(21) ?\n If yes type 'y', otherwise 'n' or anything!")
    if start_game == 'y':
        computer = [rand_card(cards),rand_card(cards)]
        player = [rand_card(cards),rand_card(cards)]

        computer = sum_check(computer)
        player = sum_check(player)

        print(f"Your Cards are :{player}, The total is {sum(player)}.")
        comp_card = computer[random.randint(0,1)]
        print(f"The computer card is {comp_card}.")

        check1 = True

        while check1:
            hit_stand = input("Type 'y' to add a card or 'n' to pass").lower()
            if hit_stand == 'y':
                player.append(rand_card(cards))
                print(f"Your Cards are :{player}, The total is {sum(player)}.")
                if sum(player)>21:
                    print(f"Your total is {sum(player)}, it greater than 21, COMPUTER WON!!!")
                    computer = comp_card
                    print(f"The Computer Card is : {computer}")
                    check1 = False
                elif sum(player)<21:
                    check1 = True
                else:
                    if sum(player)==21 and len(player)==2:
                        print(f"Your cards are {player} and you with a BlackJack!")
                        check1 = False
                    else:
                        win_check(player,computer)
                        check1 = False
            else:
                win_check(player,computer)
                check1 = False
        check2 = True
    else:
        check2 = False