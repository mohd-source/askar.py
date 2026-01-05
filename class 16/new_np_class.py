
# import matplotlib
import numpy as np



array1 = np.array([[1,2,3,4],[5,6,7,8]])
array2 = np.array([[9,10,11,12],[13,14,15,16]])
np.save('file1.npy', array1)
load = np.load('file1.npy')
print(load)
print("\n--------------------------------------------------------------------------------------\n")

np.savez('file2.npy', array2)
load2 = np.load('/home/steampup-qbh/Desktop/AK--xi/askar/class 16/file2.npy.npz')
print(load2)





print("\n--------------------------------------------------------------------------------------\n")

# np.seterr(divide='raise')
result = (array1,array2)
print(result)
print("\n--------------------------------------------------------------------------------------\n")

cal = np.exp(1000)
print(cal)







