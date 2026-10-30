nested_tuple = (1, (2, 3), (4, (5, 6)), 7)

stack = [nested_tuple]
flat_list = []

while stack:
    item = stack.pop()
    if isinstance(item, tuple):
        for x in reversed(item):
            stack.append(x)
    else:
        flat_list.append(item)

flat_tuple = tuple(flat_list)
print(flat_tuple)
print(type(flat_tuple))