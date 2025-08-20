# quiz.py
# Read the contents of a file line by line

filename = "Topic07-files/sample.txt"

with open(filename, "r") as f:
    for line in f:
        print(line.strip())
        
       # quiz.py
# Answer to Quiz Question 1a
filename = "Topic07-files/sample.txt"

with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# -------- Question 1b and 1c --------
# This code writes to the same file twice using "w" mode, which overwrites the content each time.

with open("Topic07-files/test-b.txt", "w") as f:
    data = f.write("test b\n")  # This writes 7 characters
    print("First write returns:", data)

with open("Topic07-files/test-b.txt", "w") as f2:
    data = f2.write("another line\n")  # This overwrites previous content with 13 characters
    print("Second write returns:", data)
    
    