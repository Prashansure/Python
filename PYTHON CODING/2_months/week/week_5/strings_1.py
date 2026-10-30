c = int(input("enter the number: "))
match c:
    case 1:
        s = input()
        print(s)
    case 2:
        s = input("Enter the string:")
        print(len(s))
    case 3:
        s = input("enter the string: ")
        result = ""
        for ch in s:
            if ch not in result:
                result +=ch
        print(result)
    case 4:
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")

        if len(s1) != len(s2):
            print("Not Anagrams")
        else:
            count = 0
            for ch in s1:
                for ch2 in s2:
                    if ch == ch2:
                        count += 1
                        break
            if count == len(s1):
                print("Anagrams")
            else:
                print("Not Anagrams")
    case 5:
        s = input("reverse")
        rev = ""
        for i in range(len(s)-1, -1, -1):
            rev += s[i]
        print(rev)
    case 6:
        s = input("")  
        rev = s[::-1] #slicing
        if s == rev:
            print("palindrome")              
        else:
            print("not a palindrome")

        