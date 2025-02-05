#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    start_letter = letter.read()

output_letter = ""

for name in all_names:
    i = name.strip("\n")
    output_letter = start_letter.replace("[name]", i)
    with open(f"./Output/ReadyToSend/For{i}.txt", "w")as ready:
        ready.write(output_letter)
