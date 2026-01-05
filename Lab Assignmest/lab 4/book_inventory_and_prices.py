
books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

books_backup = books.copy()



print("Current inventory:\n")
for title, price in books.items():
    print(f"- {title}: ${price:.2f}")


total_value = sum(books.values())
print(f"\nTotal value of inventory: ${total_value:.2f}")

sold_book_price = books.pop("1984")
print(f'\nSold book: "1984" for ${sold_book_price:.2f}')


print("Final inventory:")
for title,price in books.items():
    print(f"- {title} ")

print("\nBackup of books Inventory is: \n")
for title, price in books_backup.items():
    print(f"- {title}: {price:.2f}")