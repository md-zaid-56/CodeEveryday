# 📚 Roman to Integer (LeetCode #13)

## 🟢 Difficulty

Easy

---

# Pattern

✅ Hash Map

✅ String Traversal

---

# 📖 Problem Statement

Roman numerals are represented by seven symbols:

| Symbol | Value |
|---------|------:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Convert the given Roman numeral into an integer.

---

# Example 1

Input

```text
III
```

Output

```text
3
```

---

# Example 2

Input

```text
LVIII
```

Output

```text
58
```

Explanation

```
L = 50
V = 5
III = 3

Total = 58
```

---

# Example 3

Input

```text
MCMXCIV
```

Output

```text
1994
```

---

# Roman Numeral Rules

Normally values are added.

Example

```
VI

5 + 1 = 6
```

But if a smaller numeral appears before a larger numeral, it is subtracted.

Example

```
IV

5 - 1 = 4
```

Another example

```
IX

10 - 1 = 9
```

---

# 🥉 Brute Force Approach

## Idea

Traverse the string from left to right.

If the current value is smaller than the next value,

subtract it.

Otherwise,

add it.

---

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):

            if i < len(s)-1 and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
```

---

# 🏆 Optimal Approach

## Idea

Traverse the string from right to left.

Keep track of the previous value.

If the current value is smaller than the previous value,

subtract it.

Otherwise,

add it.

---

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        answer = 0
        previous = 0

        for ch in reversed(s):

            value = roman[ch]

            if value < previous:
                answer -= value
            else:
                answer += value

            previous = value

        return answer
```

---

# Dry Run

Input

```
IV
```

Reverse

```
V
I
```

Step 1

```
answer = 5
previous = 5
```

Step 2

```
1 < 5

answer = 5 - 1

4
```

---

# Complexity

| Approach | Time | Space |
|----------|------|------:|
| Left to Right | O(n) | O(1) |
| Right to Left | O(n) | O(1) |

---

# Real-World Applications

- Symbol Conversion
- Encoding Systems
- Historical Date Processing
- Data Parsing
- Mapping Problems

---

# Interview Questions

## Why do we use a dictionary?

To convert Roman symbols into integer values in constant time.

---

## Why subtract instead of add?

Roman numerals use subtraction when a smaller symbol appears before a larger one.

Example

```
IV = 4

IX = 9
```

---

## Time Complexity?

```
O(n)
```

---

## Space Complexity?

```
O(1)
```

The dictionary has a fixed size.

---

# Folder Structure

```text
Day_16/

├── brute.py
├── optimal.py
├── accepted_solution.png
└── README.md
```

---

# Key Takeaways

- Roman numerals follow addition and subtraction rules.
- Hash Maps provide constant-time symbol lookup.
- Traversing from right to left simplifies the logic.
- This problem strengthens dictionary usage and string traversal.

---

# CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem daily, compare brute-force and optimal solutions, analyze complexity, and document every concept for interview preparation.

**Learn • Practice • Build • Repeat** 🚀