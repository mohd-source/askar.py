text = "Hi, my name is Askar and I love programming!"

# Define vowels
vowels = "aeiouAEIOU"
cons = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"



count = 0
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


count_consonants = 0
for char in text:
    if char in cons:
        count_consonants += 1

print("Number of consonants:", count_consonants)

