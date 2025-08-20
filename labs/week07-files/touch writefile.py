# Write some text to a file

filename = "Topic07-files/output.txt"

with open(filename, "w") as f:
    f.write("This file was written using Python.\n")
    f.write("You’ll get there!\n")
    f.write("Keep going, one step at a time\n")
    