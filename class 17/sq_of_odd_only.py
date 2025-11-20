odd_square = []
even_sq = []

for x in range(0,21 ):
    if x%2 != 0:    
        odd_square.append(x**2)
print("\t\t Odd square: \n",odd_square, "\n")


for x in range(0, 22, 2):

    even_sq.append(x**2)
print("\t\t Even square: \n", even_sq)


sum_odd = sum(odd_square)
sum_even = sum(even_sq)
print("\nSum of odd squares: ", sum_odd)
print("Sum of even squares: ", sum_even)


add = sum_odd + sum_even
print("Sum of odd and even squares: ", add)