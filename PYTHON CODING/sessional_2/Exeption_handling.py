try:
    n =int(input())
    m =int(input())
    result = (n/m)
except ValueError as e:
    print(e)
    print("You dumb give numbers not string!!")
except ZeroDivisionError:
    print("you need to learn mathamatics")
except Exception:
    print("You did somthing dumb!!")
else:
    print(result)
finally:
    print("This will always Exicute")
    