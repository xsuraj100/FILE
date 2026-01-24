file = open("data.txt", "r")
text = file.read()
file.close()

text = text.replace(" ", "-")

file = open("data.txt", "w")
file.write(text)
file.close()

print("Spaces replaced with hyphens")
