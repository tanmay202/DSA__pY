arr=[1,1,2,2,3,4,5,5,5,5,6,6,7]
x=5
for i in range(len(arr)):
    if arr[i]==5:
        print("First occurence=>Index:",i)
        break
l=-1
for i in range(len(arr)):    
    if arr[i]==5:
        l=i
print("Last occurence=>",l)        

# | Complexity           | Your Code |
# | -------------------- | --------- |
# | **Time Complexity**  | **O(n)**  |
# | **Space Complexity** | **O(1)**  |

#<======Optimised=========>

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
        r = mid - 1       # search left
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
        l = mid + 1       # search right
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1

print("First occurrence =>", first)
print("Last occurrence =>", last)

# Time: O(log n) + O(log n) = O(log n)
# Space: O(1)