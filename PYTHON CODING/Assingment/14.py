import time

while True:
    print("\n🔴 Red Light - STOP")
    time.sleep(3)

    print("🟡 Yellow Light - WAIT")
    time.sleep(2)

    print("🟢 Green Light - GO")
    time.sleep(3)

    choice = input("\nPress 'q' to stop or Enter to continue: ")
    if choice == 'q':
        break