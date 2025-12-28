file = open("data.txt", "r")
text = file.read()

count = 0
for ch in text:
    if ch != " ":
        count += 1

print("Characters (excluding spaces):", count)
file.close()
