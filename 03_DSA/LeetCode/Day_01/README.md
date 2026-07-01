# 🚀 Day 001 - Two Sum

## 📌 Problem

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to the target.

- Each input has exactly one solution.
- The same element cannot be used twice.
- The answer can be returned in any order.

### Example

```text
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9
```

---

# 🧠 Approach 1 — Brute Force

## Idea

Compare every element with every other element until the target sum is found.

### Algorithm

1. Traverse the array.
2. For each element, compare it with every remaining element.
3. If the sum equals the target, return both indices.

---

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n²)** |
| Space Complexity | **O(1)** |

### Why?

- Two nested loops.
- Every pair is checked.
- No extra memory is used.

---

# ⚡ Approach 2 — HashMap (Optimized)

## Idea

Instead of checking every pair, calculate the number needed to reach the target.

```text
Needed Number = Target - Current Number
```

Store every visited number inside a HashMap.

If the needed number already exists, return its index.

---

## Dry Run

```text
nums = [2,7,11,15]

Target = 9
```

| Current Number | Needed | HashMap | Action |
|---------------|--------|---------|--------|
|2|7|{}|Store 2|
|7|2|{2:0}|Found ✓ Return [0,1]|

---

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
```

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

### Why?

- We traverse the array only once.
- Dictionary lookup takes approximately **O(1)** time.
- Extra memory is used to store visited elements.

---

# 📊 Comparison

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n²) | O(1) |
| HashMap | O(n) | O(n) |

---

# 📚 Key Concepts Learned

- Nested Loops
- Time Complexity
- Space Complexity
- HashMap (Dictionary)
- Complement Technique
- Python `enumerate()`
- Dictionary Lookup

---

# 💡 Interview Takeaways

- Always think of the brute-force solution first.
- Analyze its complexity.
- Try to reduce unnecessary comparisons.
- HashMaps are commonly used to optimize searching problems.
- Explain your thought process before writing code.

---

# 🎯 What I Learned

- Learned how to solve the Two Sum problem using two different approaches.
- Understood why the HashMap approach is much faster than brute force.
- Practiced using Python dictionaries for efficient lookups.
- Improved my understanding of time and space complexity.

---

## 🏷️ Tags

`Array` `HashMap` `Python` `LeetCode` `Easy` `DSA`

---

### Status

✅ Problem Solved

**LeetCode Problem #1 Completed 🎉**