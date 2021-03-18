# **Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. 
# Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

import math

def replay():
    
    return input('Check again? Enter Yes or No: ').lower().startswith('y')

while True:

    try:

        n = int(input("# Digits (1-15): "))

        if n<=15:
            e = lambda n: (int((math.e*math.pow(10,n))))/math.pow(10,n)
            print(e(n))
        else:
            print("Integer not in range!")

    except ValueError:
        print("Please enter an integer (1-15)! ")


    if not replay():
        break
