file = open("data.txt", "r")
text = file.read()
file.close()

old = input("Enter word to replace: ")
new = input("Enter new word: ")

text = text.replace(old, new)

file = open("data.txt", "w")
file.write(text)
file.close()

print("Word replaced successfully!")
