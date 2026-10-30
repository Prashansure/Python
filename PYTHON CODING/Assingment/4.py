password = input("Enter password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

score = sum([has_upper, has_lower, has_digit, has_special])

if score == 4:
    print("Strong")
elif score >= 2:
    print("Medium")
else:
    print("Weak")