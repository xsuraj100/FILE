n = int(input("Enter number of lines: "))
file = open("data.txt", "r")

lines = file.readlines()
for line in lines[-n:]:
    print(line, end="")

file.close()
