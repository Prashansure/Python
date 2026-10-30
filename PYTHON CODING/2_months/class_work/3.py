# MENU DRIVEN PROGRAM

while True:
    print("\n--- MENU ---")
    print("1. Integer Operations")
    print("2. Float Operations")
    print("3. Complex Number Operations")
    print("4. Boolean Operations")
    print("5. String Operations")
    print("6. List Operations")
    print("7. Tuple Operations")
    print("8. Dictionary Operations")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b)
        print("Floor Division:", a // b)
        print("Modulus:", a % b)
        print("Power:", a ** b)

    elif choice == 2:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        print("Addition:", x + y)
        print("Subtraction:", x - y)
        print("Multiplication:", x * y)
        print("Division:", x / y)

    elif choice == 3:
        c1 = complex(input("Enter 1st complex number (a+bj): "))
        c2 = complex(input("Enter 2nd complex number (a+bj): "))

        print("Addition:", c1 + c2)
        print("Subtraction:", c1 - c2)
        print("Multiplication:", c1 * c2)

    elif choice == 4:
        p = input("Enter True/False: ").lower() == "true"
        q = input("Enter True/False: ").lower() == "true"

        print("AND:", p and q)
        print("OR:", p or q)
        print("NOT p:", not p)

    elif choice == 5:
        name = input("Enter your name: ")
        language = input("Enter your favorite language: ")

        print("Concatenation:", name + " " + language)
        print("Repetition:", name * 3)
        print("Length:", len(name))

    elif choice == 6:
        numbers = list(map(int, input("Enter numbers: ").split()))

        numbers.append(6)
        print("After append:", numbers)

        if 3 in numbers:
            numbers.remove(3)
            print("After removing 3:", numbers)

        if len(numbers) > 4:
            print("Element at index 4:", numbers[4])

    elif choice == 7:
        colors = tuple(input("Enter colors: ").split())
        print("Tuple:", colors)

    elif choice == 8:
        student = {}
        student["name"] = input("Enter student name: ")
        student["age"] = int(input("Enter student age: "))
        student["grade"] = input("Enter student grade: ")

        print("Student Details:", student)

    elif choice == 9:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1-9.")
