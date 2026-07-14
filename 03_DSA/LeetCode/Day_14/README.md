# 📚 Palindrome Number (LeetCode #9)

## 🟢 Difficulty

Easy

---

# Pattern

✅ Math

---

# 📖 Problem Statement

Given an integer `x`, return `true` if the integer is a palindrome, otherwise return `false`.

A palindrome reads the same from left to right and right to left.

---

# Example 1

Input

```text
121
```

Output

```text
true
```

---

# Example 2

Input

```text
-121
```

Output

```text
false
```

---

# Example 3

Input

```text
10
```

Output

```text
false
```

---

# 🥉 Brute Force Approach

## Idea

Convert the number into a string.

Reverse the string.

Compare both strings.

---

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        original = str(x)
        reverse = original[::-1]

        return original == reverse
```

---

# Complexity

### Time

```
O(n)
```

### Space

```
O(n)
```

---

# 🏆 Optimal Approach

## Idea

Reverse the integer mathematically.

No string conversion.

Steps:

- Extract the last digit using `% 10`.
- Build the reversed number.
- Remove the last digit using `// 10`.
- Compare the reversed number with the original.

---

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:

            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse
```

---

# Dry Run

Input

```
121
```

Iteration 1

```
digit = 1

reverse = 1

x = 12
```

Iteration 2

```
digit = 2

reverse = 12

x = 1
```

Iteration 3

```
digit = 1

reverse = 121

x = 0
```

Compare

```
121 == 121

True
```

---

# 📊 Complexity

| Approach | Time | Space |
|----------|------|------:|
| Brute Force | O(n) | O(n) |
| Optimal | O(log n) | O(1) |

---

# 🌍 Real-World Applications

- Number Validation
- Security PIN Verification
- Pattern Recognition
- Mathematical Algorithms

---

# 🧠 Interview Questions

## Why are negative numbers never palindromes?

Because the minus sign appears only at the beginning.

Example:

```
-121

121-
```

They are different.

---

## Why is the optimal solution better?

Because it avoids converting the number into a string and uses constant extra space.

---

## Which operator extracts the last digit?

```python
digit = x % 10
```

---

## Which operator removes the last digit?

```python
x //= 10
```

---

# 📁 Folder Structure

```text
Day_14/

├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 🎯 Key Takeaways

- A palindrome reads the same forward and backward.
- Numbers can be reversed mathematically without converting to strings.
- `%` extracts the last digit.
- `//` removes the last digit.
- Mathematical solutions are generally preferred in interviews.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, understand the underlying pattern, compare brute-force and optimal solutions, and document each solution with explanations and complexity analysis.

**Learn • Practice •Build • Repeat** 🚀