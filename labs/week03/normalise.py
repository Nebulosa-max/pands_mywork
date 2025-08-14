# Program reads in a string, strips spaces, converts to lowercase, and shows length changes
# Author: Your Name

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That string normalised is: {normalisedString}")
print(f"We reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters")