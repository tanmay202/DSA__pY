# Binary Search
arr = [2, 3, 4, 5, 6, 7, 9]
l = 0
r = len(arr) - 1
k = 6
while l <= r:
    mid = (l + r) // 2

    if k == arr[mid]:
        print("Found:", mid)
        break

    elif k < arr[mid]:
        r = mid - 1

    else:
        l = mid + 1

# Complexity
# Time: O(log n) ✅ optimal
# Space: O(1) ✅ optimal

#<============Recursive approach =============>
def Binary_Recursive(arr,l,r,k):
    if l>r:
        return -1 #Base case
    mid=(l+r)//2
    if arr[mid]==k:
        return mid
    elif k<arr[mid]:
        return Binary_Recursive(arr,l,mid-1,k)
    else:
        return Binary_Recursive(arr,mid+1,r,k)

print("Recursive approach:",Binary_Recursive(arr,0,len(arr),6))


# Recursive Binary Search Complexity
# Time Complexity:  O(log n)
# Space Complexity: O(log n)

# Why?

# Suppose the array has 16 elements:

# 16 → 8 → 4 → 2 → 1

# That's about log₂(16) = 4 recursive calls.

# Each recursive call stays on the call stack until the answer is returned.

# Your two approaches
# Approach	Time	Space
# Iterative	O(log n)	O(1)
# Recursive	O(log n)	O(log n)

# So iterative is more space-efficient.