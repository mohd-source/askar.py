import time
import matplotlib.pyplot as plt

def visualize(arr,idx1=None,idx2=None):
    plt.clf()
    colors = ['blue'] *len(arr)
    if idx1 is not None and idx2 is not None:
        colors[idx1] = 'red'
        colors[idx2] = 'orange'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.xticks(range(len(arr)))
    plt.title("Bubble Sort Visualization")
    plt.pause(0.2)  
    
plt.ion()



# def visualize(arr , idx1 = None , idx2 = None):
#     plt.clf()
#     colors = ['blue'] * len(arr)
#     if idx1 is not None:
#         colors[idx1] = 'green'
#     if idx2 is not None:
#         colors[idx2] = 'red'
#     if idx1 is None and idx2 is not None:
#         colors[idx1] = 'blue'
#         colors[idx1] = 'orange'
#     plt.bar(range(len(arr)), arr, color=colors)
#     plt.xticks(range(len(arr)), arr)
#     plt.title("Array Visualization")
#     plt.pause(0.2)
# time.sleep(1)
# plt.figure(figsize=(10,6))
# plt.ion()



arr = [72, 45, 60, 33, 18, 55, 27, 44]

print("Original Array:", arr)
print()

n = len(arr)
visualize(arr)
for step in range(n - 1):
    min_index = step
    
    for j in range(step + 1, n):
        visualize(arr, step , j)
        if arr[j] < arr[min_index]:
            min_index = j
    temp = arr[step]
    arr[step] = arr[min_index]
    arr[min_index] = temp
    visualize(arr, step , min_index)

 

print("Final Array:", arr)