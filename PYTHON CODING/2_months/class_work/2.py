# BIG PYTHON PROGRAM COVERING DATA TYPES
# 1. INTEGER DATA TYPE
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))

print("INTEGER OPERATIONS")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
print()

# 2. FLOAT DATA TYPE
x = float(input("enter the first number:"))
y = float(input("enter the second number:"))

print("FLOAT OPERATIONS")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print()

# 3. COMPLEX DATA TYPE
c1 = complex(input("enter 1st complex number (a+bj):"))
c2 = complex(input("enter 2nd complex number (a+bj):"))

print("COMPLEX NUMBER OPERATIONS")
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print()

# 4. BOOLEAN DATA TYPE
p = input("enter boolean value True/False:").lower() == 'true'
q = input("enter boolean value True/False:").lower() == 'true'

print("BOOLEAN OPERATIONS")
print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)
print()

# 5. STRING DATA TYPE
name = input("enter your name:")
language = input("enter your favorite programming language:")

print("STRING OPERATIONS")
print("Concatenation:", name + " " + language)
print("Repetition:", name * 3)
print("Length:", len(name))
print()


# 6. LIST DATA TYPE
numbers = list(map(int, input("enter the numbers: ").split()))

print("LIST OPERATIONS")
numbers.append(6)
print("After append:", numbers)
numbers.remove(3)
print("After remove:", numbers)
print("Access element:", numbers[2])
print()

# 7. TUPLE DATA TYPE
colors = tuple(( input("enter the colors: ").split()))

print("TUPLE OPERATIONS")
print("Tuple:", colors)
print("Access element:", colors[1])
print("Length:", len(colors))
print()

# 8. DICTIONARY DATA TYPE
student = {}
student["name"] = input("enter student name:")
student["age"] = int(input("enter student age:"))
student["grade"] = input("enter student grade:")


print("DICTIONARY OPERATIONS")
print("Student name:", student["name"])
student["age"] = 16
print("Updated age:", student["age"])
print("All keys:", student.keys())
print("All values:", student.values())


