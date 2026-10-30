#function arguments
"""
Default function
Keyword function
variable function
required arguments
"""
def avg(a=4,b=8):
    print("the avg is ", (a+b)/2)
    
def name(fname,mname = "jhon",lname = "prashan"):
    print("Hello,",fname,mname,lname)


#-------------------------------------------------    
#Default function
avg(2,3)
avg(a = 4,b = 4)
avg()

name("hero","prashan",)
name("good")
#-------------------------------------------------  
#Keyword function
avg(b = 9)
avg(b = 9,a = 3)
#-------------------------------------------------  
#required arguments
# name()give error cuz we not given value for fname
name("z")
#-------------------------------------------------  
#variable length argyments
#are 2 types
#arbitary
#key word 
#-------------------------------------------------  
#arbitary
def avg1(*num):
    sum = 0
    print(type(num))
    for i in num:
        sum = sum + i
    print("average is : ",sum/len(num))
        
avg1(1,2,3,4,5,7,88,2)
#-------------------------------------------------  
#key word
def avg2(**numb):
    print(type(numb))
    total = 0
    for i in numb.values():   # use values()
        total += i
    print("average is:", total / len(numb))

avg2(a=35, b=7, c=53, d=5, e=6)
#-------------------------------------------------
def avg3(a=4,b=8):
   return (a+b)/2
c = avg3()
print(c)
