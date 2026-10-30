print("1.Prime numbers\n2.perfect numbers")
c = int(input("enter the number: "))

match c:
    case 1:
        for num in range(2,21):
            for i in range(2,num):
                if num %i == 0:
                    break
            else:
                print(num)
    case 2:
        for num in range(1,51):
            s = 0
            for i in range(1,num):
                if num %i == 0:
                    s += i
            if s == num:
                print(num)
                                               
    