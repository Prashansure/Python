def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 1
    for i in stuff:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5, 6))

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Bro", middle="Dude", last="Code")

name = "Prashan"
sur_name = "Sure"

print("Hello, my name is {}".format(name))
print("Hello, my name is {}. Nice to meet you".format(sur_name + name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))