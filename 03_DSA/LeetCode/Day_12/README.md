# 🧩 Remove Duplicates from Sorted Array (LeetCode #26)

## 🟢 Difficulty

Easy

---

# Pattern

✅ Two Pointers

---

# Problem

Given a sorted array, remove duplicates **in-place** and return the number of unique elements.

---

# Example

Input

```text
[1,1,2]
```

Output

```text
k = 2

nums = [1,2,_]
```

---

# Brute Force

Remove duplicate elements using `pop()`.

Time Complexity

```
O(n²)
```

Space Complexity

```
O(1)
```

---

# Optimal

Use two pointers.

- First pointer keeps track of unique elements.
- Second pointer scans the array.

Whenever a new element is found,

copy it to the next unique position.

---

# Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

# Pattern Learned

Two Pointers

---

# Key Takeaways

- Array is already sorted.
- Two pointers avoid unnecessary removals.
- In-place modification saves memory.

---

# Files

```text
Day_12/

├── brute.py
├── optimal.py
└── README.md
```