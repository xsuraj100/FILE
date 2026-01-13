file = open("data.txt", "r")
text = file.read()
count = 0

for ch in text:
    if not ch.isalnum() and not ch.isspace():
        count += 1

print("Special characters:", count)
file.close()
