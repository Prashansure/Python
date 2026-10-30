total_slots = 100
available_slots = 100

print("Welcome to Mall Parking System")
print("Total Slots:", total_slots)

while True:
    print("\n--- MENU ---")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Check Slots")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("How many vehicles entering? "))
        if available_slots == 0:
            print("Sorry! Parking is Full.")
        elif n > available_slots:
            print("Only", available_slots, "slots available.")
        else:
            available_slots = available_slots - n
            print(n, "vehicle(s) parked")
            print("Slots Available:", available_slots)

    elif choice == "2":
        n = int(input("How many vehicles exiting? "))
        available_slots = available_slots + n
        if available_slots > total_slots:
            available_slots = total_slots
        print(n, "vehicle(s) exited.")
        print("Slots Available:", available_slots)

    elif choice == "3":
        if available_slots == 0:
            print("Parking is Full")
        else:
            print("Slots Available:", available_slots)

    elif choice == "4":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice")