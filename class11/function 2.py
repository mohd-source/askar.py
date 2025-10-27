def sum(a,b):
    c = a + b
    return c     

a = 10
b = 20

print("\nThe sum is:", sum(a,b) , "\n")






def func():
    print("WELCOME TO MY WORLD")
func()





def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3


num1 = 5
num2 = 10
result = add(num1, num2)
print(f"\nThe addition of {num1} and {num2} is: {result}")



def even_or_odd(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"



number = 7

result = even_or_odd(number)
print(f"\nThe number {number} is {result}.")

number1 = 8
result = even_or_odd(number1)
print(f"\nThe number {number1} is {result}.")
print()

# default argument 
def myfun(x, y = 30):
    print("x:", x)
    print("y:", y) 

myfun(10)
print()
myfun(10, 20)
print()

# keyword argument
def myfun1(firstname, lastname):
    print(firstname , lastname)


myfun1(firstname = "John", lastname = "Doe")
print()





def nameage(name, age):
    print("Hi \nI am ", name)
    print(f"I am {age} year old ")

print("Case--1\n")
nameage("S.M Baqar R.Z", 17)
print()
returning_value = nameage("Ali", 20)





def square(num):
    return num ** 2
result = square(6)
print("\nThe square is:", result)
print()




def multiply(x, y):
    m = x * y
    return m    
x = 5
y = 4
result = multiply(x, y)
print("\nThe multiplication is:", result)
print()





def name():
    name = "S.M Baqar R.Z"

    def age():
        print(name)
    age()
name()
       



# recursive function

def factorial(n):
    if n < 0 :
        return "Invalid input! Factorial is not defined for negative numbers."
    elif n == 0 :
        return 1
    else:
        return n * factorial(n - 1)

num = 5
result = factorial(num)   
print(f"\nThe factorial of {num} is: {result}\n")






