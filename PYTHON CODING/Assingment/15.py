score = 0

questions = {
    "What is 2 + 2? ": "4",
    "Capital of India? ": "Delhi",
    "What is 5 * 3? ": "15"
}

for q in questions:
    answer = input(q)
    
    if answer.lower() == questions[q].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        continue

print("\nTotal Score:", score)