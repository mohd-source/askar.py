attendance_list = []

print("Enter student names to mark attendance.")
print("Type 'done' after completing your list.\n")

while True:
    name = input("Enter student name: ").strip()


    if name.lower() == "done":
        break

    
    if name == "":
        continue

    
    if name in attendance_list:
        attendance_list.remove(name)
        print(f"{name} was already marked. Enter different name.\n")
    else:
        attendance_list.append(name)
        print(f"{name} added to attendance.\n")


print("\nFinal Attendance List:")
if len(attendance_list) == 0:
    print("\tNo students were marked as present.")
else:
    for student in attendance_list:
        print("\t",student)
