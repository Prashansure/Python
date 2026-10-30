import os

source = "C:\\Users\\prash\\OneDrive\\Python_2026\\PYTHON CODING\\sessional-2"
destination = "C:\\Users\\prash\\OneDrive\\Python_2026\\PYTHON CODING\\hello.txt"



try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print("File moved successfully")

except FileNotFoundError:
    print("Source file not found")