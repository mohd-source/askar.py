arr = [72, 45, 60, 33, 18, 55, 27, 44]

print("Original Array:", arr)
print()

n = len(arr)

for step in range(n - 1):
    min_index = step
    
    for j in range(step + 1, n):
        
        if arr[j] < arr[min_index]:
            min_index = j


 
    arr[step], arr[min_index] = arr[min_index], arr[step]

print("Final Array:", arr)
                



arr = [72, 45, 60, 33, 18, 55, 27, 44]

print("Original Array:", arr)
print()

n = len(arr)

for step in range(n - 1):
    min_index = step
    
    for j in range(step + 1, n):
        
        if arr[j] < arr[min_index]:
            min_index = j
    temp = arr[step]
    arr[step] = arr[min_index]
    arr[min_index] = temp


 

print("Final Array:", arr)
                