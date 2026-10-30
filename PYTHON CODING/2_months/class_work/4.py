while True:
    print("\n--- MENU ---")
    print("1 for leap year")
    print("2 for login authentication system")
    print("3 for ticket pricing")
    print("4 for loan eligibility")
    print("5 for traffic signal system")
    print("6 for exit")
    
    case = int(input("enter the case you want: "))
    
    match case:
        case 1: 
            year = int(input("Enter year: "))
            if (year % 400 == 0) or (year %4 == 0):
                if (year %100 == 0):
                    print("Leap Year")
            else:
                print("Not Leap Year")
        
        case 2:
            username = input("write username: ")
            password = input("write password: ")
            if username == "admin" and password == "1234":
                print("Login Successful")
            else:
                print("Invalid Credentials")
        
        case 3:
            age = int(input("Enter age: "))
            if age < 5:
                price = 0
            elif age <= 12:
                price = 50
            elif age <= 60:
                price = 100
            else:
                price = 60
            print(f"Ticket Price: {price}")
            
        case 4:
            salary = int(input("Enter salary: "))
            credit_score = int(input("Enter credit score: "))
            if salary >= 30000 and credit_score >= 700:
                print("Eligible for Loan")
            else:
                print("Not Eligible")
        
        case 5:
            signal = input("Enter signal color: ").lower()
            match signal:
                case "red":
                    print("Stop")
                case "yellow":
                    print("Ready")
                case "green":
                    print("Go")
                case _:
                    print("Invalid Signal")
        
        case 6:
            print("exiting the program")
            break
            
        case _:
            print("invalid choice")