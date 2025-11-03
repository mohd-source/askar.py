# count occurrences of elements in a list
l1 = [10, 20, 4, 45, 99, 4, 20, 4]
print("Original List: ", l1)
value = int(input("Enter the element to count its occurrences: "))
count = l1.count(value)
print(f"Element {value} occurs {count} times in the list.")