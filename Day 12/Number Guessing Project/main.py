import random

levels = {
    "e": 10, "m": 7, "h":5
}

play = True

def gameplay(a,c,d):
    while c >=0 or d:
      if c == 0:
        print("You Lose")
        d = False
        c-=1
      else:
        print(f"You have {c} lives left.")
        b = input("Guess a Number")
        if int(b) > a:
            c -= 1
            print(f"Too High!\n")
            d = True
        elif int(b) < a:
            c-= 1
            print(f"Too Low!\n")
            d = True
        elif int(b) == a:
            c = -1
            print(f"You Won! Enjoy Pandago!!")
            d = False
        else:
            c -= 1
            print(f"Give proper Input.")
            d = True

while play:
    play_input = input("If you want to play 'Guess the Number'. Type 'y' to play and 'n' or anything else otherwise.").lower()
    if play_input == "y":
        play = True
        lives = 0
        while lives == 0:
            level_input = input("Which level do you want to play?\n Type 'e' for easy, 'm' for medium and 'h' for hard: ").lower()
            if level_input not in levels:
                print("Give Proper input level")
                lives = 0
            else:
                lives = levels[level_input]
        x = random.randint(1,100)
        game = True
        gameplay(x,lives, game)
    else:
        play = False