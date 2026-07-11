# 📚 Concatenation of Array (LeetCode #1929)

## 🟢 Difficulty

Easy

---

# 📖 Problem Statement

Given an integer array `nums` of length `n`, return an array `ans` of length `2n` where:

```text
ans[i] = nums[i]
ans[i + n] = nums[i]
```

In simple words,

Return a new array that contains the original array **twice**.

---

# Example 1

## Input

```text
nums = [1,2,1]
```

## Output

```text
[1,2,1,1,2,1]
```

---

# Example 2

## Input

```text
nums = [1,3,2,1]
```

## Output

```text
[1,3,2,1,1,3,2,1]
```

---

# 🥉 Approach 1 : Brute Force

## Idea

Create a new list.

Traverse the original array twice.

- First traversal copies the original array.
- Second traversal appends the same elements again.

---

## Code

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        for num in nums:
            ans.append(num)

        for num in nums:
            ans.append(num)

        return ans
```

---

## Dry Run

Input

```text
nums = [1,2,1]
```

Initially

```text
ans = []
```

After first loop

```text
ans = [1,2,1]
```

After second loop

```text
ans = [1,2,1,1,2,1]
```

Return

```text
[1,2,1,1,2,1]
```

---

## Complexity

### Time Complexity

```text
O(n)
```

---

### Space Complexity

```text
O(n)
```

---

# 🏆 Optimal Approach

Python provides a very concise solution.

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

---

## Complexity

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

# 📊 Comparison

| Approach | Time | Space |
|----------|------|------:|
| Brute Force | O(n) | O(n) |
| Python Concatenation | O(n) | O(n) |

---

# 🌍 Real-World Applications

- Playlist Duplication
- Data Replication
- Image Processing
- Simulation Systems
- Repeating Test Data

---

# 🧠 Interview Questions

## What does this problem test?

Basic array traversal and array manipulation.

---

## Why is the complexity O(n)?

Because every element is copied exactly twice.

---

## Is `nums + nums` an in-place operation?

No.

It creates a new list.

---

# 📁 Folder Structure

```text
Day_11/

├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 📚 Pattern Learned

✅ Array Traversal

---

# 🎯 Key Takeaways

- Arrays can be traversed multiple times.
- Python allows list concatenation using the `+` operator.
- Both solutions require linear time.
- This problem is a good introduction to array manipulation.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, understand the underlying pattern, compare brute-force and optimal solutions, and document each solution with explanations and complexity analysis.

**Learn • Practice • Build • Repeat** 🚀