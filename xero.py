file = open("data.txt", "r")
text = file.read()

paragraphs = text.split("\n\n")
print("Paragraphs:", len(paragraphs))

file.close()
