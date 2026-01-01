file = open("data.txt", "r")
lines = file.readlines()
file.close()

for line in reversed(lines):
    print(line, end="")
