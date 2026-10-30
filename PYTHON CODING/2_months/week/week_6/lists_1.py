s = ['d']
print(len(s))
count = 0
for i in s:
    count += 1
print(count)

y = input("Enter the sting: ")
a = input("enter the char to check: ")
if a in y:
    print("char exists")
else:
    print("not exists")

lst = input("Enter elements: ").split()
lst = list(map(int, lst))
count = 0
for i in lst:
    count = count + i
print(count)
print(count/len(lst))
    
ls = input("Enter the elements: ").split()
print(ls)
ls = list(map(int,ls))
print(ls)
count = 1
for i in ls:
    count = count*i
print(count)

l = list(map(int, input("Enter numbers: ").split()))

for i in l:
    if i % 2 == 0:
        print(i, end=" ")
        
d = list(map(int, input("Enter numbers: ").split()))

for i in d:
    if i % 2 != 0:
        print(i, end=" ")
        
z = list(map(int, input("Enter numbers: ").split()))

for i in z:
    if i > 0:
        print(i, end=" ")

p= list(map(int, input("Enter numbers: ").split()))

for i in p:
    if i < 0:
        print(i, end=" ")




