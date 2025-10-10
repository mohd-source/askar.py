

n = int(input("Enter no of subject :"))

total_marks = 0
maximum_marks = 100

for i in range(n):
    marks = int(input(f"Enter marks for sub { i + 1 } "))

total_marks += marks

print(marks)

per = (total_marks / ( n*maximum_marks )*100 )

print(per)
