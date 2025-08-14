# This program prints out a random fruit using a tuple

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')   # tuple = round brackets

index = random.randint(0, len(fruits) - 1)       # 0 .. last index
fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))