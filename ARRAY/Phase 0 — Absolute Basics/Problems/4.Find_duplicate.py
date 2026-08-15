arr=[2,3,4,4,2,1]

def Brute(arr):
    duplicates = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])

    return duplicates

print(Brute(arr))

# =======Why brute force is slow===========
# There are two nested loops.
# For every element, you potentially compare it with many other elements.
# If n = 1,000,000, the number of comparisons can become enormous.
# Also, this part:
# arr[i] not in duplicates is itself a linear search through duplicates.
# So brute force becomes inefficient for large arrays.


# =====Optimization idea=====
# Use a set to remember elements we've already seen.
# Idea
# Maintain:
# seen = set()
# duplicates = set()
# For every element:
# If it's already in seen → it's a duplicate.
# Otherwise → add it to seen.

def optimized(arr):
    seen = set()
    duplicates = set()

    for x in arr:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)
print(optimized(arr))

# | Approach    | Pattern      |           Time |  Space |
# | ----------- | ------------ | -------------: | -----: |
# | Brute Force | Nested loops |        `O(n²)` | `O(n)` |
# | Hash Set    | Hashing      | `O(n)` average | `O(n)` |
