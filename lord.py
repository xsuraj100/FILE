file = open("data.txt", "r")
words = file.read().lower().split()
file.close()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
