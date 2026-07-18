# 🧩 LeetCode #58 - Length of Last Word

## 🟢 Difficulty

Easy

---

## 📚 Concepts

- Strings
- String Traversal
- Reverse Traversal
- Edge Cases

---

# 📖 Problem

Given a string `s` containing words and spaces, return the length of the last word.

A word is a sequence of non-space characters.

---

# Example 1

```text
Input:

s = "Hello World"

Output:

5
```

Explanation:

```text
Last Word = World

Length = 5
```

---

# Example 2

```text
Input:

s = "   fly me   to   the moon  "

Output:

4
```

The last word is:

```text
moon
```

Therefore:

```text
Length = 4
```

---

# 🥉 Approach 1 - Using Built-in Functions

We can use:

```python
split()
```

to divide the sentence into words.

## Code

```python
class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        words = s.split()

        return len(words[-1])
```

---

# How It Works

Input:

```text
"Hello World"
```

After:

```python
s.split()
```

We get:

```text
["Hello", "World"]
```

Last element:

```text
World
```

Then:

```python
len("World")
```

returns:

```text
5
```

---

# Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

because `split()` creates a list of words.

---

# 🏆 Approach 2 - Manual Reverse Traversal

Instead of creating another list, we can start from the end of the string.

## Code

```python
class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        length = 0

        # Ignore spaces from end

        while i >= 0 and s[i] == " ":
            i -= 1

        # Count characters of last word

        while i >= 0 and s[i] != " ":

            length += 1
            i -= 1

        return length
```

---

# 🧠 Dry Run

Input:

```text
"Hello World   "
```

Start from the end:

```text
Hello World___
             ↑
```

First, skip spaces.

Then reach:

```text
d
```

Now count:

```text
d → 1

l → 2

r → 3

o → 4

W → 5
```

Next character is a space.

Stop.

Answer:

```text
5
```

---

# Complexity

## Manual Approach

Time:

```text
O(n)
```

Worst case, we may traverse the string.

Space:

```text
O(1)
```

No extra list is created.

---

# 📊 Comparison

| Approach | Time | Space |
|---|---|---|
| `split()` | O(n) | O(n) |
| Reverse Traversal | O(n) | O(1) |

---

# 🧠 Interview Question

## Which solution would you prefer?

For simple and readable Python code:

```python
len(s.split()[-1])
```

is very clean.

However, if the interviewer asks:

> Can you solve it without using `split()`?

Then use manual reverse traversal.

This demonstrates a better understanding of string traversal and space optimization.

---

# 🔥 Interview Trap

Consider:

```text
"Hello World      "
```

If we immediately start counting from:

```python
len(s) - 1
```

we encounter spaces.

Therefore, we must first:

```text
Skip trailing spaces
```

and then:

```text
Count the last word
```

---

# Pattern Recognition

Do not memorize this only as:

> "Length of Last Word"

The useful pattern is:

```text
Start From End
      ↓
Skip Unwanted Characters
      ↓
Process Required Characters
      ↓
Stop When Condition Changes
```

This reverse-traversal pattern appears in many string and array problems.

---

# Key Takeaways

- `split()` gives a simple Python solution.
- Manual traversal gives O(1) extra space.
- Always consider trailing spaces.
- Reverse traversal can avoid unnecessary processing.
- Understand both readable and optimized approaches.

---

# 📁 Files

```text
Day_18/

├── brute.py
├── optimal.py
└── README.md
```

---

# 🚀 CodeEveryday Challenge

One DSA problem every day.

The goal is not only:

```text
Accepted ✅
```

The real goal is:

```text
Understand Brute Force
        ↓
Find Better Approach
        ↓
Analyze Complexity
        ↓
Recognize the Pattern
        ↓
Be Able to Explain WHY
```

**Learn • Solve • Analyze • Improve 🚀**