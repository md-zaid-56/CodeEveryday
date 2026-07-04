# 🔍 Contains Duplicate (LeetCode #217)

## 🟢 Difficulty
Easy

---

# 📖 Problem Statement

Given an integer array `nums`, determine whether any value appears **at least twice**.

Return:

- `true` → If any element appears more than once.
- `false` → If all elements are unique.

---

## Example 1

### Input

```text
nums = [1,2,3,1]
```

### Output

```text
true
```

### Explanation

The number **1** appears twice.

---

## Example 2

### Input

```text
nums = [1,2,3,4]
```

### Output

```text
false
```

### Explanation

Every element is unique.

---

## Example 3

### Input

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

### Output

```text
true
```

---

# 🧠 Approach 1 : Brute Force

## Idea

Compare every element with every other element after it.

If two elements are equal, a duplicate exists.

---

## Algorithm

1. Traverse the array.
2. For every element, compare it with all remaining elements.
3. If a duplicate is found, return `True`.
4. If no duplicates are found, return `False`.

---

## Brute Force Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
```

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

---

# 🚀 Approach 2 : Hash Set (Optimal)

## Idea

Instead of comparing every element with all previous elements, store every visited element inside a **Hash Set**.

For each number:

- If it already exists in the set → Duplicate found.
- Otherwise, insert it into the set.

Since searching inside a Hash Set takes approximately **O(1)** time, the entire algorithm becomes **O(n)**.

---

## Algorithm

1. Create an empty Hash Set.
2. Traverse the array.
3. If the current element already exists in the set:
   - Return `True`.
4. Otherwise:
   - Insert the element into the set.
5. If the loop finishes, return `False`.

---

# 💻 Optimal Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)

        return False
```

---

# 🖥 Dry Run

Input

```text
nums = [1,2,3,1]
```

| Current Number | Hash Set | Duplicate Found? |
|---------------:|----------|------------------|
| 1 | {1} | ❌ |
| 2 | {1,2} | ❌ |
| 3 | {1,2,3} | ❌ |
| 1 | {1,2,3} | ✅ Yes |

Return

```text
True
```

---

# 🔍 Why Hash Set?

A Hash Set stores **only unique values**.

Before inserting a new value, checking whether it already exists takes approximately **O(1)** time.

This makes it much faster than searching through a list.

---

# 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|-----------------|
| Brute Force | O(n²) | O(1) |
| Hash Set | O(n) | O(n) |

---

# 💡 Key Concepts Learned

- Arrays
- Hash Set
- Duplicate Detection
- Optimization
- Time Complexity
- Space Complexity
- Interview Problem Solving

---

# 📁 Folder Structure

```text
Contains_Duplicate/
│
├── brute_force.py
├── optimal.py
└── README.md
```

---

# 🎯 Interview Takeaway

The brute-force solution compares every pair of elements, resulting in **O(n²)** time complexity.

The optimal solution uses a **Hash Set** to remember previously seen elements. Since searching and inserting into a Hash Set are approximately **O(1)** operations, the overall time complexity improves to **O(n)**.

This is one of the most common interview patterns and forms the foundation for solving many advanced Hash Table problems.

---

# 🚀 Part of my **#CodeEveryday – Basics to Advance Challenge**

Learning one concept, one problem, and one commit every single day.