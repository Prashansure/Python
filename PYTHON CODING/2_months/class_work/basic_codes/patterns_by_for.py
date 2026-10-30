print("1. Right Triangle")
print("2. Inverted Right Triangle")
print("3. Pyramid")
print("4. Inverted Pyramid")
print("5. Diamond")
print("6. Square")
print("7. Number Triangle")
print("8. Same Number Pattern")
print("9. Floyd's Triangle")
print("10. Hollow Square")

choice = int(input("Enter your choice (1-10): "))
n = int(input("Enter number of rows: "))

match choice:

    case 1:   # Right Triangle
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")
            print()

    case 2:   # Inverted Right Triangle
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

    case 3:   # Pyramid
        for i in range(n):
            for s in range(n - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()

    case 4:   # Inverted Pyramid
        for i in range(n):
            for s in range(i):
                print(" ", end="")
            for j in range(2 * (n - i) - 1):
                print("*", end="")
            print()

    case 5:   # Diamond
        for i in range(n):
            for s in range(n - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()
        for i in range(n - 2, -1, -1):
            for s in range(n - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()

    case 6:   # Square
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

    case 7:   # Number Triangle
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    case 8:   # Same Number Pattern
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end="")
            print()

    case 9:   # Floyd's Triangle
        num = 1
        for i in range(1, n + 1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()

    case 10:  # Hollow Square
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    case _:
        print("Invalid choice")
