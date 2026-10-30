import os

path = "C:\\Users\\prash\\OneDrive\\Python_2026\\PYTHON CODING\\hello.txt"

if os.path.exists(path):
    print("Exist")

else:
    print("doesn't exist")
    