#  **Change Return Program** 
#  The user enters a cost and then the amount of money given. 
#  The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

coins=[]
coin = [50,25,10,5,1]
cost = float(input('Cost: '))
amount_given = float(input('Amount given: '))

change = (amount_given - cost)
change_ = change-int(change)
change_ = round(change_,2)*100

for c in coin:
    while change_>=c:
        coins.append(c)
        change_ -= c
    
half=coins.count(50)
qua = coins.count(25)
dime=coins.count(10)
ni=coins.count(5)
pen=coins.count(1)
dollars = int(change)

if half !=0 or qua != 0 or dime!=0 or ni!=0 or pen!=0:
    print (f'The change of {round(amount_given,2)} is: {change:.2f} \n-dollars: {dollars}, \n-halfs: {half} \n-quarters: {qua} \n-dime: {dime} \n-nickels: {ni} \n-pennies: {pen}')
else:
     print (f'The change from {round(amount_given,2)} is: {change}, and no coins')

