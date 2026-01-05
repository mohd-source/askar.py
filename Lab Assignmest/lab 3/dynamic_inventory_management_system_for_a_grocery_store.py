
fruits_list = []

while len(fruits_list) < 5:
    fruit = input("Enter a fruit name: ")
    fruits_list.append(fruit)


fruits_tuple = tuple(fruits_list)
print("\nInitial inventory:", fruits_tuple)


fruit_remove = input("\nEnter the fruit to remove: ")
new_fruit = input("Enter the new fruit to add: ")

# Convert tuple back to list for updating
updated_list = list(fruits_tuple)

if fruit_remove in updated_list:
    updated_list.remove(fruit_remove)
else:
    print(f"{fruit_remove} not found in inventory.")

updated_list.append(new_fruit)


updated_fruits_tuple = tuple(updated_list)


print("\nUpdated inventory:", updated_fruits_tuple)
