
#**Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.

def factors(n):
    i = 2
    factors = []
    while i <= n:
        if (n % i) == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

number = int(input("Number: ")) 
print(factors(number))
