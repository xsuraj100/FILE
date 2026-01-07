file = open("data.txt", "r")
text = file.read()
file.close()

file = open("data.txt", "w")
file.write(text.upper())
file.close()

print("File content converted to uppercase")
