# A function that adds extra behavior to another function without changing its code.
# First-Class Function → functions are values
# Closure → function + memory
# Decorator → function that modifies another function

#Basic one
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)

decorated_display()


#classic method 
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


display()