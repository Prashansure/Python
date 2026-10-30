students = {
    "ram": [80, 90],
    "sam": [70, 60],
    "tom": []
}

topper_name = ""
highest_avg = 0

for name, marks in students.items():
    if marks:
        average = sum(marks) / len(marks)
    else:
        average = 0

    print(name, "average:", average)

    if average > highest_avg:
        highest_avg = average
        topper_name = name

print("Topper:", topper_name)