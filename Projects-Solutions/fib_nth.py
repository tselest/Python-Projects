# Fibonacci series will start at 0 and travel up to below number

n = int(input("Starting from 0, how many Fibonaccis to generate? : "))

# Initializing First and Second Values
a = 0
b = 1
sum = 0
count = 1

# Find & Displaying Fibonacci series
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b



