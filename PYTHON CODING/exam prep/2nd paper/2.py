branch_a = {"Alice": 50000, "Bob": 45000, "Charlie": 55000}
branch_b = {"Bob": 48000, "David": 40000, "Alice": 52000}

result = {}

# Add all from branch_a first
for name in branch_a:
    result[name] = branch_a[name]

# Merge branch_b
for name in branch_b:
    if name in result:
        result[name] = max(result[name], branch_b[name])
    else:
        result[name] = branch_b[name]

print(result)