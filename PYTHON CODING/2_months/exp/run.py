from code import add 

print("Type: fib(number)")
print("Type: exit to quit")

while True:
    try:
        cmd = input("> ")
        if cmd == "exit":
            break
        print(eval(cmd))
    except Exception as e:
        print("Error:", e)
