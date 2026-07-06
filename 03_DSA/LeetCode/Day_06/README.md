# 🔀 Merge Sorted Array (LeetCode #88)

## 🟢 Difficulty

Easy

---

# 📖 Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of valid elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array.

The final sorted array should be stored inside `nums1`. Do **not** return anything; modify `nums1` in-place.

---

## Example 1

### Input

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

### Output

```text
[1,2,2,3,5,6]
```

---

## Example 2

### Input

```text
nums1 = [1]
m = 1

nums2 = []
n = 0
```

### Output

```text
[1]
```

---

## Example 3

### Input

```text
nums1 = [0]
m = 0

nums2 = [1]
n = 1
```

### Output

```text
[1]
```

---

# 🧠 Approach 1 : Brute Force

## Idea

1. Copy all elements of `nums2` into the empty positions of `nums1`.
2. Sort the entire `nums1` array.

This is the easiest approach but not the most efficient.

---

## Brute Force Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()
```

---

## Dry Run

Initial

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

After Copying

```text
[1,2,3,2,5,6]
```

After Sorting

```text
[1,2,2,3,5,6]
```

---

## Complexity Analysis

### Time Complexity

```text
O((m+n) log(m+n))
```

### Space Complexity

```text
O(1)
```

---

# 🚀 Approach 2 : Optimal (Two Pointers)

## Idea

Instead of merging from the beginning, merge from the **end** of both arrays.

Why?

Because the last `n` positions of `nums1` are empty, allowing us to place larger elements without overwriting useful data.

---

## Algorithm

1. Place one pointer at the last valid element of `nums1`.
2. Place another pointer at the last element of `nums2`.
3. Place a third pointer at the end of `nums1`.
4. Compare the two elements.
5. Place the larger element at the end.
6. Move the corresponding pointer.
7. Repeat until one array is exhausted.
8. Copy any remaining elements from `nums2`.

---

## Optimal Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

# 🖥 Dry Run

Input

```text
nums1 = [1,2,3,0,0,0]

nums2 = [2,5,6]
```

Pointers

```text
i = 2 → 3
j = 2 → 6
k = 5
```

Compare

```text
3 < 6

↓

Place 6

[1,2,3,0,0,6]
```

Next

```text
3 < 5

↓

Place 5

[1,2,3,0,5,6]
```

Next

```text
3 > 2

↓

Place 3

[1,2,3,3,5,6]
```

Continue

↓

Final Array

```text
[1,2,2,3,5,6]
```

---

# 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|-----------------|
| Brute Force | O((m+n) log(m+n)) | O(1) |
| Two Pointers | O(m+n) | O(1) |

---

# 💡 Why Do We Only Copy Remaining Elements from `nums2`?

Suppose

```text
nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
```

After placing `6`, `5`, and `4`, the remaining elements in `nums1`

```text
1 2 3
```

are already in the correct position.

Therefore, only the remaining elements of `nums2` need to be copied.

---

# 🧠 Key Concepts Learned

- Two Pointer Technique
- In-place Array Modification
- Backward Traversal
- Array Manipulation
- Sorting vs Merging
- Time Complexity Optimization

---

# 🎯 Interview Questions

### Why do we merge from the end instead of the beginning?

Because merging from the front would overwrite valid elements in `nums1`.

---

### Why don't we need another loop for the remaining elements of `nums1`?

Any remaining elements of `nums1` are already in their correct positions.

---

### What is the time complexity of the optimal solution?

```text
O(m+n)
```

---

### What is the space complexity?

```text
O(1)
```

---

# 📁 Folder Structure

```text
Merge_Sorted_Array/
│
├── brute.py
├── optimal.py
└── README.md
```

---

# 🚀 Part of my **#CodeEveryday – Basics to Advance Challenge**

Learning one algorithm, one programming concept, and one GitHub commit every single day.

Current Patterns Learned:

- ✅ Hash Map
- ✅ Stack
- ✅ Greedy
- ✅ Hash Set
- ✅ Two Pointers
- ✅ In-place Array Manipulation