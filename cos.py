file = open("students.txt", "a")

name = input("Enter name: ")
roll = input("Enter roll no: ")
marks = input("Enter marks: ")

file.write(name + "," + roll + "," + marks + "\n")
file.close()

print("Student data stored")
