
inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}


inventory.update({
    "Smartphone": inventory["Smartphone"] + 10,
    "Headphones": inventory["Headphones"] + 5
})

print("Updated inventory:")
for item, qty in inventory.items():
    print(item, qty)


sold_item, sold_qty = inventory.popitem()
print(f"\nSold last item: {sold_item} (Quantity: {sold_qty})")


camera_stock = inventory.get("Camera", "Out of Stock")
print(f"\nCamera stock: {camera_stock}")
