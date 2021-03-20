# **Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. 
# The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). 
# The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). 
# So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.

def caepher():

    string = input("enter string: ")
    key = int(input("enter key: "))

    encryption = ''

    for char in string:

        if char == " ":

            encryption += char

        elif char.isupper():
        # chr() --> takes an integer and converts it to a character
            encryption += chr((ord(char) + key - ord('A')) %26 + ord('A'))
        # ord() --> gives ascii values of letters; e.g 65 for uppercase 'A' 97 for lowercase 'a'

        else:
            encryption += chr((ord(char) + key - ord('a')) %26 + ord('a'))

    return f"Encryption of the given string: {encryption}"

# Ave, True to Caesar

if __name__=="__main__":
    print(caepher())
