data = ["Python\n", "Java\n", "C++\n"]

file = open("languages.txt", "w")
file.writelines(data)
file.close()

print("List written to file")
