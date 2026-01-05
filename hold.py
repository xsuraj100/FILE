file = open("data.txt", "r")
words = file.read().split()

longest = max(words, key=len)
print("Longest word:", longest)

file.close()
