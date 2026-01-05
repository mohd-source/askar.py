import numpy as np
a = []
print("Enter 10 numbers:")


for i in range(10):
    num = int(input(f"Number {i+1}: "))
    a.append()


length = len(a)
print("list:", a)
print("list's Length:", length)


sum = np.sum(a)
avg = sum / length
print("Average:", avg)



print("Highest index:", a1.argmax())
print("Lowest index:", np.argmin(a))
