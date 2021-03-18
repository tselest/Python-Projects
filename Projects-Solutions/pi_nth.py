#**Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places.

import math

def replay():
    
    return input('Check again? Enter Yes or No: ').lower().startswith('y')

def num_digits(x):

    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1

while True:      

    try:
        DIGITS = int(input("# Digits: ")) 
        digits = [str(n) for n in list(num_digits(DIGITS))]
        print(f'{digits.pop(0)}.{"".join(digits)}')
    except ValueError:
        print("Please enter an integer!")

    if not replay():
        break






