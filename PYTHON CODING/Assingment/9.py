def add_student():
    file = open("students.txt", "a")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    file.write(name + "," + marks + "\n")
    file.close()

def search_student():
    file = open("students.txt", "r")
    name = input("Enter name to search: ")
    found = False

    for line in file:
        data = line.strip().split(",")
        if data[0] == name:
            print("Record Found:", data)
            found = True

    if not found:
        print("Student not found")

    file.close()

def update_student():
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    name = input("Enter name to update: ")
    new_marks = input("Enter new marks: ")

    file = open("students.txt", "w")

    for line in lines:
        data = line.strip().split(",")
        if data[0] == name:
            file.write(name + "," + new_marks + "\n")
        else:
            file.write(line)

    file.close()

# Menu
while True:
    print("\n1. Add\n2. Search\n3. Update\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    else:
        break