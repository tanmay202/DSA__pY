arr=[1,2,3,4,5,6,7,8,9,0]
k=3

def RotateLeft(arr):
    return arr[1:] + [arr[0]]

def RotateRight(arr):
    return [arr[-1]] + arr[:-1]

def RotateRightK(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

print("Left rotate array by 1:",RotateLeft(arr))
print("Right rotate array by 1:",RotateRight(arr))
print("Right rotate array by k:",RotateRightK(arr,k))

# TC = O(n)
# SC = O(1)

# =========Pattern to memorize==============
# LEFT K:
# arr[k:] + arr[:k]

# RIGHT K:
# arr[-k:] + arr[:-k]

# And always use:

# k = k % len(arr)

# because if k > len(arr), rotating by k is equivalent to rotating by k % n.