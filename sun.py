file = open("data.txt", "r")
words = file.read().lower().split()
count = 0

for word in words:
    if word[0] in "aeiou":
        count += 1

print("Words starting with vowel:", count)
file.close()
