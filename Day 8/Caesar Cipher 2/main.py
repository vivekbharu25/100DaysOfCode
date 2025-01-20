alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caeser(dir):
    def encrypt(texta, shifta):
        etext = []
        for i in range(len(texta)):
            if texta[i] not in alphabet:
                etext.append(texta[i])
            else:
                index_val = alphabet.index(texta[i])
                change_num = index_val+shifta
                change_num %= len(alphabet)
                etext.append(alphabet[change_num])

        print("".join(etext))

    def decrypt(texta, shifta):
        etext = []
        for i in range(len(texta)):
            if texta[i] not in alphabet:
                etext.append(texta[i])
            else:
                index_val = alphabet.index(texta[i])
                change_num = index_val-shifta
                change_num %= len(alphabet)
                etext.append(alphabet[change_num])

        print("".join(etext))
    if dir == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif dir == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Give a proper input")

caeser(direction)







