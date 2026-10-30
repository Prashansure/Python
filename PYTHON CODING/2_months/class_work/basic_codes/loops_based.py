#palindrome 
a = int(input("enetr the number you want to check: "))
temp = a
rev = 0
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10
    
if rev == temp:  
    print("the number is palindorme")
else:
    print("the number is not a palindrome")

#fabonacci
n = int(input("Enter how many terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    

    