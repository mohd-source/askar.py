print("\t\t  -------")
print("\n\t\t | TABLE | \n")
print("\t\t  -------")


n = int(input( "Enter a No to write it's Table : " ))

r = int(input( "\nGive Range : " ))


print("\n")


for i in range(1, r+1):


    print(f"|\t{n} X {i} = " , n*i , "")