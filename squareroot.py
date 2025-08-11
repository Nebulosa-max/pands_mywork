# Approximate square root using Newton's method

def sqrt(x):
    guess = x / 2
    for i in range(10):
        guess = (guess + x / guess) / 2
    return guess

# Ask user for input
number = float(input("Please enter a positive number: "))
result = sqrt(number)
print(f"The square root of {number} is approx. {result:.1f}")
