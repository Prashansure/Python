arr = list(map(int, input().split()))
target = int(input())
def search(arr,target,index):
    if arr[index] == target:
        return index
    if index >= len(arr):
        return -1
    return search(arr,target,index +1)
print(search(arr, target, 0))