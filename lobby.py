import os

filename = "data.txt"

if os.path.getsize(filename) == 0:
    print("File is empty")
else:
    print("File is not empty")
