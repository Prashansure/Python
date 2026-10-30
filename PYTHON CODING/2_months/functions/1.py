#normal function
def addition(a,b):
    print(a+b)
addition(9,1)
print()

#default arguments
def addition1(a = 1,b = 2):
    print(a+b)
addition1()
addition1(3,2)
addition1(a = 357)
print()

# keyword argument
def substraction(a = 10,b = 1):
    print(a-b)
substraction()
substraction(12,3)
substraction(b = 5)
substraction(b = 123,a = 125)

# variable length
