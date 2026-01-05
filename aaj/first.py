import math
print("-------------------- Average of List --------------------")
num = list(map(int, input("Enter Elements (Space-Separated): ").strip().split()))





if len(num) == 0:
    print("\nError! Please Enter Some Number to Calculate\n")



else:
    print(num)
    print(len(num))
    print(sum(num))

    avg = sum(num) / len(num)

    print(f"Average of numbers is {avg}")


    num.sort()

    print(f"Sorted list is {num} ")
