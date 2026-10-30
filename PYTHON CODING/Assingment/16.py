books = {
    "Python": True,
    "Java": True,
    "C++": True
}

def issue_book():
    name = input("Enter book name: ")
    
    if name in books:
        if books[name]:
            books[name] = False
            print("Book issued successfully")
        else:
            print("Book already issued")
    else:
        print("Book not found")

def return_book():
    name = input("Enter book name: ")
    
    if name in books:
        books[name] = True
        print("Book returned successfully")
    else:
        print("Book not found")

# Menu
while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Show Books")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        issue_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        print(books)
    else:
        break