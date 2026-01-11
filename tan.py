file = open("students.txt", "r")

for line in file:
    name, roll, marks = line.split(",")
    print("Name:", name, "Roll:", roll, "Marks:", marks)

file.close()
