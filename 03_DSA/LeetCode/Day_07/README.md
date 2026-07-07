# 🔤 Valid Anagram (LeetCode #242)

## 🟢 Difficulty

Easy

---

# 📖 Problem Statement

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

An anagram is formed by rearranging the letters of another word using **all original characters exactly once**.

---

## Example 1

### Input

```text
s = "anagram"

t = "nagaram"
```

### Output

```text
True
```

---

## Example 2

### Input

```text
s = "rat"

t = "car"
```

### Output

```text
False
```

---

# 🥉 Approach 1 : Brute Force

## Idea

Convert `t` into a list.

For every character in `s`:

- Search the character in `t`
- If found, remove it
- Otherwise return `False`

If every character is removed successfully, both strings are anagrams.

---

## Brute Force Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        t = list(t)

        for char in s:

            if char in t:
                t.remove(char)
            else:
                return False

        return True
```

---

## Dry Run

Input

```text
s = "abc"

t = "cab"
```

Process

```text
Take 'a'

cab

↓

cb

Take 'b'

cb

↓

c

Take 'c'

c

↓

Empty
```

Return

```text
True
```

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

Searching and removing each character takes linear time.

---

### Space Complexity

```text
O(n)
```

Additional list is created from string `t`.

---

# 🚀 Approach 2 : Sorting

## Idea

If two strings are anagrams, sorting both strings produces the same result.

---

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
```

---

## Dry Run

```text
listen

↓

eilnst
```

```text
silent

↓

eilnst
```

Both are equal.

Return

```text
True
```

---

## Complexity Analysis

### Time Complexity

```text
O(n log n)
```

Sorting dominates the running time.

---

### Space Complexity

```text
O(n)
```

Sorting requires additional memory depending on implementation.

---

# 🏆 Approach 3 : Optimal (Hash Map)

## Idea

Count the frequency of every character in both strings.

If the frequency of every character matches, the strings are anagrams.

---

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:

            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
```

---

## Dry Run

Input

```text
s = "rat"

t = "tar"
```

Dictionary

```text
r → 1

a → 1

t → 1
```

After processing `t`

```text
r → 0

a → 0

t → 0
```

Return

```text
True
```

---

# 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|-----------------|
| Brute Force | O(n²) | O(n) |
| Sorting | O(n log n) | O(n) |
| Hash Map | O(n) | O(n) |

---

# 🧠 Key Concepts Learned

- Strings
- Lists
- Character Matching
- Sorting
- Hash Maps (Dictionary)
- Frequency Counting
- Time Complexity Optimization

---

# 🎯 Interview Questions

### What is an Anagram?

Two strings containing the same characters with the same frequency.

---

### Why check the lengths first?

If the lengths differ, they cannot be anagrams.

---

### Why is the brute force approach slow?

Searching and removing each character requires linear time.

---

### Why is sorting better?

Sorted anagrams become identical strings.

---

### Why is the Hash Map solution optimal?

It counts character frequencies in one pass, giving linear time complexity.

---

# 📁 Folder Structure

```text
Valid_Anagram/
│
├── brute.py
├── optimal.py
└── README.md
```

---

# 🚀 Part of my **#CodeEveryday – Basics to Advance Challenge**

Learning one algorithm every day while mastering fundamental interview patterns.

## Patterns Learned So Far

- ✅ Hash Map
- ✅ Stack
- ✅ Greedy
- ✅ Hash Set
- ✅ Two Pointers
- ✅ Frequency Counting