
class add:
    def add(self, a, b):
        return a + b
addd = add()



class sub:
    def sub(self, a, b):
        return a - b
subb = sub()



class multi:
    def multi(self, a, b):
        return a * b
multii = multi()



class dev:
    def dev(self, a, b):
        return a / b
devv = dev()






while True:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))




    print(" 1. Add\n 2. Sub\n 3. Multi\n 4. Devide\n 5. Exit")
    print()
    print()

    c = int(input("What do u want to do ...(1-4)\n"))


    if c == 1:

        print(f"The Addition of {x} and {y} is : { addd.add(x, y)}")



    elif c == 2:

        print(f"The Subtraction of {x} and {y} is : {subb.sub(x, y)}")



    elif c == 3:

        print(f"Multipacationof {x} and {y} is :", multii.multi(x, y))



    elif c == 4:


        print(f"Devision  of {x} and {y} is : ", devv.dev(x, y))
    


    elif c == 5:
        break



