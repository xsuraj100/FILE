file = open("numbers.txt", "w")
nums = input("Enter numbers separated by space: ")
file.write(nums)
file.close()

file = open("numbers.txt", "r")
numbers = map(int, file.read().split())
print("Sum =", sum(numbers))
file.close()
