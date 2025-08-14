# Floors a number (rounds down towards negative infinity)
# Author: Andrew Beatty

import math

numberToFloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberToFloor)
print("{} floored is {}".format(numberToFloor, flooredNumber))