def student(names):
    t = []
    for i in names:
        if i[0].lower() in 'aeiou':
            t.append(i)
    return t
name = list(input().split(","))
print(student(name))