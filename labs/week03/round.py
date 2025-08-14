# rounds a number
# Be careful: round() rounds to the nearest even number for .5 values
# Example: 4.5 → 4, 5.5 → 6
# Author: Andrew Beatty

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print("{} rounded is {}".format(numberToRound, roundedNumber))