def factorial(num):

    if num == 1:
        return num
    

    else :


        return num * factorial(num - 1)
    
num = int(input("Enter a no: "))

if num < 0:
    print("Factorial can not be found of -ve NO")


elif num == 1:
    print( "Factorial of 0 in 1" ) 

else :
    print("Factorial of " , num ," is : " , factorial(num) )
    
    
    