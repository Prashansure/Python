class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 18:
        raise AgeError("Not eligible")

    print("Eligible")

except AgeError as e:
    print(e)

except:
    print("Invalid input")