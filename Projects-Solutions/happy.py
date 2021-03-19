# SPLIT NUMBER INTO DIGITS

def get_digits(number):
	digits = []
	while number:
		digits.append(number % 10)
		number //= 10
	digits.reverse()
	return digits

# ENTER A NUMBER - CHECK IF HAPPY/SAD

def happy():
    number = int(input("Enter a number: "))
    seen = []

    while True:
        digits = get_digits(number)
        squared = sum(list(map(lambda x:x**2, digits)))
        if squared == 1:
            return "Given number is happy :)"
        elif squared in seen:
            return "Given number is saaad :("
        else:
            number = squared
            seen.append(number)

if __name__=="__main__":
    print(happy())
