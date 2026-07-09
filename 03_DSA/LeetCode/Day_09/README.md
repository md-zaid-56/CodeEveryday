# 🔗 Is Subsequence (LeetCode #392)

## 🟢 Difficulty

Easy

---

# 📖 Problem Statement

Given two strings `s` and `t`, return **True** if `s` is a **subsequence** of `t`.

A subsequence is formed by deleting zero or more characters from another string **without changing the order of the remaining characters**.

Otherwise, return **False**.

---

# Examples

## Example 1

### Input

```text
s = "abc"
t = "ahbgdc"
```

### Output

```text
True
```

Explanation

```
t = a h b g d c
    ↑   ↑     ↑

a → b → c
```

All characters appear in the correct order.

---

## Example 2

### Input

```text
s = "axc"
t = "ahbgdc"
```

### Output

```text
False
```

Explanation

Character **x** does not exist in `t`.

---

## Example 3

### Input

```text
s = ""
t = "abc"
```

### Output

```text
True
```

An empty string is always a subsequence.

---

# 🥉 Approach 1 : Brute Force

## Idea

- Start from the beginning of `t`.
- Search for each character of `s`.
- If a character is found, continue searching from the next position.
- If any character cannot be found, return `False`.

---

## Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        index = 0

        for char in s:

            while index < len(t) and t[index] != char:
                index += 1

            if index == len(t):
                return False

            index += 1

        return True
```

---

## Dry Run

Input

```text
s = "abc"
t = "ahbgdc"
```

Searching

```
Need → a

Found ✔

Need → b

Skip h

Found ✔

Need → c

Skip g
Skip d

Found ✔
```

Return

```text
True
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
O(1)
```

---

# 🏆 Approach 2 : Optimal (Two Pointers)

## Pattern

**Two Pointers**

---

## Idea

Maintain two pointers:

- `p1` → points to string `s`
- `p2` → points to string `t`

Rules:

- If characters match → move both pointers.
- If they don't match → move only `p2`.

If `p1` reaches the end of `s`, then `s` is a subsequence.

---

## Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p1 = 0
        p2 = 0

        while p1 < len(s) and p2 < len(t):

            if s[p1] == t[p2]:
                p1 += 1

            p2 += 1

        return p1 == len(s)
```

---

## Dry Run

```
s = abc
    ↑

t = ahbgdc
    ↑
```

### Step 1

```
a == a ✔

Move both
```

```
s = abc
     ↑

t = ahbgdc
     ↑
```

---

### Step 2

```
b != h

Move only t
```

```
s = abc
     ↑

t = ahbgdc
      ↑
```

---

### Step 3

```
b == b ✔

Move both
```

```
s = abc
      ↑

t = ahbgdc
       ↑
```

---

### Step 4

```
c != g

Move t
```

---

### Step 5

```
c != d

Move t
```

---

### Step 6

```
c == c ✔

Move both
```

Now

```
p1 == len(s)
```

Return

```text
True
```

---

# 📊 Complexity Comparison

| Approach | Time | Space |
|----------|------|------|
| Brute Force | O(n) | O(1) |
| Two Pointers | **O(n)** | **O(1)** |

---

# 🧠 Pattern Learned

✅ Two Pointers

---

# 💡 Key Concepts

- String Traversal
- Two Pointer Technique
- Character Matching
- Sequence Validation
- Greedy Pointer Movement

---

# 🌍 Real-World Applications

- Username Validation
- Search Suggestions
- DNA Sequence Matching
- Text Pattern Matching
- Document Verification
- Event Sequence Validation

---

# 🎯 Interview Questions

### What is a subsequence?

A sequence obtained by deleting zero or more characters while maintaining the original order.

---

### Difference between Subsequence and Substring?

| Subsequence | Substring |
|-------------|-----------|
| Characters remain in order | Characters must be contiguous |
| Can skip characters | Cannot skip characters |

Example

```
String = abcde
```

Subsequence

```
ace ✔
```

Substring

```
ace ✖
```

---

### Why does the Two Pointer approach work?

Because both strings are scanned only once while maintaining their relative order.

---

### Why move only `p2` when characters don't match?

Because we are searching for the current character of `s` inside `t`.

---

### When should you think of the Two Pointer pattern?

Whenever you need to compare or traverse two sequences efficiently.

Examples:

- Valid Palindrome
- Merge Sorted Array
- Reverse String
- Is Subsequence
- Two Sum II

---

# 📁 Folder Structure

```text
0392_Is_Subsequence/
│
├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 📚 DSA Pattern Progress

| Pattern | Problems Solved |
|----------|-----------------|
| Hash Map | ✅ |
| Stack | ✅ |
| Greedy | ✅ |
| Hash Set | ✅ |
| Two Pointers | ✅ Valid Palindrome |
| Two Pointers | ✅ Is Subsequence |
| Frequency Counting | ✅ |

---

# 🎯 Key Takeaways

- A subsequence maintains the relative order of characters.
- Two pointers allow both strings to be traversed in a single pass.
- If characters match, move both pointers.
- If they don't, move only the pointer in the larger string.
- This technique achieves **O(n)** time and **O(1)** space.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, understand the underlying pattern, compare brute-force and optimal approaches, and document every solution with explanations and complexity analysis.

**Think • Solve • Optimize • Repeat** 🚀