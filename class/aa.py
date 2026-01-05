data = "STU|Steamupqbhs|AGE:22|GPA=3.44|DEPT-CS|CGPA-3.51|SEM-07|R-NO=0911|DURATION-3 Hour"


name = data.split("|")[1]
age = int(data[data.index("AGE:") + 4 : data.index("|GPA")])
gpa = float(data[data.index("GPA=") + 4 : data.index("|DEPT")])
cgpa = float(data[data.index("CGPA-") + 5 : data.index("|SEM")])
dept = data[data.index("DEPT-")  + 5  : data.index("|CGPA")]
sem = int(data[data.index("SEM-") + 4 : data.index("|R-NO")])
rno = int(data[data.index("R-NO=") + 5 : data.index("|DURATION")])
dur = data[data.index("DURATION-")  + 9  : ]

per = (gpa/4)*100
print(per)
print()


print("\n\tName\t\t\t:\t\t\t",name)
print("\tAge\t\t\t:\t\t\t",age)
print("\tGPA\t\t\t:\t\t\t",gpa)
print("\tDEPT\t\t\t:\t\t\t",dept)
print("\tCGPA\t\t\t:\t\t\t",cgpa)
print("\tSEMESTER\t\t:\t\t\t",sem)
print("\tRoll-NO\t\t\t:\t\t\t",rno)
print("\tDuration Of Course\t:\t\t\t",dur)
print(f"""\n\t   ------------------------------------------------
\t   |Converted GPA Percentage is\t:\t      {per}|
\t   ------------------------------------------------""")
print()

