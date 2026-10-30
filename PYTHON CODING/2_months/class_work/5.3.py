print("----- SIMPLE BANKING SYSTEM -----")

balance = 0  # Initial balance

while True:
    print("Current Balance: ₹", balance)
    print("Choose an option:")
    print("1. Credit (Deposit)")
    print("2. Debit (Withdraw)")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    match choice:
        case 1:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Amount credited successfully.")
            else:
                print("Invalid deposit amount.")

        case 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Amount debited successfully.")
                print("amount debeted: ₹",amount)

        case 3:
            print("Thank you for using the banking system.")
            break

        case _:
            print("Invalid choice. Please select again.")