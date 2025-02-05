# TODO-1: Import and print the logo from art.py when the program starts.

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(texta, shifta, direc):
    etext = []
    if direc == "decode":
        shifta *= -1
    for i in range(len(texta)):
        if texta[i] not in alphabet:
            etext.append(texta[i])
        else:
            index_val = alphabet.index(texta[i])
            change_num = index_val + shifta
            change_num %= len(alphabet)
            etext.append(alphabet[change_num])

    print("".join(etext))

restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Give your Input Text: \n").lower()
    shift = int(input("Shift by how much ? \n"))

    caeser(text, shift, direction)
    restart_input = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart_input == 'no':
        restart = False
        print("Bye!")
    else:
        restart = True