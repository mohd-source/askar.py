student_list = []

def add_student():

    name = input("\nEnter Name: ")
    roll_no = int(input("Enter Roll No: "))
    marks = int(input("Enter Marks: "))

    student_list.append({"name": name, "roll no": roll_no, "marks": marks})
    print("Student added successfully\n")



def view_student():
    if not student_list:
        print("No Student Recorde")

    else:
        for i in student_list:
            print(f"name {i['name']} | roll_no {i['roll_no']} | marks {i['marks']}")


def search_student():
    rno = int(input("Enter Roll No to search: "))
    for i in student_list:
        if i['roll no'] == rno:
            print(f"name {i['name']} | roll_no {i['roll no']} | marks {i['marks']}")
