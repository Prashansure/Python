fiction = set(input().split(","))
science = set(input().split(","))
c = fiction & science
print(*sorted(c))
print(fiction - science)