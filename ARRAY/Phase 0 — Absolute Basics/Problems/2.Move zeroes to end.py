arr=[0,0,1,2,3,4,5]

#=========bruteForce Approach:===============
# First traverse the array and put all non-zero elements into ans.
# Traverse the array again and put all zeroes into ans.
# Return ans.

def bruteForce(arr):
    ans=[]
    for i in arr:       # O(n)
        if i!=0:
            ans.append(i)
    for i in arr:       # O(n)
        if i==0:
            ans.append(i)
    return ans
# Total TC=O(n) + O(n) = O(n)

print(bruteForce(arr))

# solution is not very slow in terms of time. The main problem is the extra memory.
# traversing the array twice

# ==========Optimization idea==========
# We can solve it in-place, meaning we modify the original array instead of creating ans.

# Keep a pointer j representing the position where the next non-zero element should go.
# Traverse the array with i.
# Whenever arr[i] != 0, swap it with arr[j].
# Increment j.

def moveZeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
print("Optimized:",moveZeros(arr))

# Brute force:  O(n) time, O(n) space
# Optimized:    O(n) time, O(1) space