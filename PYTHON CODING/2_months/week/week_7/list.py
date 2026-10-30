
# find the elements occurring more than once (duplicates)
# remove duplicates while preserving order
# find the second largest element in the list
# rotate list by k positions 
# find intersection of two lists
# flatten a nested list
# find the pair that sum the target()
# merge two sorted list
# find the most frequent element


lst = [1, 2, 3, 2, 4, 1, 5]
duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

lst = [1, 2, 3, 2, 4, 1, 5]
result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)



lst = [10, 20, 4, 45, 99, 99]

largest = max(lst)
second_largest = None

for i in lst:
    if i != largest:
        if second_largest is None or i > second_largest:
            second_largest = i

print(second_largest)



lst = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)




lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

intersection = []

for i in lst1:
    if i in lst2 and i not in intersection:
        intersection.append(i)

print(intersection)




lst = [1, 2, [3, 4], [5, 6], 7]
flat_list = []

for i in lst:
    if type(i) == list:
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)

print(flat_list)



lst = [2, 4, 3, 7, 8]
target = 10

pairs = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))

print(pairs)



lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]

merged = []
i = j = 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

merged.extend(lst1[i:])
merged.extend(lst2[j:])

print(merged)



lst = [1, 3, 2, 1, 4, 1, 3]
most_freq = lst[0]
max_count = 0

for i in lst:
    count = lst.count(i)
    if count > max_count:
        max_count = count
        most_freq = i

print(most_freq)
