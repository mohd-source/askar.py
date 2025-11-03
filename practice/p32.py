# find key is present in dictionary or not
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}


find = "name"


if find in my_dict:
    
    print(f"'{find}' is present in the dictionary.")
else:
    print(f"'{find}' is not present in the dictionary.")