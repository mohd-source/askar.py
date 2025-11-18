
students_scores = {
    "kamran": [85, 92, 78],
    "asif": [79, 95, 88],
    "abrar": [92, 90, 85],
    "danyial": [70, 75, 80]
}


def calculate_average_scores(scores_dict):
    averages = {}
    for name, scores in scores_dict.items():
        avg_score = sum(scores) / len(scores)
        averages[name] = avg_score
    return averages


average_scores = calculate_average_scores(students_scores)


top_student = max(average_scores, key=average_scores.get)
top_average = average_scores[top_student]


print(f"Average scores: {average_scores}")
print(f"Top student: {top_student}, Average Score: {top_average:.2f}")