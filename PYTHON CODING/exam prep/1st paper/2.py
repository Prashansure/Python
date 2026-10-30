students = {}
for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    students[name] = score
    
highest = max(students.values())
lowest = min(students.values())
average = sum(students.values()) / len(students)
for name, score in students.items():
    if score == highest:
        top_student = name
# result dictionary
result = {
    "highest": highest,
    "lowest": lowest,
    "average": average,
    "top_student": top_student
}

print(result)