"""
First-Class Functions:
A programming language is said to have first-class functions if it treats
functions as first-class citizens. 

First-Class Citizen (Programming):
A first-class citizen (sometimes called first-class objects) in a programming
language is an entity which supports all the operations generally available
to other entities. These operations typically include being passed as an
argument, returned from a function, and assigned to a variable.
"""
def square(x):
    return x * x

def my_map(func, lst):
    result = []
    for i in lst:
        result.append(func(i))
    return result

lst = list(map(int, input("Enter numbers: ").split()))

squares = my_map(square, lst)

print(squares) 



def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')