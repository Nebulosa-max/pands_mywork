# Q3: Queue with random numbers
# Author: Sophie

import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for _ in range(numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print(f"queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print(f"current Number is {currentNumber} and the queue is {queue}")

print("the queue is now empty")