s = input("enetr the string: ")
lower = upper = digit = spec = 0

for i in s:
    if i>='a' and i<='z':
        lower +=1
    elif i>= 'A' and i<='Z':
        upper +=1
    elif i>= '0' and i<='9':
        digit +=1
    else :
        spec +=1
        
print(lower,upper,digit,spec)
        