length = int(input("Enter the length of the list: "))
arr = []

# Input
for i in range(length):
    arr.append(int(input("Enter a number: ")))

# Sorting using selection sort
for i in range(length-1):
    min_index = i
    for j in range(i+1, length):
        if arr[j]<arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

#Display
print("The sorted list is:-")
print(arr)