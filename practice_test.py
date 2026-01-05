n = int(input("enter a no: "))
# # Step 1: Build the initial tuple
# inventory = ()

# while len(inventory) < 5:
#     fruit = input("Enter a fruit to add to the inventory: ")
#     inventory += (fruit,)  # adding to a tuple
#     print("Current inventory:", inventory)

# # Step 2: Update the tuple
# fruit_to_remove = input("\nEnter the fruit you want to remove from the inventory: ")

# # Convert tuple to list for modification
# inventory_list = list(inventory)

# # Remove fruit if it exists
# if fruit_to_remove in inventory_list:
#     inventory_list.remove(fruit_to_remove)
#     print(f"{fruit_to_remove} removed.")
# else:
#     print(f"{fruit_to_remove} not found in inventory.")

# # Add a new fruit
# new_fruit = input("Enter the new fruit to add: ")
# inventory_list.append(new_fruit)

# # Convert back to tuple
# inventory = tuple(inventory_list)

# # Step 3: Final updated inventory
# print("\nFinal updated inventory:", inventory)






# # for i in range (1, n+1):
# #     for j in range (n, i - 1, -1):
# #         print(" ", end = "")
    
# #     for k in range (1, i + 1):
# #         print("*", end = "")
    
# #     for k in range (2, i + 1):
# #         print("*", end = "")
# #     print()

# for i in range (1, n+1):
#     for j in range (n, i -1, -1):
#         print(" ", end="")
#     print("*", end="")

#     for k in range (1, i+1):
#         print(" ", end="")

#     for l in range (2, i+1):
#         print(" ", end = "")
#     print("*" , end = "")
#     print()

# for i in range (2, n+1):
#     for j in range (1, i+1):
#         print(" ", end="")
#     print("*", end="")

#     for k in range (n, i -1, -1):
#         print(" ", end="")

#     for l in range (n-1, i-1,-1):
#         print(" ", end = "")
#     print("*" , end = "")
#     print()
















for i in range (1, n+1):
    for j in range (n, i - 1, - 1):
        print(" ", end = "")
    print("*", end="")

    for k in range (1, i):
        print(" ", end="")

    for l in range (2, i+1):
        print(" ", end = "")
    print("*", end = "")
    print()



for i in range(2, n+1):
    for j in range(1, i):
        print(" ", end = "")
    print("*", end = "")

    for j in range(n, i-1, -1):
        print(" ", end = "")

    for k in range(n-1, i-1, -1):
        print(" ", end = "")
    print("*", end = "")
    print()

















for i in range (1, n+1):
    for j in range (n, i-1 ,-1):
        
        print(" ", end="")



    for j in range (1, i+1):
        print("*", end="")


    for j in range (2, i+1):
        print("*", end="")
    
    print()



for i in range (2, n+1):
    for j in range (1, i+1):
        print(" ", end="")
    


    for j in range (n, i-1 ,-1):
        print("*", end="")
    

    for j in range (n - 1, i - 1, - 1):
        print("*", end="")
    print()