# Reverse a String - Enter a string and the program will reverse it and print it out.

def val_input(string):
    if " " in string:
        for char in string:
            if char.isdigit():
                return "NOT A STRING!!"

            elif char.isalpha() | char.isspace():
                return string[::-1]

    else:
        for char in string:
            if char.isdigit():
                return "NOT A STRING!!"

            elif char.isalpha() | char.isspace():
                return string[::-1]

def reversed():
    i = input("Give a string:")
    print(val_input(i))

if __name__ == '__main__':
    reversed()
