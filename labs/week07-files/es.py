import sys
import os

# Check if filename is provided
if len(sys.argv) < 2:
    print("Error: No filename provided.")
    print("Usage: python es.py filename.txt")
    sys.exit(1)

filename = sys.argv[1]

# Check if file exists
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

# Check if file is a .txt file
if not filename.lower().endswith('.txt'):
    print("Error: File must be a .txt file.")
    sys.exit(1)

# Open the file and count lowercase 'e' and uppercase 'E'
with open(filename, 'r') as f:
    text = f.read()
    count_e = text.lower().count('e')

# Print result in nice format
print(f"{filename} contains {count_e} e's")

