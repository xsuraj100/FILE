letter = input("Enter starting letter: ").lower()
file = open("data.txt", "r")

words = file.read().lower().split()

for word in words:
    if word.startswith(letter):
        print(word)

file.close()
