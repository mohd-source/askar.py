from numpy import sort


cart = []
while True:
    print("\n1. Add Item\n2. Remove Item\n3. View Card\n4. Exit ") 
    choice = input("Choice the Option: ")

    if choice == '1':
        item = input("Enter item to add: \n")
        cart.append(item)




    elif choice == '2':
        item = input("Enter item to remove: \n")
        
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found\n")




    elif choice == '3':
        print (f"your cart contain: \n")
        m = sorted(cart, key=str.lower)
        print(m)




    elif choice == '4':
        break




    else:
        print("Invalid Choice!\n")






m = sorted(cart, key=str.lower)
print(f"Your Crat List is: \n{m}")




total_item_cart = len(cart)
print("\n\t", total_item_cart)


count = {}
for item in cart:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
























































# import tkinter as tk
# from tkinter import messagebox

# cart = []

# # --- functions ---

# def add_item():
#     item = entry.get().strip()
#     if item:
#         cart.append(item)
#         entry.delete(0, tk.END)
#         update_cart_display()
#     else:
#         messagebox.showwarning("Warning", "Please enter an item.")

# def remove_item():
#     item = entry.get().strip()
#     if item in cart:
#         cart.remove(item)
#         entry.delete(0, tk.END)
#         update_cart_display()
#     else:
#         messagebox.showerror("Error", "Item not found in cart.")

# def update_cart_display():
#     listbox.delete(0, tk.END)
#     for item in sorted(cart, key=str.lower):
#         listbox.insert(tk.END, item)

# def exit_app():
#     total = len(cart)
#     messagebox.showinfo("Cart Summary",
#                         f"Final items:\n{sorted(cart, key=str.lower)}\n\nTotal items: {total}")
#     root.destroy()

# # --- GUI setup ---

# root = tk.Tk()
# root.title("Shopping Cart")
# root.geometry("350x400")

# title = tk.Label(root, text="Shopping Cart GUI", font=("Arial", 16))
# title.pack(pady=10)

# entry = tk.Entry(root, font=("Arial", 14))
# entry.pack(pady=10)

# btn_add = tk.Button(root, text="Add Item", width=15, command=add_item)
# btn_add.pack(pady=5)

# btn_remove = tk.Button(root, text="Remove Item", width=15, command=remove_item)
# btn_remove.pack(pady=5)

# btn_exit = tk.Button(root, text="Exit", width=15, command=exit_app)
# btn_exit.pack(pady=5)

# listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
# listbox.pack(pady=10)

# root.mainloop()










# import tkinter as tk
# from tkinter import ttk, messagebox

# class ShoppingCartGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Advanced Shopping Cart")
#         self.root.geometry("650x450")
#         self.root.resizable(False, False)

#         self.cart = []  # Each item = {"name": "", "qty": int}

#         self.create_widgets()

#     # -----------------------------
#     # UI Layout
#     # -----------------------------
#     def create_widgets(self):
#         title = tk.Label(self.root, text="🛒 Advanced Shopping Cart",
#                          font=("Arial", 20, "bold"))
#         title.pack(pady=10)

#         form_frame = tk.Frame(self.root)
#         form_frame.pack(pady=10)

#         # Item name
#         tk.Label(form_frame, text="Item Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
#         self.item_entry = tk.Entry(form_frame, width=25, font=("Arial", 12))
#         self.item_entry.grid(row=0, column=1, padx=5)

#         # Quantity
#         tk.Label(form_frame, text="Quantity:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
#         self.qty_entry = tk.Entry(form_frame, width=10, font=("Arial", 12))
#         self.qty_entry.grid(row=0, column=3, padx=5)

#         # Add to cart button
#         self.add_button = tk.Button(form_frame, text="Add to Cart", font=("Arial", 12), command=self.add_to_cart)
#         self.add_button.grid(row=0, column=4, padx=5)

#         # Cart display
#         self.cart_tree = ttk.Treeview(self.root, columns=("Item", "Quantity"), show="headings")
#         self.cart_tree.heading("Item", text="Item")
#         self.cart_tree.heading("Quantity", text="Quantity")
#         self.cart_tree.pack(pady=10)

#         # Checkout button
#         self.checkout_button = tk.Button(self.root, text="Checkout", font=("Arial", 12), command=self.checkout)
#         self.checkout_button.pack(pady=10)

#     # -----------------------------
#     # Button Commands
#     # -----------------------------
#     def add_to_cart(self):
#         item_name = self.item_entry.get().strip()
#         try:
#             item_qty = int(self.qty_entry.get().strip())
#         except ValueError:
#             messagebox.showerror("Invalid Input", "Please enter a valid quantity.")
#             return

#         if item_name and item_qty > 0:
#             self.cart.append({"name": item_name, "qty": item_qty})
#             self.item_entry.delete(0, tk.END)
#             self.qty_entry.delete(0, tk.END)
#             self.update_cart_display()
#         else:
#             messagebox.showwarning("Warning", "Please enter valid item details.")

#     def update_cart_display(self):
#         for i in self.cart_tree.get_children():
#             self.cart_tree.delete(i)
#         for item in self.cart:
#             self.cart_tree.insert("", tk.END, values=(item["name"], item["qty"]))

#     def checkout(self):
#         if not self.cart:
#             messagebox.showinfo("Cart Empty", "Your cart is empty.")
#             return
#         total_items = sum(item["qty"] for item in self.cart)
#         messagebox.showinfo("Checkout", f"Total items: {total_items}")
#         self.cart.clear()
#         self.update_cart_display()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ShoppingCartGUI(root)
#     root.mainloop()