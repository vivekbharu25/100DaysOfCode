import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
fig_list = [rock, paper, scissors]
num = int(input("Choose '0' for Rock, '1' for Paper and '2' for Scissors"))
if 0<= num <= 2:
    print(f"You Chose: \n {fig_list[num]}")
comp_num = random.randint(0,2)
print(f"Computer Chose: \n {fig_list[comp_num]}")

if num == comp_num:
    print("It's a Draw")
elif num == 0:
    if comp_num == 1:
        print("You Lost!")
    else:
        print("You Won")
elif num == 1:
    if comp_num == 0:
        print("You Won!")
    else:
        print("You Lost!")
elif num == 2:
    if comp_num == 0:
        print("You Lost!")
    else:
        print("You Won!")
else:
    print("You Chose invalid Number, You Lost!")