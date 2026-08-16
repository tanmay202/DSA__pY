arr=[1,2,4,5]
n=5
for i in range(n+1):
    if i not in arr:
        print(i)

# =====Why brute force is slow=====
# x in arr takes O(n) in a Python list.
# We're doing it up to n + 1 times.
# Therefore:
# O(n²) time.
# Optimization idea
# Use the mathematical sum:
# Expected sum = n × (n + 1) / 2
# Then:
# Missing = Expected sum - Actual sum

def find_missing(arr):
    size = len(arr)

    expected = size * (size + 1) // 2
    actual = sum(arr)

    return expected - actual
ar = [3, 0, 1]
print(find_missing(ar))  # 2

# 5. Time complexity
# sum(arr) → O(n)
# Overall → O(n)
# 6. Space complexity

# O(1) extra space.