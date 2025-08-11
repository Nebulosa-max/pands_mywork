# bank.py
# This program adds two money amounts (in cent) and prints the result in euro format.

# Ask the user to input two amounts in cent
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))

# Add the amounts
total_cent = amount1 + amount2

# Convert to euro
euro = total_cent / 100

# Print the result with euro symbol (€) and two decimal places
print(f"The sum of these is €{euro:.2f}")