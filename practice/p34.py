student_list = []

def add_s():
    name = input(str("\nEnter name: "))
    rno = int(input("Enter Roll No: "))
    marks = int(input("Enter Marks: "))
    grade = input(str("Enter Grade: \n"))
    student_list.append({"name": name, "roll no": rno, "marks": marks, "grade": grade})
    print("Student added successfully")


def view_s():
    if not student_list:
        print("No Student Record")

    else:
        for i in student_list:
            print(f"name: {i['name']} | roll no: {i['roll no']} | marks: {i['marks']} | grade: {i['grade']}")


def search_s():
    r_no = input(int("Enter Roll No to search: "))
    for i in student_list:
        if i['roll no'] == r_no:
            print(f"name: {i['name']} | roll no: {i['roll no']} | marks: {i['marks']} | grade: {i['grade']}")
            break
    else:
        print("Student not found")




def delete_s():
    r_no = input(int("Enter Roll No to delete: "))
    for i in student_list:
        if i['roll no'] == r_no:
            student_list.remove(i)
            print("Student record deleted successfully")
            break
    else:
        print("Student not found")


def update_s():
    r_no = int(input("Enter Roll No to update: "))
    for i in student_list:
        if i['roll no'] == r_no:
            name = input(str("Enter new name: "))
            marks = int(input("Enter new Marks: "))
            grade = input(str("Enter new Grade: "))
            i['name'] = name
            i['marks'] = marks
            i['grade'] = grade
            print("Student record updated successfully\n")
            break
    else:
        print("Student not found")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_s()
        elif choice == 2:
            view_s()
        elif choice == 3:
            search_s()
        elif choice == 4:
            delete_s()
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again.")

main()










