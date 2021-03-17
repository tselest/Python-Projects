def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for c in range(a, b):
        for i in range(2, c):
            if c % i == 0:
                break
        else:
            return c
    return None

def main():
    n = int(input('Find the next prime number from: '))
    print('Next prime is ' + str(find_next_prime(n+1)))

if __name__ == '__main__':
    main()

