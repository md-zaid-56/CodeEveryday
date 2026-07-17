# 📚 Longest Common Prefix (LeetCode #14)

## 🟢 Difficulty

Easy

---

# Pattern

- Strings
- Vertical Scanning
- Character Comparison

---

# 📖 Problem Statement

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string.

---

# Example 1

Input

```text
["flower","flow","flight"]
```

Output

```text
"fl"
```

---

# Example 2

Input

```text
["dog","racecar","car"]
```

Output

```text
""
```

Explanation

There is no common prefix.

---

# 🥉 Brute Force Approach

## Idea

Take the first word as the prefix.

Compare it with every other word.

If a word does not start with the prefix,

remove the last character from the prefix.

Repeat until all words share the same prefix.

---

## Algorithm

1. Store the first string as the prefix.
2. Compare it with every remaining string.
3. Shrink the prefix until it matches.
4. Return the final prefix.

---

## Code

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = strs[0]

        for word in strs[1:]:

            while not word.startswith(prefix):

                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
```

---

# Dry Run

Input

```text
["flower","flow","flight"]
```

Initial Prefix

```text
flower
```

Compare with

```text
flow
```

New Prefix

```text
flow
```

Still doesn't match

```text
flo
```

Still doesn't match

```text
fl
```

Compare with

```text
flight
```

Matches

```
fl
```

Return

```
fl
```

---

# Complexity

Time

```
O(n × m)
```

where:

- n = Number of strings
- m = Length of smallest string

Space

```
O(1)
```

---

# 🏆 Optimal Approach

## Idea

Compare characters vertically.

Example

```text
flower
flow
flight
```

Compare

```text
f f f ✅

l l l ✅

o o i ❌
```

Stop immediately.

Return

```
fl
```

---

## Algorithm

1. Use `zip(*strs)` to group characters column-wise.
2. Check whether all characters in a column are identical.
3. Append matching characters.
4. Stop on the first mismatch.

---

## Code

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        answer = ""

        for chars in zip(*strs):

            if len(set(chars)) == 1:
                answer += chars[0]
            else:
                break

        return answer
```

---

# Dry Run

Input

```text
["flower","flow","flight"]
```

Columns

```text
(f,f,f) ✅

(l,l,l) ✅

(o,o,i) ❌
```

Answer

```
fl
```

---

# Complexity

| Approach | Time | Space |
|----------|------|------:|
| Brute Force | O(n × m) | O(1) |
| Vertical Scan | O(n × m) | O(1) |

---

# Why is `zip(*strs)` Useful?

It groups characters from the same index together.

Example

```python
zip(*["abc","abd","abe"])
```

Produces

```text
('a','a','a')

('b','b','b')

('c','d','e')
```

This makes vertical comparison very simple.

---

# Real-World Applications

- Search Engine Auto-complete
- File Path Matching
- URL Prefix Detection
- DNA Sequence Comparison
- Text Processing
- Command-line Suggestions

---

# 🧠 Interview Questions

## Why does `zip(*strs)` stop automatically?

Because `zip()` stops at the shortest iterable.

---

## Why use `set(chars)`?

If every character is the same,

the set contains only one unique element.

---

## Why not compare every string character manually?

Using `zip()` makes the solution cleaner and easier to understand.

---

## Time Complexity?

```
O(n × m)
```

---

## Space Complexity?

```
O(1)
```

---

# Common Mistakes

❌ Forgetting that one string may be shorter.

---

❌ Comparing beyond the shortest string.

---

❌ Returning the first string directly.

---

❌ Ignoring the empty prefix case.

---

# Folder Structure

```text
Day_17/

├── brute.py
├── optimal.py
├── accepted_solution.png
└── README.md
```

---

# Key Takeaways

- Compare strings character by character.
- `zip(*strs)` is a powerful Python feature for vertical traversal.
- Stop immediately on the first mismatch.
- Always consider the shortest string when comparing prefixes.
- This problem introduces the **Vertical Scanning** pattern used in many string interview questions.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, compare brute-force and optimal solutions, analyze complexity, and document every concept for interview preparation.

**Learn • Practice • Build • Repeat** 🚀