e = int(input("Enter the size of list: "))

name_l = list(map(str, input("Enter Name Of Empolyee (Space-Separated): ").strip().split()))[:e]


for i in range(len(name_l)):
    print(f"{i+1}.", name_l[i])
    print()


rate_l = list(map(int, input("Enter Rate Of Empolyee (Space-Separated): ").strip().split()))[:e]


for i in range(len(name_l)):   
    print()
    print()
    print() 


    if rate_l[i] == 5 :
        print(f"{name_l[i]} resive 1000 bonus")
        

    elif rate_l[i] == 4 :
        print(f"{name_l[i]} resive 750 bonus")
      
    

    elif rate_l[i] == 3 :
        print(f"{name_l[i]} resive 500 bonus")
       

    
    elif rate_l[i] == 2 :
        print(f"{name_l[i]} resive 250 bonus")
        
    else:
        print("no bonus")


print()
print()

