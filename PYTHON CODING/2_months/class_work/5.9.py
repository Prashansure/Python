print("solving the quadratic equation ax^2 + bx + c = 0")
a = int(input("enter coeff of x^2: "))
b = int(input("enter coeff of x: "))
c = int(input("enter constant term: "))
d = (b**2) - (4*a*c)
if d==0:
    print("the roots are real and same")
elif d>0:
    print("the roots are real and different")
else:
    print("the roots are complex and different")

if d>0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("root1: ",root1)
    print("root2: ",root2)
elif d==0:
    root1 = root2 = -b / (2*a)  
    print("root1: ",root1)
else:
    realPart = -b / (2*a)
    imagPart = (-d**0.5) / (2*a)
    print("root1: ",realPart ,"+", imagPart ,"i")
    print("root2: ",realPart ,"-", imagPart ,"i")
