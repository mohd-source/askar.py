a = int(input("Enter Value of NO 1 : "))
b = int(input("Enter Value of NO 2 : "))
print()
print()




print(" 1. Add\n 2. Sub\n 3. Multi\n 4. Devide")
print()
print()


add = a + b
sub = a - b
multi = a * b
devide = a / b

c = int(input("What do u want to do ...\n"))


if c == 1:

    print(f"The Addition of {a} and {b} is : ")
    print(float(add))


elif c == 2:
    
    print(f"The Subtraction of {a} and {b} is : ")
    print(float(sub))


elif c == 3:

    print(f"The Subtraction of {a} and {b} is : ")
    print(float(multi))


elif c == 4:
    
    print(f"The Subtraction of {a} and {b} is : ")
    print(float(devide))


