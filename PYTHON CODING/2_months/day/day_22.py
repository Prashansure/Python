#python lists
marks = [3,True,"prashan"]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-1])
#print(marks[3])   IndexError: list index out of range
if 3 in marks:
    print('yes')
else:
    print("no")
    
if "3" in marks:
    print('yes')
else:
    print("no")

if "pr" in marks:
    print('yes')
else:
    print("no")
    
if "pra" in "prashan":
    print('yes')
else:
    print("no")
    
print(marks)
print(marks[:])
print(marks[0:3])
#------------------------------------
#list comprehension
list = [ i**i for  i in range(12)]
print(list)
