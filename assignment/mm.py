n = int(input("How meny empolyee u have: "))
a=1
name = []
rate = []
for i in range (n):
    name[i] = str(input(f"Enter the Name Of {a} Empolyee: "))
    rate[i] = int(input(f"Enter the Rate of {a} Empolyee: "))
    a += 1
    print()
    print()

for j in range(n):
    print(name[j], rate[j])


