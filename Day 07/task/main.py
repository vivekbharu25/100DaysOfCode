import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

lives = 6

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
count = 0
display = ["_"]*word_length
print("".join(display))

while lives != 0 :
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    temp_num = 0
    for i in range(word_length):

        if guess == chosen_word[i]:
            if display[i]=="_":
                display[i] = guess
                count+=1
            else:
                print(f"The Letter {guess}, is already present")
        else:
            temp_num +=1

    if temp_num == word_length:
        lives -=1
        print(f"The letter {guess}, is not there, One Life Fasak!")
        print(stages[lives])


    print("".join(display))

    if count == word_length:
        lives = 0
        print("Sooper ra Bittu!")
        print("****************************YOU WIN****************************")
    elif lives == 0:
        print("Gangaarpanam!!!")
        print("****************************YOU LOSE****************************")
        print(f"The word is: {chosen_word}")



# game_over = False
# correct_letters = []
#
# while not game_over:
#
#     # TODO-6: - Update the code below to tell the user how many lives they have left.
#     print("****************************<???>/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()
#
#     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print("Word to guess: " + display)
#
#     # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#     #  e.g. You guessed d, that's not in the word. You lose a life.
#
#     if guess not in chosen_word:
#         lives -= 1
#
#         if lives == 0:
#             game_over = True
#
#             # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
#             print(f"***********************YOU LOSE**********************")
#
#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")
#
#     # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
#     print(stages[lives])
