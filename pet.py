file = open("data.txt", "r")
text = file.read()

sentences = text.count('.') + text.count('!') + text.count('?')
print("Number of sentences:", sentences)

file.close()
