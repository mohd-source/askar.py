# n = int(input("Enter number of students: ")) 


# attandence_list = []

# for i in range(0, n+1):

#     name = input("Enter student name (or type 'exit' to finish): ")
#     print()    


#     if name.lower() == 'exit':
#         break

    
#     if name in attandence_list:
#         print(f"{name} is already in the attendance list.")
    
    
#     else:
#         attandence_list.append(name)
#         print()
#         print(f"{name} has been added to the attendance list.")



# print("\nAttendance List:")

# sorted_list = sorted(attandence_list)

# for student in attandence_list:

#     print()
#     print(student)




# print("sotred list is : ", sorted_list )



# attandence_list_2 = []
# name_2 = input("Enter student name to check attendance: ")
# if name_2 in attandence_list_2:
#     attandence_list_2.append(name_2)
#     print(f"{name_2} is present in the attendance list.")
# else:
#     print(f"{name_2} is not present in the attendance list.")# print()
# # print()   



# Mark attendance

attendance_list = []

n = int(input("Enter number of students: "))



for i in range(n):
    name = input(f"Enter name of present student {i+1}: ")




    if name not in attendance_list:
        attendance_list.append(name)
        print(f"{name} marked present.")



    else:
        print(f"{name} is already marked present.")

print("\nAttendance List:")

attendance_list1 = sorted(attendance_list)

for student in range(0, 1):
    print(attendance_list1)

i = 1
for j in range(n):

    
    check_name = input("\nEnter a name to check attendance: ")
    
    if check_name in attendance_list:
        print(f" {check_name} is present.")
    else:
        print(f"{check_name} is absent.") 













