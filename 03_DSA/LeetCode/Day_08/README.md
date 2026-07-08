# 🔤 Valid Palindrome (LeetCode #125)

## 🟢 Difficulty

Easy

---

# 📖 Problem Statement

A phrase is a palindrome if, after:

- Removing all non-alphanumeric characters.
- Converting uppercase letters to lowercase.

it reads the same forward and backward.

Return `True` if it is a palindrome, otherwise return `False`.

---

## Example 1

### Input

```text
s = "A man, a plan, a canal: Panama"
```

### Output

```text
True
```

---

## Example 2

### Input

```text
s = "race a car"
```

### Output

```text
False
```

---

## Example 3

### Input

```text
s = " "
```

### Output

```text
True
```

---

# 🥉 Approach 1 : Brute Force

## Idea

1. Remove all non-alphanumeric characters.
2. Convert all letters to lowercase.
3. Create a reversed copy manually.
4. Compare both strings.

---

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        reverse = ""

        for i in range(len(cleaned) - 1, -1, -1):
            reverse += cleaned[i]

        return cleaned == reverse
```

---

## Dry Run

Input

```text
"A man, a plan, a canal: Panama"
```

Cleaned String

```text
amanaplanacanalpanama
```

Reverse

```text
amanaplanacanalpanama
```

Both strings are equal.

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
O(n)
```

---

# 🏆 Approach 2 : Optimal (Two Pointers)

## Pattern

Two Pointers

---

## Idea

Instead of creating a new string:

- Keep one pointer at the beginning.
- Keep another pointer at the end.
- Skip non-alphanumeric characters.
- Compare characters after converting to lowercase.
- Move inward until the pointers meet.

---

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

## Dry Run

Input

```text
"A man, a plan, a canal: Panama"
```

```
Left → A
Right → a

↓

Match

↓

Move both pointers

↓

Skip spaces and punctuation

↓

Continue comparison
```

Eventually,

```
Left >= Right
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

No extra string is created.

---

# 📊 Complexity Comparison

| Approach | Time | Space |
|----------|------|------|
| Brute Force | O(n) | O(n) |
| Two Pointers | **O(n)** | **O(1)** |

---

# 🧠 Pattern Learned

✅ Two Pointers

---

# 💡 Key Concepts

- String Traversal
- Character Validation (`isalnum()`)
- Case Conversion (`lower()`)
- Two Pointer Technique
- Space Optimization

---

# 🎯 Interview Questions

### Why remove non-alphanumeric characters?

Because punctuation and spaces are ignored according to the problem statement.

---

### Why convert characters to lowercase?

To make the comparison case-insensitive.

---

### Why is the Two Pointer approach better?

It avoids creating a new string, reducing the space complexity from **O(n)** to **O(1)**.

---

### When should you think of the Two Pointer pattern?

Whenever you need to compare elements from both ends of a string or array.

Examples:

- Valid Palindrome
- Reverse String
- Merge Sorted Array
- Two Sum II
- Container With Most Water

---

# 📁 Folder Structure

```text
0125_Valid_Palindrome/
│
├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 🚀 Part of my **#CodeEveryday – Basics to Advance Challenge**

Learning one Data Structures & Algorithms pattern every day while building strong problem-solving skills.

## Patterns Learned So Far

- ✅ Hash Map
- ✅ Stack
- ✅ Greedy
- ✅ Hash Set
- ✅ Two Pointers
- ✅ Frequency Counting