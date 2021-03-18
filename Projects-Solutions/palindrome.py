# Check if Palindrome - Checks if the string entered by the user is a palindrome. 

def palindrome():
    i = input("Give an input: ")
    
    if i.isdigit():
        print("NOT A STRING")
    else:
        print(check(i))


def check(string):
    if string==string[::-1]:
        return "input is a palindrome"
    else:
        return "not a palindrome"

if __name__=="__main__":
    palindrome()
