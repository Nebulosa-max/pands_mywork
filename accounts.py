# Ask user to enter a 10-digit account number
account_number = input("Please enter a 10 digit account number: ")

# Get the last 4 digits
last_four = account_number[-4:]

# Create the masked version
masked_account = "X" * 6 + last_four

# Display the result
print(masked_account)

