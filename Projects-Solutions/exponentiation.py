# **Fast Exponentiation** - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.


while True:
    try:
        base = int(input("Enter a positive integer: "))
        exponent = int(input("Enter the exponent: "))
        power = 1
        count = 0

        while count < exponent:
            power *= base
            count += 1
        print(f"The given number {base} powered by {exponent} gives {power}")
        break

    except ValueError:
        print("Not an integer number")
        break





