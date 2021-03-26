# Unit Converter (temp, currency, volume, mass and more)
# Converts various units between one another. 
# The user enters the type of unit being entered, the type of unit they want to convert 
# to and then the value. The program will then make the conversion.

# Define the function
def unit_converter():
    # Ask the general type you want to convert into
    print('Here are the type of units you can convert:')
    print('\t1. TIME')
    print('\t2. CURRENCY')
    print('\t3. VOLUME')
    print('\t4. MASS')
    print('\t5. TEMPERATURE\n')

    # Use a try/except loop to get the right input
    while True:
        try:
            type = int(input('Which type of unit do you want to convert (choose a number):  '))
        except:
            print('Invalid input')
            continue
        else:
            break

    # Time type
    if type == 1:
        print('\nHere are the types you can convert:')
        print('\t1. HOURS')
        print('\t2. MINUTES')
        print('\t3. SECONDS')

        # Ask the user for the type of unit they want to convert
        # Use a try/except loop to get the right input
        while True:
            try:
                sub_type_one = int(input('\nWhat type of unit do you want to convert from? (Choose a number)\n'))
                sub_type_two = int(input('\nWhat type of unit do you want to convert to? (Choose a number)\n'))
            except:
                print('Invalid input')
                continue
            else:
                if sub_type_one not in range(1,4) or sub_type_two not in range(1,4):
                    print('We can\'t do such operation, please try again')
                    continue
                else:
                    break

        # Ask the user the number he want to convert
        while True:
            try:
                unit = int(input('\nWhat is the unit you want to convert?\n'))
            except:
                print('Invalid input')
                continue
            else:
                break

        if sub_type_one == 1 and sub_type_two == 2:
            result = unit * 60
            print(f'\n{unit} hours is equal to {result} minutes\n')
        elif sub_type_one == 2 and sub_type_two == 1:
            result = unit / 60
            print(f'\n{unit} minutes is equal to {result} hours\n')
        elif sub_type_one == 1 and sub_type_two == 3:
            result = (unit * 60) * 60
            print(f'\n{unit} hours is equal to {result} seconds\n')
        elif sub_type_one == 3 and sub_type_two == 1:
            result = (unit / 60) / 60
            print(f'\n{unit} seconds is equal to {result} hours\n')
        elif sub_type_one == 2 and sub_type_two == 3:
            result = unit * 60
            print(f'\n{unit} minutes is equal to {result} seconds\n')
        elif sub_type_one == 3 and sub_type_two == 2:
            result = unit / 60
            print(f'\n{unit} seconds is equal to {result} minutes\n')
        else:
            print('We can\'t do this operation')

    # Currency type
    elif type == 2:
        print('\nHere are the types you can convert:')
        print('\t1. EUR')
        print('\t2. USD')
        print('\t3. GBP')

        # Ask the user for the type of unit they want to convert
        # Use a try/except loop to get the right input
        while True:
            try:
                sub_type_one = int(input('\nWhat type of unit do you want to convert from? (Choose a number)\n'))
                sub_type_two = int(input('\nWhat type of unit do you want to convert to? (Choose a number)\n'))
            except:
                print('Invalid input')
                continue
            else:
                if sub_type_one not in range(1,4) or sub_type_two not in range(1,4):
                    print('We can\'t do such operation, please try again')
                    continue
                else:
                    break

        # Ask the user the number he want to convert
        while True:
            try:
                unit = int(input('\nWhat is the unit you want to convert?\n'))
            except:
                print('Invalid input')
                continue
            else:
                break

        if sub_type_one == 1 and sub_type_two == 2:
            result = unit * 1.14
            print(f'\n{unit} EUR is equal to {round(result,2)} USD\n')
        elif sub_type_one == 2 and sub_type_two == 1:
            result = unit / 1.14
            print(f'\n{unit} USD is equal to {round(result,2)} EUR\n')
        elif sub_type_one == 1 and sub_type_two == 3:
            result = unit / 1.15
            print(f'\n{unit} EUR is equal to {round(result,2)} GBP\n')
        elif sub_type_one == 3 and sub_type_two == 1:
            result = unit * 1.15
            print(f'\n{unit} GBP is equal to {round(result,2)} EUR\n')
        elif sub_type_one == 2 and sub_type_two == 3:
            result = unit / 1.31
            print(f'\n{unit} USD is equal to {round(result,2)} GBP\n')
        elif sub_type_one == 3 and sub_type_two == 2:
            result = unit * 1.31
            print(f'\n{unit} GBP is equal to {round(result,2)} USD\n')
        else:
            print('We can\'t do this operation')


    # Volume type
    elif type == 3:
        print('\nHere are the types you can convert:')
        print('\t1. Liter')
        print('\t2. Milliliter')
        print('\t3. Imperial Gallon')

        # Ask the user for the type of unit they want to convert
        # Use a try/except loop to get the right input
        while True:
            try:
                sub_type_one = int(input('\nWhat type of unit do you want to convert from? (Choose a number)\n'))
                sub_type_two = int(input('\nWhat type of unit do you want to convert to? (Choose a number)\n'))
            except:
                print('Invalid input')
                continue
            else:
                if sub_type_one not in range(1,4) or sub_type_two not in range(1,4):
                    print('We can\'t do such operation, please try again')
                    continue
                else:
                    break

        # Ask the user the number he want to convert
        while True:
            try:
                unit = int(input('\nWhat is the unit you want to convert?\n'))
            except:
                print('Invalid input')
                continue
            else:
                break

        if sub_type_one == 1 and sub_type_two == 2:
            result = unit * 1000
            print(f'\n{unit} L is equal to {round(result,2)} ml\n')
        elif sub_type_one == 2 and sub_type_two == 1:
            result = unit / 1000
            print(f'\n{unit} ml is equal to {round(result,2)} L\n')
        elif sub_type_one == 1 and sub_type_two == 3:
            result = unit / 4.55
            print(f'\n{unit} L is equal to {round(result,2)} Imp gal\n')
        elif sub_type_one == 3 and sub_type_two == 1:
            result = unit * 4.55
            print(f'\n{unit} Imp gal is equal to {round(result,2)} L\n')
        elif sub_type_one == 2 and sub_type_two == 3:
            result = unit * 4546.09
            print(f'\n{unit} ml is equal to {round(result,2)} Imp gal\n')
        elif sub_type_one == 3 and sub_type_two == 2:
            result = unit / 4546.09
            print(f'\n{unit} Imp gal is equal to {round(result,5)} ml\n')
        else:
            print('We can\'t do this operation')


    # Mass type
    elif type == 4:
        print('\nHere are the types you can convert:')
        print('\t1. Kilograms')
        print('\t2. Pound')
        print('\t3. Ounce')

        # Ask the user for the type of unit they want to convert
        # Use a try/except loop to get the right input
        while True:
            try:
                sub_type_one = int(input('\nWhat type of unit do you want to convert from? (Choose a number)\n'))
                sub_type_two = int(input('\nWhat type of unit do you want to convert to? (Choose a number)\n'))
            except:
                print('Invalid input')
                continue
            else:
                if sub_type_one not in range(1,4) or sub_type_two not in range(1,4):
                    print('We can\'t do such operation, please try again')
                    continue
                else:
                    break

        # Ask the user the number he want to convert
        while True:
            try:
                unit = int(input('\nWhat is the unit you want to convert?\n'))
            except:
                print('Invalid input')
                continue
            else:
                break

        if sub_type_one == 1 and sub_type_two == 2:
            result = unit * 2.205
            print(f'\n{unit} kgs is equal to {round(result,2)} lbs\n')
        elif sub_type_one == 2 and sub_type_two == 1:
            result = unit / 2.205
            print(f'\n{unit} lbs is equal to {round(result,2)} kgs\n')
        elif sub_type_one == 1 and sub_type_two == 3:
            result = unit * 35.27
            print(f'\n{unit} kgs is equal to {round(result,2)} oz\n')
        elif sub_type_one == 3 and sub_type_two == 1:
            result = unit / 35.27
            print(f'\n{unit} oz is equal to {round(result,2)} kgs\n')
        elif sub_type_one == 2 and sub_type_two == 3:
            result = unit * 16
            print(f'\n{unit} lbs is equal to {round(result,2)} oz\n')
        elif sub_type_one == 3 and sub_type_two == 2:
            result = unit / 16
            print(f'\n{unit} oz is equal to {round(result,5)} lbs\n')
        else:
            print('We can\'t do this operation')

    # Temperature Type
    elif type == 5:
        print('Here are the type you can convert:')
        print('1. Celsius')
        print('2. Fahrenheit')
        print('3. Kelvin')

        while True:
            try:
                sub_type_one = int(input('\nWhat type of unit do you want to convert from? (Choose a number)\n'))
                sub_type_two = int(input('\nWhat type of unit do you want to convert to? (Choose a number)\n'))
            except:
                print('Invalid input')
                continue
            else:
                if sub_type_one not in range(1,4) or sub_type_two not in range(1,4):
                    print('We can\'t do such operation, please try again')
                    continue
                else:
                    break

        # Ask the user the number he want to convert
        while True:
            try:
                unit = int(input('\nWhat is the unit you want to convert?\n'))
            except:
                print('Invalid input')
                continue
            else:
                break

        if sub_type_one == 1 and sub_type_two == 2:
            result = (unit * (9/5)) + 32
            print(f'{unit}° C is equal to {result}° F')
        elif sub_type_one == 2 and sub_type_two == 1:
            result = (unit - 32) * (5/9)
            print(f'{unit}° F is equal to {round(result,2)}° C')
        elif sub_type_one == 1 and sub_type_two == 3:
            result = unit + 273.15
            print(f'{unit}°C is equal to {result} K')
        elif sub_type_one == 3 and sub_type_two == 1:
            result = unit - 273.15
            print(f'{unit} K is equal to {round(result,2)}°C')
        elif sub_type_one == 2 and sub_type_two == 3:
            result = (unit - 32) * (5/9) + 273.15
            print(f'{unit}°F is equal to {round(result,2)} K')
        elif sub_type_one == 3 and sub_type_two == 2:
            result = (unit - 273.15) * (9/5) + 32
            print(f'{unit} K is equal to {round(result,2)}°F')
        else:
            print('We can\'t do this operation')
    else:
        print('We do not do such operation!!!')

        
# Call the function
unit_converter()
