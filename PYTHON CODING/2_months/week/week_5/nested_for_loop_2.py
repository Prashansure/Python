print("1. Matrix Display")
print("2. Multiplication Table")
print("3. string Pattern")
print("4. chessboard Pattern")

choice = int(input("enter your choice: "))

match choice:

    case 1:
      
        matrix = [[1, 2], [3, 4]]

        print("Matrix:")
        for i in matrix:
            for val in i:
                print(val, end=" ")
            print()

    case 2:
        # Multiplication Table
        n = int(input("Enter a number: "))

        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")

    case 3:
        # String Pattern
        s = "PYTHON"

        for i in range(len(s)):
            for j in range(i + 1):
                print(s[j], end="")
            print()

    case 4:
        # Chessboard Pattern
        n = 4

        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    print("W", end=" ")
                else:
                    print("B", end=" ")
            print()

    case _:
        print("invalid choice")