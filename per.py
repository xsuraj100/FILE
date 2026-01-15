file = open("data.txt", "r")

for i, line in enumerate(file, start=1):
    print(i, ":", line, end="")

file.close()
