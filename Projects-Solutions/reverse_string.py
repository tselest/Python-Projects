# Reverse a String - Enter a string and the program will reverse it and print it out.

def val_input(string):
    if any(map(str.isdigit, string))==True:
        return "NOT A STRING!!"
    else:
        return string[::-1]

def reversed():
    i = input("Give a string: ")
    print(val_input(i))

if __name__ == '__main__':
    reversed()
