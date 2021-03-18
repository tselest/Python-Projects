# **Binary to Decimal and Back Converter** 
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def check(n):

    for i in str(n):
        if i not in "23456789":
            print("Given number is binary")
            y = int(str(n), 2)
            return f"Its decimal equivalent is {str(y)}"

        elif i not in "01":
            print("Given number is decimal")
            z = format(n, "b")
            return f"Its binary equivalent is {str(z)}"

def number():

    x = int(input("Enter binary/decimal number: "))
    print(check(x))

if __name__ == "__main__":
    number()
