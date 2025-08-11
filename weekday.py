# weekday.py

import datetime

# Get current day of the week (0 = Monday, 6 = Sunday)
today = datetime.datetime.today().weekday()

# Check if it's weekend (Saturday=5 or Sunday=6)
if today >= 5:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
    