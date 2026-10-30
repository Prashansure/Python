# module file (utils.py)
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def palindrome(s):
    return s == s[::-1]