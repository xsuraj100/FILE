file = open("data.txt", "r")
count = 0

for line in file:
    count += 1

print("Total lines:", count)
file.close()
