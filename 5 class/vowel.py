a = str(input("Enter a Text : "))


vowels = "aeiouAEIOU"
for char in a :
    if char in vowels:
        print(char)

    else:
        print("The Text Has No Vowels")