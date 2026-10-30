print("----- Student Grading System -----")

a = float(input("Enter the marks: "))

if a > 100 or a < 0:
    print("Invalid marks")

elif a >= 90:
    print("Grade A+")

elif a >= 80:
    print("Grade A")

elif a >= 70:
    print("Grade B+")

elif a >= 60:
    print("Grade B")

elif a >= 50:
    print("Grade C")

else:
    print("Fail")