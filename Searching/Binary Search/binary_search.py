length = int(input("Enter the length of the sorted list: "))
arr = []
found = False
left = 0
right = length-1
mid = 0

# Input
for i in range(length):
    arr.append(int(input("Enter a number: ")))

target = int(input("Enter number to search: "))

# Searching using binary search
while(left<=right):
    mid = int((left+right)/2)
    if arr[mid] == target:
        found = True
        pos = mid
        break
    elif target<arr[mid]:
        right = mid-1
    else:
        left = mid+1

# Display
if found:
    print(f"Found at position {pos}")
else:
    print("Not found")