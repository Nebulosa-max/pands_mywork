# gradeExtra.py
# This program reads in a student's percentage
# Rounds it to the nearest whole number
# Uses a while loop to keep asking until user enters -1

while True:
    user_input = input("Enter the percentage (-1 to quit): ")

    # Check for quit condition
    if user_input == "-1":
        print("Goodbye!")
        break

    # Try to convert to float
    try:
        percentage = float(user_input)
    except ValueError:
        print("Please enter a valid number (or -1 to quit).")
        continue

    # Check if within range
    if percentage < 0 or percentage > 100:
        print("Please enter a number between 0 and 100 (or -1 to quit).")
        continue

    # Round to nearest whole number
    percentage = round(percentage)

    # Determine grade
    if percentage < 40:
        print("Fail")
    elif percentage < 50:
        print("Pass")
    elif percentage < 60:
        print("Merit2")
    elif percentage < 70:
        print("Merit1")
    else:
        print("Distinction")