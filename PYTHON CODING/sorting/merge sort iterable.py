def merge_sort_iterative(arr):
    n = len(arr)
    size = 1

    while size < n:
        left = 0

        while left < n:
            mid = min(left + size, n)
            right = min(left + 2*size, n)

            merged = []
            i = left
            j = mid

            while i < mid and j < right:
                if arr[i] < arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1

            merged += arr[i:mid]
            merged += arr[j:right]

            arr[left:right] = merged

            left += 2 * size

        size *= 2

    return arr


arr = [8,3,5,2,9,1]
print(merge_sort_iterative(arr))