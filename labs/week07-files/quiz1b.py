with open("test-d.txt", "w") as f:
    data = f.write("test d\n")
    print("First write returns:", data)

with open("test-d.txt", "a") as f2:
    data = f2.write("another line\n")
    print("Second write returns:", data)