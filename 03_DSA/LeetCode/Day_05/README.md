# 🔤 Valid Palindrome (LeetCode #125)

## 🟢 Difficulty
Easy

---

# 📖 Problem Statement

Given a string `s`, determine whether it is a palindrome after:

- Converting all uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

Return `true` if the string is a palindrome; otherwise, return `false`.

---

## Example 1

### Input

```text
s = "A man, a plan, a canal: Panama"
```

### Output

```text
true
```

---

## Example 2

### Input

```text
s = "race a car"
```

### Output

```text
false
```

---

# 🧠 Approach 1 : Brute Force

## Idea

1. Traverse the string.
2. Keep only alphanumeric characters.
3. Convert every character to lowercase.
4. Reverse the cleaned string.
5. Compare both strings.

---

## Brute Force Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        reversed_string = cleaned[::-1]

        return cleaned == reversed_string
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

# 🚀 Approach 2 : Two Pointers (Optimal)

## Idea

Use two pointers:

- One starts from the beginning.
- One starts from the end.

Skip all non-alphanumeric characters and compare characters after converting them to lowercase.

If every comparison matches, the string is a palindrome.

---

## Optimal Code

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

# 🖥 Dry Run

Input

```text
"A man, a plan, a canal: Panama"
```

After ignoring spaces and symbols

```text
amanaplanacanalpanama
```

Compare

```text
a == a ✅
m == m ✅
a == a ✅
...
```

All characters match.

Return

```text
True
```

---

# 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|-----------------|
| Brute Force | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |

---

# 💡 Key Concepts Learned

- Strings
- Two Pointer Technique
- Character Validation
- String Manipulation
- Time Complexity Optimization

---

# 📁 Folder Structure

```text
Valid_Palindrome/
│
├── brute.py
├── two_pointer.py
└── README.md
```

---

# 🎯 Interview Takeaway

The brute-force solution creates a new cleaned string and compares it with its reverse, requiring extra memory.

The optimal solution uses the **Two Pointer** technique, comparing characters directly from both ends while skipping non-alphanumeric characters. This reduces the space complexity from **O(n)** to **O(1)**.

---

# 🚀 Part of my **#CodeEveryday – Basics to Advance Challenge**

Learning one concept, one problem, and one GitHub commit every single day.