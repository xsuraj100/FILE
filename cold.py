try:
    file = open("unknown.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist")
