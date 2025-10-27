# # e = int(input("How many items you purchase: "))
# # item = []
# # item = list(map(str, input("Enter item (Space-Separated): ").strip().split()))[:e]
# # price = []
# # price = list(map(float, input("Enter price of items (Space-Separated): ").strip().split()))[:e]
# # q = str(input("\nYou have any discount coupon (yes/no): "))



# # def calculate_final_price(e, item, price, q):
   
# #     print()
    
    
    
# #     print("Items purchased:\n\n", item)
    
    
   
   
    
# #     print("Price of items purchased:\n\n", price)
    
    
    
# #     total = 0
# #     for i in range(e):
# #         total += price[i]
# #     print("\nTotal price of items purchased:", total)
# #     print()
    
    
    
    
# #     if q.lower() == "yes":
# #         discount = float(input("Enter discount percentage: "))
# #         discount_amount = (discount / 100) * total
# #         final_price = total - discount_amount
# #         print(f"\nFinal price after {discount}% discount: {final_price}")
# #     else:
# #         print("\nNo discount applied.")
# #         print(f"Final price: {total}")




# # calculate_final_price(e, item, price, q)
# import tkinter as tk
# from tkinter import messagebox

# def calculate_final_price():
#     try:
#         # Get the entered items and prices
#         items = entry_items.get().split()
#         prices = list(map(float, entry_prices.get().split()))

#         if len(items) != len(prices):
#             messagebox.showerror("Input Error", "Number of items and prices must match!")
#             return

#         total = sum(prices)
#         has_coupon = coupon_var.get()

#         # If user selected "Yes" for coupon
#         if has_coupon == "yes":
#             try:
#                 discount = float(entry_discount.get())
#                 final_price = total * (1 - discount / 100)
#                 result_text.set(f"Total: ₹{total:.2f}\nDiscount: {discount}%\nFinal Price: ₹{final_price:.2f}")
#             except ValueError:
#                 messagebox.showerror("Input Error", "Please enter a valid discount percentage!")
#         else:
#             result_text.set(f"Total: ₹{total:.2f}\nNo discount applied.\nFinal Price: ₹{total:.2f}")

#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numeric prices.")

# # --- Main Window ---
# root = tk.Tk()
# root.title("Shopping Bill Calculator")
# root.geometry("400x400")
# root.config(bg="#f9f9f9")

# # --- UI Elements ---
# tk.Label(root, text="Enter Item Names (space-separated):", bg="#f9f9f9").pack(pady=5)
# entry_items = tk.Entry(root, width=50)
# entry_items.pack(pady=5)

# tk.Label(root, text="Enter Prices (space-separated):", bg="#f9f9f9").pack(pady=5)
# entry_prices = tk.Entry(root, width=50)
# entry_prices.pack(pady=5)

# # Coupon option
# tk.Label(root, text="Do you have a discount coupon?", bg="#f9f9f9").pack(pady=5)
# coupon_var = tk.StringVar(value="no")
# tk.Radiobutton(root, text="Yes", variable=coupon_var, value="yes", bg="#f9f9f9").pack()
# tk.Radiobutton(root, text="No", variable=coupon_var, value="no", bg="#f9f9f9").pack()

# # Discount input
# tk.Label(root, text="If Yes, enter discount percentage:", bg="#f9f9f9").pack(pady=5)
# entry_discount = tk.Entry(root, width=10)
# entry_discount.pack(pady=5)

# # Calculate button
# tk.Button(root, text="Calculate Final Price", command=calculate_final_price, bg="#4CAF50", fg="white").pack(pady=15)

# # Result display
# result_text = tk.StringVar()
# tk.Label(root, textvariable=result_text, bg="#f9f9f9", fg="#333", font=("Arial", 12), justify="left").pack(pady=10)

# # Run the window
# root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox

class ShoppingBillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛍️ Shopping Bill Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("TLabel", font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=25)

        # ======== Title ========
        ttk.Label(root, text="Shopping Bill Calculator", font=("Arial", 16, "bold")).pack(pady=10)

        # ======== Frame for adding items ========
        add_frame = ttk.Frame(root)
        add_frame.pack(pady=10)

        ttk.Label(add_frame, text="Item Name:").grid(row=0, column=0, padx=5)
        self.item_name = ttk.Entry(add_frame, width=20)
        self.item_name.grid(row=0, column=1, padx=5)

        ttk.Label(add_frame, text="Quantity:").grid(row=0, column=2, padx=5)
        self.item_qty = ttk.Entry(add_frame, width=8)
        self.item_qty.grid(row=0, column=3, padx=5)

        ttk.Label(add_frame, text="Price:").grid(row=0, column=4, padx=5)
        self.item_price = ttk.Entry(add_frame, width=10)
        self.item_price.grid(row=0, column=5, padx=5)

        ttk.Button(add_frame, text="Add Item", command=self.add_item).grid(row=0, column=6, padx=10)

        # ======== Treeview Table ========
        columns = ("Item", "Quantity", "Price", "Total")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)
        self.tree.pack(pady=10)

        # ======== Discount Frame ========
        discount_frame = ttk.Frame(root)
        discount_frame.pack(pady=10)

        ttk.Label(discount_frame, text="Discount Coupon (%):").grid(row=0, column=0, padx=5)
        self.discount_entry = ttk.Entry(discount_frame, width=10)
        self.discount_entry.grid(row=0, column=1, padx=5)
        ttk.Button(discount_frame, text="Apply Discount", command=self.apply_discount).grid(row=0, column=2, padx=10)

        # ======== Buttons ========
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Calculate Total", command=self.calculate_total).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=1, padx=10)

        # ======== Result Label ========
        self.result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"), foreground="blue")
        self.result_label.pack(pady=10)

        self.total_amount = 0.0

    # --- Add Item Function ---
    def add_item(self):
        name = self.item_name.get().strip()
        try:
            qty = int(self.item_qty.get())
            price = float(self.item_price.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid quantity and price.")
            return

        if not name:
            messagebox.showerror("Missing Data", "Please enter an item name.")
            return

        total = qty * price
        self.tree.insert("", "end", values=(name, qty, price, total))

        self.item_name.delete(0, tk.END)
        self.item_qty.delete(0, tk.END)
        self.item_price.delete(0, tk.END)

    # --- Calculate Total Function ---
    def calculate_total(self):
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning("No Items", "Please add items first.")
            return

        total = sum(float(self.tree.item(i, "values")[3]) for i in items)
        self.total_amount = total
        self.result_label.config(text=f"Total Amount: ₹{total:.2f}")

    # --- Apply Discount Function ---
    def apply_discount(self):
        if self.total_amount == 0:
            self.calculate_total()

        try:
            discount = float(self.discount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid discount percentage.")
            return

        if discount < 0 or discount > 100:
            messagebox.showerror("Invalid Discount", "Discount must be between 0 and 100.")
            return

        discount_amt = (discount / 100) * self.total_amount
        final_price = self.total_amount - discount_amt
        self.result_label.config(text=f"Total: ₹{self.total_amount:.2f}\nDiscount: {discount}%\nFinal Price: ₹{final_price:.2f}")

    # --- Clear Function ---
    def clear_all(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.item_name.delete(0, tk.END)
        self.item_qty.delete(0, tk.END)
        self.item_price.delete(0, tk.END)
        self.discount_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.total_amount = 0.0


# ======== Run the App ========
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingBillApp(root)
    root.mainloop()
