# 📚 Build Array from Permutation (LeetCode #1920)

## 🟢 Difficulty

Easy

---

# Pattern

✅ Array

---

# 📖 Problem Statement

Given a zero-based permutation array `nums`, build a new array `ans` such that:

```text
ans[i] = nums[nums[i]]
```

Return the resulting array.

---

# Example

## Input

```text
nums = [0,2,1,5,3,4]
```

## Output

```text
[0,1,2,4,5,3]
```

---

# 🥉 Brute Force Approach

## Idea

Create a new array.

For every index:

- Find `nums[i]`
- Use that value as an index again.
- Store the result in the answer array.

---

## Code

```python
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
```

---

# 🧠 Dry Run

Input

```text
nums = [0,2,1,5,3,4]
```

```
i = 0

nums[nums[0]]

↓

nums[0]

↓

0
```

```
i = 1

nums[nums[1]]

↓

nums[2]

↓

1
```

Continue for every index.

Final Answer

```text
[0,1,2,4,5,3]
```

---

# 🏆 Optimal Approach

Python List Comprehension

```python
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
```

---

# 📊 Complexity

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

# 🌍 Real-World Applications

- Index Mapping
- Data Rearrangement
- Lookup Tables
- Permutation Problems

---

# 🧠 Interview Questions

## What pattern does this problem use?

Array Traversal.

---

## Why is the time complexity O(n)?

Because each element is processed exactly once.

---

## Why is extra space required?

A new array is created to store the result.

---

# 📁 Folder Structure

```text
Day_13/

├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 🎯 Key Takeaways

- Learned how to access nested indices.
- Practiced array traversal.
- Used list comprehension for a concise solution.
- Reinforced the concept of index-based mapping.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, understand the underlying pattern, compare brute-force and optimal solutions, and document everything on GitHub.

**Learn • Practice • Build • Repeat** 🚀