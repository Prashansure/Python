# Useful Python Dunder (Double Underscore) Attributes & Methods
# Learn these gradually. Don't try to memorize everything at once.


# __name__
# Gives the name of a function

def greet():
    pass

print(greet.__name__)      # greet


# __doc__
# Gives the documentation string

def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__doc__)         # Adds two numbers


# __class__
# Gives the type/class of an object

x = 10
print(x.__class__)         # <class 'int'>


# __dict__
# Shows all attributes stored in an object

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 20

p = Person("Prashan")

print(p.__dict__)          # {'name': 'Prashan', 'age': 20}


# __init__
# Constructor
# Runs automatically when an object is created

class Student:
    def __init__(self, name):
        self.name = name
        print("Student Created")

s = Student("Ram")


# __str__
# Controls what print(object) displays

class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee({self.name})"

e = Employee("Krishna")

print(e)                   # Employee(Krishna)


# __len__
# Controls len(object)

class Team:
    def __len__(self):
        return 11

team = Team()

print(len(team))           # 11


# __repr__
# Official string representation
# Mainly used for debugging

class Book:
    def __repr__(self):
        return "Book()"

b = Book()

print(b)                   # Book()


# __call__
# Makes an object behave like a function

class Hello:
    def __call__(self):
        print("Object called like a function")

h = Hello()

h()                        # Object called like a function


# __contains__
# Controls the 'in' operator

class Numbers:
    def __contains__(self, item):
        return item in [1, 2, 3]

nums = Numbers()

print(2 in nums)           # True


# __getitem__
# Controls indexing []

class Letters:
    def __getitem__(self, index):
        return ['a', 'b', 'c'][index]

letters = Letters()

print(letters[1])          # b


# __iter__
# Makes objects iterable in loops

class Counter:
    def __iter__(self):
        return iter([1, 2, 3])

for i in Counter():
    print(i)


# Most Important For You Right Now:
#
# __name__   -> Function name
# __doc__    -> Documentation
# __class__  -> Object type
# __dict__   -> Object attributes
# __init__   -> Constructor
# __str__    -> Print representation
#
# Learn these first.
# The rest will make sense naturally when you study OOP.