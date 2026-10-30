while True:
    print("\n----- Formula Based Simple Programs -----")
    print("1. Simple Interest")
    print("2. Area of a Circle")
    print("3. Celsius to Fahrenheit")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        p = int(input("Enter the principal amount: "))
        r = int(input("enter the rate of interest: "))
        t = int(input("Enter the time: "))
        si = (p * r * t) / 100
        print("Simple Interest =", si)

    elif choice == 2:
        r = float(input("Enter the radius of the circle: "))
        area_of_circle = 22 / 7 * r * r
        print("Area of Circle =", area_of_circle)

    elif choice == 3:
        C = float(input("Enter the temperature in Celsius: "))
        F = (C * 9 / 5) + 32
        print("Temperature in Fahrenheit =", F)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice! Please try again.")
