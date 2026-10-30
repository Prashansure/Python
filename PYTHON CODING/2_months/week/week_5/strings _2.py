c = int(input("enter the number: "))
match c:
    case 1 :
        s = input()
        count = 1

        for ch in s:
            if ch == " ":
                count += 1

        print(count)
    case 2:
        s = input("Enter string: ")

        for ch in set(s):
            print(ch, ":", s.count(ch))
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in freq:
            print(ch, ":", freq[ch])


