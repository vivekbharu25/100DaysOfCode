import game_data
import random
import art

def profile_detailsa(item):
    print(f"Compare A: {item['name']}, a {item['description']}, from {item['country']}")
    return item['follower_count']

def profile_detailsb(item):
    print(f"Against B: {item['name']}, a {item['description']}, from {item['country']}")
    return item['follower_count']
def real_answer(a,b):
    if a>b:
        return 'a'
    else:
        return 'b'

game = True
score = 0
item_a = random.choice(game_data.data)
while game:
    item_b = random.choice(game_data.data)
    if item_b == item_a:
        item_b = random.choice(game_data.data)
    print(art.logo)
    a_fol = profile_detailsa(item_a)
    print(art.vs)
    b_fol = profile_detailsb(item_b)
    real_ans = real_answer(a_fol, b_fol)
    play_ans = input("Who has more followers 'A' or 'B'?").lower()
    if real_ans == play_ans:
        score+=1
        print("\n" * 20)
        print(f"It is correct and the current score is {score}.")
    else:
        game = False
        print(f"You Lost and your final score is {score}.")
    item_a = item_b