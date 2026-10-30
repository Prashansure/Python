while True:
    print("\n--- Number Pattern Menu ---")
    print("1. Right triangle")
    print("2. Same number triangle")
    print("3. Continuous numbers")
    print("4. Reverse triangle")
    print("5. Pyramid")
    print("0. Exit")

    choice = int(input("enter your choice: "))

    match choice:

        case 1:
            n = 4
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(j, end="")
                print()

        case 2:
            n = 4
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(i, end="")
                print()

        case 3:
            n = 4
            num = 1
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(num, end="")
                    num += 1
                print()

        case 4:
            n = 4
            for i in range(n, 0, -1):
                for j in range(1, i + 1):
                    print(j, end="")
                print()

        case 5:
            n = 4
            for i in range(1, n + 1):

                for space in range(n - i):
                    print(" ", end="")

                for j in range(1, i + 1):
                    print(j, end="")

                for j in range(i - 1, 0, -1):
                    print(j, end="")

                print()

        case 0:
            print("program ended")
            break

        case _:
            print("invalid choice, try again")
