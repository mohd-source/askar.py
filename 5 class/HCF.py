def computer_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

a = int(input("Enter First NO : "))
b = int(input("Enter Second NO : "))

hcf = computer_hcf(a , b) 


print("The HCF is " , hcf)