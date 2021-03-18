
#Calculate the monthly payment based on the formula
# M = P[r(1+r)^n/((1+r)^n)-1)] 
# M = the total monthly mortgage payment
# P = the principal loan amount
# r = your monthly interest rate
# n = number of payments over the loan’s lifetime.

#Declare and initialize the variables
monthlyPayment = 0.0
loanAmount = 0.0
interestRate = 0.0
numberOfPayments = 0.0
loanDurationInYears = 0.0

#Ask the user for the values needed to calculate the monthly payments
strLoanAmount = input("How much money will you borrow? ")
strInterestRate = input("What is the interest rate on the loan? ")
strLoanDurationInYears = input("How many years will it take you to pay off the loan? " )

#Convert the strings into floating numbers so we can use them in the formula
loanDurationInYears = float(strLoanDurationInYears)
loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)/100/12

#Since payments are once per month, number of payments is number of years for the loan * 12
numberOfPayments = float(loanDurationInYears)*12

monthlyPayment = loanAmount * (interestRate * (1 + interestRate) ** numberOfPayments) / ((1 + interestRate) ** numberOfPayments - 1)

#provide the result to the user
print(f"Your monthly payment will be ${monthlyPayment:.2f}")


