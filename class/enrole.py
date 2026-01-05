from abc import ABC, abstractmethod

class CourseBase(ABC):
    @abstractmethod
    def enroll_student(self, student_name):
        pass

    @abstractmethod
    def drop_student(self, student_name):
        pass

    @abstractmethod
    def display_course(self):
        pass


class course(CourseBase):
    def __init__(self, course_name, course_code, max_student):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__max_student = max_student
        self.__students = []

    def enroll_student(self, student_name):
        if len(self.__students) < self.__max_student:
            self.__students.append(student_name)
            print(f"{student_name} has been enrolled in {self.__course_name}.")
        else:
            print(f"enrolled failed")

    
    def drop_student(self, student_name):
        if student_name in self.__students:
            self.__students.remove(student_name)
            print(f"{student_name} has been dropped from {self.__course_name}.")
        else:
            print(f"{student_name} is not enrolled in this course.")
    


    def display_course(self):
        print("\nCourse Details")
        print(f"Name       : {self.__course_name}")
        print(f"Code       : {self.__course_code}")
        print(f"Max Seats  : {self.__max_student}")
        print(f"Enrolled   : {len(self.__students)} students")
















































































            # print(f"Cannot enroll {student_name}. {self.__course_name} is full.")
# 
    # def drop_student(self, student_name):
        # if student_name in self.__students:
            # self.__students.remove(student_name)
            # print(f"{student_name} has dropped {self.__course_name}.")
        # else:
            # print(f"{student_name} is not enrolled in {self.__course_name}.")
# 
    # def display_course(self):
        # print(f"\nCourse: {self.__course_name} ({self.__course_code})")
        # print(f"Maximum Students: {self.__max_student}")
        # print(f"Enrolled Students ({len(self.__students)}): {self.__students}")
# 
# 
# Example usage
# python_course = course("Python Programming", "CSE101", 3)
# ds_course = course("Data Structures", "CSE202", 2)
# 
# python_course.enroll_student("Ali")
# python_course.enroll_student("Sara")
# python_course.enroll_student("Ahmed")
# python_course.enroll_student("Usman")
# 
# ds_course.enroll_student("Ali")
# ds_course.enroll_student("Sara")
# ds_course.enroll_student("Ahmed")
# 
# python_course.drop_student("Sara")
# python_course.enroll_student("Usman")
# 
# python_course.display_course()
# ds_course.display_course()