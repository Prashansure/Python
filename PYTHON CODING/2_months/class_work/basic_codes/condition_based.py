# biggest among 3 numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    if a > c:
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b > c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")

while True:
    print("\n---- MENU ----")
    print("1. Check Voting Eligibility")
    print("2. Check Leap Year")
    print("3. Find Student Grade")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    # 1. Voting eligibility
    if choice == 1:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")

    # 2. Leap year
    elif choice == 2:
        year1 = int(input("Enter any year: "))
        if year1 % 400 == 0:
            print("It is a leap year")
        elif year1 % 4 == 0 and year1 % 100 != 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")

    # 3. Grade calculation
    elif choice == 3:
        percentage = float(input("Enter your percentage: "))

        if percentage >= 80 and percentage <= 100:
            print("Your grade is A+")
        elif percentage >= 60:
            print("Your grade is A")
        elif percentage >= 50:
            print("Your grade is B")
        elif percentage >= 40:
            print("Your grade is C")
        elif percentage >= 35:
            print("Your grade is D")
        elif percentage >= 0:
            print("Your grade is F")
        else:
            print("You have entered a wrong percentage")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice! Try again.")
