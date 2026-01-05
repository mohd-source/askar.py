
courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

courses["Data Structures"]["Alice"] = 90
courses["Data Structures"].pop("Charlie", None)

courses["Web Development"] = {"Grace": 92, "Henry": 85}

if "Bob" not in courses["Algorithms"]:
    courses["Algorithms"]["Bob"] = 80

courses.pop("Machine Learning", None)

data_structures_grades = courses.get("Data Structures")
if data_structures_grades:
    average_grade = sum(data_structures_grades.values()) / len(data_structures_grades)
else:
    average_grade = "Course not found"

print("Final Courses Dictionary:")
for course, students in courses.items():
    print(course, ":", students)

print("\nAverage grade for Data Structures:", average_grade)
