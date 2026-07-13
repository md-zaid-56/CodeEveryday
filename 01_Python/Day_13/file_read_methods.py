with open("logs.txt", "w") as f:
    f.write("Server Started \n")

with open("logs.txt", "a") as f:
    f.write("User Login \n")

with open("logs.txt", "a") as f:
    f.write("Database Connected \n")

with open("logs.txt", "a") as f:
    f.write("Server Stopped")

print("readline() output","-" * 12) #This read only ONE line
with open("logs.txt", "r") as f:
    print(f.readline())

print("\nreadlines() output","-" * 12) #This read All the lines and store them into list
with open("logs.txt", "r") as f:
    output = f.readlines()
print(output)

print("\nfor loop output","-" * 12) #This is used Only to print whole file line by line
with open("logs.txt", "r") as f:
    for line in f:
        print(line)
