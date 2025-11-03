dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'Name': 'Manni', 'Age': 8, 'Class': 'Second'}

# add both dictionaries into one dictionary
dict3 = {**dict1, **dict2}
print(dict3)