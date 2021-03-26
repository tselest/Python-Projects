# Credit Card Validator 
# Takes in a credit card number from a common credit card vendor 
# (Visa, MasterCard, American Express, Discoverer) and validates it 
# to make sure that it is a valid number (look into how credit cards use a checksum).

# look for luhn algorithm to understand how credit cards validator use the checksum to see if a card is valid

def credit_card_validator(credit_card):
    card_list = [int(x) for x in credit_card]                            
    # turn the credit card number in a list of integers
    card_list.reverse()                                                  
    # reverse it to make the necessary calculation

    final_list = []                                                      
    # declare an empty list where we will append the modified digits

    for i in range(0, len(card_list)):                                   
        # for every number in the list
        if i % 2:                                                           
            # if the number is in an odd position
            doubled_num = card_list[i] * 2                                      
            # multiply the number by 2
            if doubled_num > 9:                                                 
                # if the doubled number is a two digit number (i.e. every number greater than 9)
                split_num = map(int, str(doubled_num))                              
                # split the two digits in two different integers (we use a list to do that)
                sum = 0
                for num in split_num:                                               
                    # then sum the two integers
                    sum += num
                final_list.append(sum)                                              
                # finally append the sum of the two integers in our empty list
            elif doubled_num <= 9:                                              
                # else if the doubled number is a one digit number (i.e. every number lower than, or equal to, 9)
                final_list.append(doubled_num)                                      
                # just append it to the list
        else:                                                               
            # else if the number is in an even position
            final_list.append(card_list[i])                                     
            # just append the number

    final_sum = 0
    for every_num in final_list:                                          
        # now sum every number of the list
        final_sum += every_num

    if not final_sum % 10:                                                
        # if the sum is divisable for 10 then the card is valid
        return True
    else:                                                                 
        # else the card is not valid
        return False


client_card = input('Please enter your credit card number:  ')


is_valid = credit_card_validator(client_card)

if is_valid:
    print('Your credit card number is valid')
else:
    print('Your credit card number is not valid')
