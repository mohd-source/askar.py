
grades = [85, 90, 78, 92, 88, 76, 95, 89]
print("Initial grade list of student:", grades)
print()


grades.append(80)
print("New grade 80 is added in list.The list is:", grades)
print()


grades.sort()
print("Grades Sorted in ascending order\n")


highest_grade = max(grades)

grades.remove(76)
print("A grade 76 is removed from the list.\n")


count_above_85 = 0

for grade in grades:
    if grade > 85:
        count_above_85 += 1



print("Final Grades List:", grades)
print("Highest Grade:", highest_grade)
print("Students Scoring Above 85:", count_above_85)






















