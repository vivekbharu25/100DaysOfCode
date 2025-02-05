import pandas as pd


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
speak_is_on = True

while speak_is_on:
    user_name = input("What's your name or what do you want to spell ?").upper()
    if user_name == "EXIT":
        break
    else:
        try:
            user_nato = [nato_dict[letter] for letter in user_name]
        except KeyError:
            print("Sorry, Letters only.")
        else:
            print(user_nato)