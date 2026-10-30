s = input("enetr string of 3 char: ")
print(len(s))
for i in range (4):
    for j in range (4):
        for k in range (4):
            if i!= j and j!=k and k!=i:
                print(s[i] + s[j] + s[k])
    
    