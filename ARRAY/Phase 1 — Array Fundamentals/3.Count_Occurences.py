arr = [1,1,2,2,3,4,5,5,5,5,6,6,7]
x = 5

# First occurrence
l = 0
r = len(arr) - 1
first = -1

while l <= r:
    mid = (l + r) // 2

    if arr[mid] == x:
        first = mid
        r = mid - 1

    elif arr[mid] < x:
        l = mid + 1

    else:
        r = mid - 1


# Last occurrence
l = 0
r = len(arr) - 1
last = -1

while l <= r:

    mid = (l + r) // 2

    if arr[mid] == x:
        last = mid
        l = mid + 1

    elif arr[mid] < x:
        l = mid + 1

    else:
        r = mid - 1


# Count
if first == -1:
    print(0)
else:
    print(last - first + 1)