arr = [2, 3, 4, 5, 6, 3, 2, 1, 3, 5, 6, 4]


# ========== Brute Force Approach ==========

def Brute(arr):
    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        print(arr[i], count)


Brute(arr)


# ========== Why Brute Force is Slow ==========

# Suppose there are n elements.
#
# For every element, we're scanning the entire array:
#
# 1st element → n comparisons
# 2nd element → n comparisons
# 3rd element → n comparisons
# ...
# nth element → n comparisons
#
# Therefore:
#
# n × n = n²
#
# Time Complexity = O(n²)
#
# For a large array, this becomes expensive.
#
# Example:
#
# n = 10,000
#
# n² = 100,000,000 comparisons


# ========== Optimization Idea ==========

# Instead of repeatedly searching the array,
# store the frequency while traversing the array once.
#
# Use a Python dictionary.
#
# Dictionary:
#     key   → element
#     value → frequency


def FindFreq(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


print("Optimized:", FindFreq(arr))


# ========== Complexity ==========

# Brute Force:
# Time Complexity  = O(n²)
# Space Complexity = O(1)
#
# Optimized:
# Time Complexity  = O(n) average
# Space Complexity = O(k)
#
# k = number of unique elements