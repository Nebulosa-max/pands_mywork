
# quiz2.py

FILENAME = "Topic07-files/count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
    return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 3
print(f"This program has been run {num} times.")
writeNumber(num)
