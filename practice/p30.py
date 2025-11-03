# create a dictionary with student names as keys and their scores as values find the average score of the class and print it
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

average_score = sum(student_scores.values()) / len(student_scores)
print(student_scores)
print(f"The average score of the class is: {average_score}")

