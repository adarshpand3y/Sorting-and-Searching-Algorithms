length = int(input("Enter the length of the list: "))
arr = []
found = False

# Input
for i in range(length):
    arr.append(int(input("Enter a number: ")))

target = int(input("Enter number to search: "))

# Searching using linear search
for iteration, num in enumerate(arr):
    if num == target:
        found = True
        pos = iteration
        break

if found:
    print(f"Found at position {pos}")
else:
    print("Not found")