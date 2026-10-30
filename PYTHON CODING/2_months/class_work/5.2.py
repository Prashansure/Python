import math

print(" MENU DRIVEN CALCULATOR ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        result = num1 + num2
        print("Result:", result)

    elif choice == 2:
        result = num1 - num2
        print("Result:", result)

    elif choice == 3:
        result = num1 * num2
        print("Result:", result)

    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed")

    elif choice == 5:
        result = math.pow(num1, num2)
        print("Result:", result)

    elif choice == 6:
        if num1 >= 0 and num2 >= 0:
            result1 = math.sqrt(num1)
            print("Result:", result1)
            result2 = math.sqrt(num2)
            print("Result:", result2)
        else:
            print("Error: Square root of negative number not possible")
    elif choice == 7:
        print("exiting program..")
        break

    else:
        print("Invalid choice")