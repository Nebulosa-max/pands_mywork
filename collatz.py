number = int(input("Please enter a positive integer: "))

while number != 1:
    print(number, end=' ')
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

print(1)  # Final number in the sequence
