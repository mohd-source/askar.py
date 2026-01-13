import time
import matplotlib.pyplot as plt

arr = [72 , 45 , 60 , 30 , 18 , 55 , 27]

def visualize(arr , idx1 = None , idx2 = None):
    plt.clf()
    colors = ['blue'] * len(arr)
    if idx1 is not None:
        colors[idx1] = 'red'
    if idx2 is not None:
        colors[idx2] = 'green'
    if idx1 is None and idx2 is not None:
        colors[idx1] = 'blue'
        colors[idx1] = 'orange'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.xticks(range(len(arr)), arr)
    plt.title("Array Visualization")
    plt.pause(0.1)
plt.figure(figsize=(10,6))
plt.ion()


visualize(arr)
n = len(arr)
for step in range(n - 1):
    for i in range(n-1 - step):
        visualize(arr, i, i + 1)
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
           
plt.ioff()
plt.show()
time.sleep(5)