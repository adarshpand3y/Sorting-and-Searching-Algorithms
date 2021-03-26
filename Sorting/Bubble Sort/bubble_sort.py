length = int(input("Enter the length of the list: "))
arr = []

# Input
for i in range(length):
    arr.append(int(input("Enter a number: ")))

# Sorting
for i in range(length):
    for j in range(length-1-i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

#Display
print("The sorted list is:-")
print(arr)