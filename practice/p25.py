# function to calculate factorial of a number
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  
    return factorial

n = 5
print(f"The factorial of {n} is: {factorial(n)}")