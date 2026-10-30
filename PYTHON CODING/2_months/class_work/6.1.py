# Python Programs using for statement
# Write a Python program to convert a given decimal number into its binary equivalent.
# Write a Python program to find the Greatest Common Divisor (GCD) of two given numbers.
# Write a Python program to find the Least Common Multiple (LCM) of two given numbers.
# Write a Python program to print all the prime numbers from the given set of numbers.
# Write a Python program to print number patterns using for loop
# Write a Python program to check whether a given number is:
# a) Palindrome
# b) Perfect
# c) Strong
# d) Armstrong
# To find the sum of squares of first n natural numbers.
# To print number pattern using nested for loop.
# To generate Fibonacci series up to n terms.
# To check whether a given number is a palindrome.
# To reverse a given number using for loop.
while True:
    print("\n------ MENU ------")
    print("1. Decimal to Binary")
    print("2. GCD of two numbers")
    print("3. LCM of two numbers")
    print("4. Prime numbers from a set")
    print("5. Palindrome (string)")
    print("6. Perfect number")
    print("7. Strong number")
    print("8. Armstrong number")
    print("9. sum of squares of first n natural numbers")
    print("10. Number pattern")
    print("11. Fibonacci series")
    print("12. Palindrome number")
    print("13. Reverse a number")
    print("14. Exit")

    choice = int(input("ent your choice: "))

    match choice:

        # Decimal to Binary
        case 1:
            n = int(input("enter number: "))
            bi = ""
            if n == 0:
                bi= "0"
            else:
                for _ in range(n):
                    if n == 0:
                        break
                    bi = str(n % 2) + bi
                    n //= 2
            print("Binary:", bi)

        # GCD
        case 2:
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
            gcd = 1
            for i in range(1, min(a, b) + 1):
                if a % i == 0 and b % i == 0:
                    gcd = i
            print("GCD:", gcd)

        # LCM
        case 3:
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
            for i in range(max(a, b), a * b + 1):
                if i % a == 0 and i % b == 0:
                    print("LCM:", i)
                    break

        # Prime numbers from set
        case 4:
            nums = list(map(int, input("enter numbers: ").split()))
            print("Prime numbers are:")
            for n in nums:
                if n > 1:
                    for i in range(2, n):
                        if n % i == 0:
                            break
                    else:
                        print(n, end=" ")
            print()

        # Palindrome string
        case 5:
            s = input("enter value: ")
            rev = ""
            for ch in s:
                rev = ch + rev
            if s == rev:
                print("Palindrome")
            else:
                print("Not Palindrome")

        # Perfect number
        case 6:
            n = int(input("enter number: "))
            total = 0
            for i in range(1, n):
                if n % i == 0:
                    total += i
            if total == n:
                print("Perfect number")
            else:
                print("Not Perfect")

        # Strong number
        case 7:
            n = int(input("enter number: "))
            temp = n
            sum_fact = 0
            for d in str(n):
                fact = 1
                for i in range(1, int(d) + 1):
                    fact *= i
                sum_fact += fact
            if sum_fact == temp:
                print("Strong number")
            else:
                print("Not Strong")

        # Armstrong number
        case 8:
            n = int(input("enter number: "))
            power = len(str(n))
            total = 0
            for d in str(n):
                total += int(d) ** power
            if total == n:
                print("Armstrong number")
            else:
                print("Not Armstrong")

        # sum of squares
        case 9:
            n = int(input("enter n: "))
            s = 0
            for i in range(1, n + 1):
                s += i * i
            print("sum of squares:", s)

        # Number pattern
        case 10:
            n = int(input("enter rows: "))
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()

        # Fibonacci series
        case 11:
            n = int(input("enter terms: "))
            a, b = 0, 1
            for _ in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

        # Palindrome number
        case 12:
            n = input("enter number: ")
            rev = ""
            for ch in n:
                rev = ch + rev
            if n == rev:
                print("Palindrome number")
            else:
                print("Not Palindrome")

        # Reverse number
        case 13:
            n = input("enter number: ")
            rev = ""
            for ch in n:
                rev = ch + rev
            print("Reverse:", rev)

        # Exit
        case 14:
            print("Program ended.")
            break

        case _:
            print("Invalid choice")

        
                