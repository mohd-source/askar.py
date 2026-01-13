arr = [72, 45, 60, 33, 18, 55, 27, 44]

print("orignal Array:", arr)
print()

n = len(arr)
for step in range (n - 1):
    for i in range(n-1 - step):
        if(arr[i]) > (arr[i + 1]):
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

print("Final Array:", arr)


