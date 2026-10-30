# Creating sets
set1 = {'aa', 'bb', 'cc', 'dd'}
set2 = set(('aaa', 'bbb', 'ccc', 'ddd'))

print("set1:", set1)
print("set2:", set2)

# Sets are unordered, unindexed, and do not allow duplicates
# Set items are unchangeable, but we can add/remove elements

# Different types of elements in sets
lang = {'C', 'C++', 'Java', 'Python', 'Perl'}
print("Languages:", lang)

s1 = {1, 2, 3, 4}
print("Integers set:", s1)

s2 = {2.2, 3.4, 4.5}
print("Float set:", s2)

s3 = {1, 2.3, 'abc'}
print("Mixed set:", s3)

s4 = {True, False, False}
print("Boolean set (duplicates ignored):", s4)

# Duplicate elements are ignored
lang_dup = {'C', 'C++', 'Java', 'Python', 'Perl', 'Java'}
print("Languages with duplicate:", lang_dup)

# Datatype of set
print("Type of lang:", type(lang))

# Accessing elements (unordered)
print("Accessing elements of set:")
for i in lang:
    print(i)

# Length of set
print("Length of lang:", len(lang))

# Membership operators
print("'C++' in lang:", 'C++' in lang)
print("'Ruby' in lang:", 'Ruby' in lang)
print("'C' not in lang:", 'C' not in lang)
print("'C#' not in lang:", 'C#' not in lang)

# Other built-in functions
nums = {1, 2, 3, 4, 5}
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted:", sorted(nums))

# Copying a set
s_copy = nums.copy()
print("Copied set:", s_copy)

# Adding elements
s = {1, 2, 3.5, 'psp'}
s.add(90)
print("After add():", s)

# Update with another set
s.update({12, 45})
print("After update with set:", s)

# Update with list
s.update([11, 22])
print("After update with list:", s)

# Update with another set
s1 = {11, 22, 33, 44}
s.update(s1)
print("After update with another set:", s)

# Update with any iterable
set1 = {"apple", "banana", "cherry"}
l1 = ["kiwi", "orange"]
set1.update(l1)
print("After updating set with list:", set1)

# Removing elements
s1 = {1, 2, 3, 11, 22, 'psp', 'a'}
s1.remove(3)
print("After remove(3):", s1)

# discard() does not give error if element not present
s1.discard(2)
print("After discard(2):", s1)

s1.discard(21)  # no error
print("After discard(21):", s1)

# pop() removes random element
set_pop = {'apple', 'orange', 'cherry', 'banana'}
print("Before pop:", set_pop)
print("Popped element:", set_pop.pop())
print("After pop:", set_pop)

# =========================
# Set Operations
# =========================

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Union
s3 = s1.union(s2)
s4 = s1 | s2
print("Union (method):", s3)
print("Union (operator):", s4)

# Intersection
s5 = s1.intersection(s2)
s6 = s1 & s2
print("Intersection (method):", s5)
print("Intersection (operator):", s6)

# Intersection update
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print("Intersection update result:", s1_copy)

# Difference
s7 = s1.difference(s2)
s8 = s1 - s2
print("Difference (method):", s7)
print("Difference (operator):", s8)

# Symmetric difference
s9 = s1.symmetric_difference(s2)
s10 = s1 ^ s2
print("Symmetric difference (method):", s9)
print("Symmetric difference (operator):", s10)

# =========================
# Set Comparisons
# =========================

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}

print("s1 is superset of s2:", s1 > s2)
print("s2 is subset of s1:", s2 < s1)

s5 = {1, 2, 3, 4, 5}
print("s1 == s5:", s1 == s5)