import numpy as np
# # rank 1 array

# array = np.array([1,2,3])
# print(array)
# print("------------------------------------------------------------------------------")
# # rank 2 array

# arrray = np.array([[1,2,3],[2,3,4]])
# print(arrray)

# print("------------------------------------------------------------------------------")

# # Initail Array
# arr = np.array([
#     [2,5,6,7],
#     [-4,6,7,-8],
#     [5,6,8,9],
#     [4,8,5,3]])
# print("Initial Array")
# print(arr)

# print("------------------------------------------------------------------------------")


# # Printing a range of Array
# # With the use of slicing method

# sliced_arr = arr[:2, ::2]
# print("Array with first 2 rows and"
#       " alternate columns (o and 2 ):\n",sliced_arr)

# print("------------------------------------------------------------------------------")

# # Printing elements at
# # Specific Indices
# index_arr = arr[[1,1,0,3],
#                 [3,2,1,0]]
# print("\n Elements at indices (1,3),"
#     "(1,2),(0,1),(3,0):\n",index_arr)

# print("------------------------------------------------------------------------------")

# a = np.array([1,2,3,4])
# b = np.array([2,3,4,5])

# print(a)
# print(b)
# print(a+b)
# print(a+1)

# print("------------------------------------------------------------------------------")

# arrr = np.zeros(4)
# print(arrr)

# print("------------------------------------------------------------------------------")

# arra = np.ones(2)
# print(arra)

# print("------------------------------------------------------------------------------")

# lis = np.random.rand(5)
# print(lis)

# print("------------------------------------------------------------------------------")

# array1 = np.array([1,2,3,4.5],dtype='int32')

# print(array1 , array1.dtype)

# print("\n\t------------------------------------------------------------------------------\n")

# arr1 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
# trans_arr = arr1.T
# sqrt = np.sqrt(arr1)
# print(trans_arr)
# print(sqrt)


# print("------------------------------------------------------------------------\n")

# import numpy as np

# # 10 rows, 7 columns, random temperatures between 25 and 50
# temperature_random = 25 + (50 - 25) * np.random.randint(size=(10, 7))

# print("Random Temperature Array (10x7):")
# print(temperature_random)

# # Average temperature
# avg_temp = np.mean(temperature_random)
# print("\nAverage Temperature:", avg_temp)

# for i , avg in enumerate(avg_temp):
#     print(f"city{i} : {avg}")


array4 = np.array([[1,2,3,4],[5,6,7,8]])
np.save('array_file.npy', array4)