import numpy as np 

temp = np.array([28, 35, 42, 39, 45, 30])
idx = np.where(temp > 38)



print("Hight Temperature:", temp[idx])
print("Index of Hight Temperature:", idx[0])