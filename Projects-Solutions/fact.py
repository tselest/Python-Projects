# **Factorial Finder** 
# - The factorial of a positive integer *n* is defined 
# as the product of the sequence , n-1, n-2, ...1 and the factorial of 0 is defined as being 1. 
# Solve this using both loops and recursion.

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(x))

while True:
    try:
        x = int(input("Enter an integer number: "))
        print(f"The factorial of  {x} is {factorial(x)}")
        r = input("Check again? Y/N: ").lower()
        if r.startswith("y") == True:
            continue
        elif r.startswith("n") == True:
            break
        else:
            print("Not a valid option.")
            break
    except ValueError:
        print("Given value not an integer! Please enter a non-negative integer.")
    except RecursionError:
        print("Negative given number! Please enter a non-negative integer.")
