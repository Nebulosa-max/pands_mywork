def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError("number must be > 0")

    a, b = 0, 1
    fib_sequence = [0]

    for i in range(1, number):
        fib_sequence.append(b)
        a, b = b, a + b

    return fib_sequence