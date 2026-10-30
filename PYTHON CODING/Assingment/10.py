balance = 5000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        raise ValueError("Invalid amount")

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Error:", e)

finally:
    print("Transaction completed")