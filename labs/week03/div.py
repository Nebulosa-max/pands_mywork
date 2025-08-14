# Program that reads in two numbers and outputs the integer result and remainder

# Read two numbers from the user
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# Calculate integer division and remainder
answer = x // y       # integer division
remainder = x % y     # remainder

# Show the result
print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
