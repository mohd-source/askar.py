Inventory = {}

while True:
    print("\n---------------------- Inventory Management System ----------------------")
    print("1. Add The Items")
    print("2. View The Items")
    print("3. Search The Item")
    print("4. Update The Item")
    print("5. Remove The Item")
    print("6. Exit")

    choice = input("\tSelect The Option (1-6): ")
    print()

    if choice == "1":
        name = input("Add The Item: ")
        quantity = input("Quantity: ")
        if quantity.isdigit():
            Inventory[name] = int(quantity)
            print(f"\n{len(Inventory)} Item Added Successfully")
        else:
            print("Invalid quantity! Please enter a number.")

    elif choice == "2":
        if not Inventory:
            print("Inventory Is Empty")
        else:
            print("Current Inventory:")
            for key, value in Inventory.items():
                print(f"{key} : {value}")

    elif choice == "3":
        name = input("Enter The Item To Search: ")
        if name in Inventory:
            print(f"{name} - Quantity: {Inventory[name]}")
        else:
            print("Product Not Found")

    elif choice == "4":
        name = input("Enter The Item To Update: ")
        if name in Inventory:
            qty = input("Add New Quantity: ")
            if qty.isdigit():
                Inventory[name] = int(qty)  # update quantity
                print("The Quantity Of The Item Is Updated")
            else:
                print("Invalid quantity! Please enter a number.")
        else:
            print("Product Not Found")

    elif choice == "5":
        name = input("Enter The Item To Remove: ")
        if name in Inventory:
            del Inventory[name]
            print("The Item Is Deleted Successfully")
        else:
            print("Product Not Found")

    elif choice == "6":
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid Option. Please select 1-6.")
print("Thank You For Using Inventory Management System")