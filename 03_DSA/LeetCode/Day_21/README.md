# 🧩 LeetCode #28 — Find the Index of the First Occurrence in a String

## 📅 Day 21 — CodeEveryday Challenge

**Difficulty:** 🟢 Easy  
**Topics:** Strings, String Matching  
**Pattern:** Sliding Comparison

---

# 📖 Problem Statement

Given two strings:

```text
haystack
needle
```

Return the index of the first occurrence of `needle` inside `haystack`.

If `needle` does not exist, return:

```text
-1
```

---

# Example 1

```text
haystack = "sadbutsad"

needle = "sad"
```

Output:

```text
0
```

Because the first occurrence of:

```text
"sad"
```

starts at index:

```text
0
```

---

# Example 2

```text
haystack = "leetcode"

needle = "leeto"
```

Output:

```text
-1
```

Because `"leeto"` does not occur inside `"leetcode"`.

---

# 🥉 Manual Approach

We check every possible position where `needle` could start.

```python
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):

            if haystack[i:i + m] == needle:

                return i

        return -1
```

---

# 🧠 Core Idea

Suppose:

```text
haystack = "hello"

needle = "ll"
```

Length:

```text
n = 5

m = 2
```

We compare windows of size `2`.

```text
hello

he → ❌

 el → ❌

  ll → ✅
```

The match starts at:

```text
Index 2
```

Therefore:

```text
Return 2
```

---

# 🔍 Why `n - m + 1`?

Suppose:

```text
haystack length = 5

needle length = 2
```

Valid starting indexes are:

```text
0
1
2
3
```

There are:

```text
5 - 2 + 1

= 4
```

possible starting positions.

Therefore:

```python
range(n - m + 1)
```

---

# Why Not Check Every Index Until n?

Suppose:

```text
haystack = "hello"

needle = "abc"
```

If only 2 characters remain in the haystack, there is no reason to check for a 3-character needle.

We stop when there are not enough characters left.

---

# 🪟 Sliding Comparison Pattern

Conceptually:

```text
Haystack:

s a d b u t s a d

Needle:

s a d
```

Start:

```text
[s a d] b u t s a d

  ↑

Compare
```

If not equal:

```text
s [a d b] u t s a d
```

Move one position.

This continues until:

```text
Match Found
```

or:

```text
No valid starting positions remain
```

---

# 🐍 Python Built-in Approach

Python provides:

```python
.find()
```

Example:

```python
text = "hello"

print(text.find("ll"))
```

Output:

```text
2
```

If not found:

```python
print(text.find("xyz"))
```

Output:

```text
-1
```

Therefore:

```python
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)
```

is a very short solution.

---

# ⚠️ Interview Perspective

Using:

```python
haystack.find(needle)
```

may solve the coding platform problem.

But an interviewer may ask:

> Can you implement the searching logic yourself?

Therefore, understanding the manual algorithm is more important than memorizing the built-in function.

---

# ⏱️ Complexity

For the simple manual matching approach:

```text
n = length of haystack

m = length of needle
```

Worst-case time complexity:

```text
O(n × m)
```

Why?

At multiple starting positions, we may compare up to `m` characters.

Extra space:

```text
O(1)
```

Conceptually, if implemented with direct character comparison.

---

# ⚠️ Python Slicing Detail

This code:

```python
haystack[i:i + m]
```

creates a substring in Python.

Therefore, slicing itself uses temporary memory.

For stricter `O(1)` extra-space reasoning, we can compare characters manually instead of creating slices.

Example:

```python
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):

            match = True

            for j in range(m):

                if haystack[i + j] != needle[j]:

                    match = False
                    break

            if match:

                return i

        return -1
```

---

# 🧠 Interview Question

What happens when:

```text
needle length > haystack length
```

Example:

```text
haystack = "hi"

needle = "hello"
```

Then:

```text
n - m + 1
```

is negative.

The loop does not execute.

Therefore:

```text
-1
```

is returned.

---

# 🔥 Tricky Question

Consider:

```text
haystack = "aaaaa"

needle = "aaa"
```

There are multiple matches:

```text
Index 0

Index 1

Index 2
```

But the problem asks for:

```text
FIRST occurrence
```

Therefore, return immediately when the first match is found:

```python
return i
```

Answer:

```text
0
```

---

# 🎯 Pattern Recognition

Don't remember this only as:

```text
LeetCode #28
```

Remember the general pattern:

```text
Large Sequence
      ↓
Take Candidate Window
      ↓
Compare With Target
      ↓
No Match?
      ↓
Shift Starting Position
      ↓
Repeat
```

This introduces the basic idea behind **string matching algorithms**.

Later, more advanced algorithms improve this process:

```text
Naive String Matching
        ↓
KMP
        ↓
Rabin-Karp
        ↓
Z Algorithm
```

---

# 🧠 Interview Insight

A strong interviewer may ask:

> Can you do better than O(n × m)?

That leads to algorithms such as:

```text
KMP — Knuth-Morris-Pratt
```

which can achieve:

```text
O(n + m)
```

You do not need KMP for today's Easy problem, but knowing that the naive approach has a more advanced optimization path is useful.

---

# 📊 Approaches

| Approach | Time | Extra Space |
|---|---:|---:|
| Python `.find()` | Implementation-dependent | Implementation-dependent |
| Slicing Comparison | O(n × m) worst case | Temporary substring space |
| Manual Character Comparison | O(n × m) | O(1) |
| KMP | O(n + m) | O(m) |

---

# ❌ Common Mistakes

### Returning the match itself

Wrong:

```python
return needle
```

The problem asks for:

```text
INDEX
```

---

### Returning all matches

The problem asks only for:

```text
FIRST occurrence
```

Return immediately after finding it.

---

### Wrong loop boundary

Be careful with:

```python
range(n - m + 1)
```

The `+1` is necessary because Python's `range()` excludes its ending value.

---

# 📁 Files

```text
03_DSA/
└── Day_21/
    ├── brute.py
    ├── simple.py
    ├── accepted_solution.png
    └── README.md
```

---

# 🚀 Day 21 — CodeEveryday

Today's focus:

```text
Strings
   ↓
Substring Search
   ↓
Sliding Comparison
   ↓
Manual Matching
   ↓
Complexity Analysis
```

The goal remains:

```text
Don't memorize the answer.

Understand the pattern.
```

**Learn • Solve • Analyze • Improve • Repeat 🚀**