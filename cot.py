f1 = open("data.txt", "r")
f2 = open("even_lines.txt", "w")

for i, line in enumerate(f1, start=1):
    if i % 2 == 0:
        f2.write(line)

f1.close()
f2.close()
print("Even lines copied")
