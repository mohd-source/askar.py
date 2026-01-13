import numpy as np

# transaction = np.array([100, 200, 300])

# transaction = transaction.astype(float)

# print(transaction)

# print("item size =", transaction.itemsize)
# print()



# transaction = np.array ([100, 200, 300]) 
# transactions = transaction.astype(str)
# print(transactions)
# print("item size =", transactions.itemsize)




transaction = np.array([100, 200, 300])
transaction = transaction.astype(float)
print("Transaction ", transaction.dtype)
# convert araay to string
transaction_str = transaction.astype(str)
print("Transaction ", transaction_str.dtype)
print("item size of float : ", transaction.itemsize)
print("item size of string : ", transaction_str.itemsize)