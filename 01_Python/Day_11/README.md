# 🐍 Python - Day 11

## 📅 Date

11 July 2026

---

# 📖 Introduction

Today I explored three useful built-in Python functions that make code cleaner, more readable, and more Pythonic.

Instead of writing extra loops or counters, Python provides built-in functions to simplify common programming tasks.

---

# 📚 Topics Covered

- enumerate()
- any()
- all()

---

# 1️⃣ enumerate()

## Definition

`enumerate()` is used to iterate over a sequence while keeping track of the index of each element.

---

## Syntax

```python
enumerate(iterable, start=0)
```

- `iterable` → List, tuple, string, etc.
- `start` → Starting index (default is 0)

---

## Example

```python
books = ["Python", "C++", "Machine Learning"]

for index, book in enumerate(books, start=1):
    print(index, book)
```

### Output

```text
1 Python
2 C++
3 Machine Learning
```

---

## Use Cases

- Leaderboards
- Student Roll Numbers
- Product Lists
- Menu Systems
- Reports

---

# 2️⃣ any()

## Definition

`any()` returns **True** if at least one element in the iterable is True.

---

## Syntax

```python
any(iterable)
```

---

## Example

```python
attendance = [False, False, True]

print(any(attendance))
```

### Output

```text
True
```

---

## Use Cases

- Checking if at least one user is online
- Product availability
- Login validation
- Alert systems

---

# 3️⃣ all()

## Definition

`all()` returns **True** only if every element in the iterable is True.

---

## Syntax

```python
all(iterable)
```

---

## Example

```python
passed = [True, True, True]

print(all(passed))
```

### Output

```text
True
```

---

## Example 2

```python
passed = [True, False, True]

print(all(passed))
```

### Output

```text
False
```

---

## Use Cases

- Checking if all students passed
- Order completion
- File upload verification
- Validation systems

---

# 📊 Difference Between any() and all()

| Function | Returns True When |
|----------|-------------------|
| any() | At least one element is True |
| all() | Every element is True |

---

# 🌍 Real-World Example

### enumerate()

Displaying a ranked list of books.

### any()

Checking if at least one book is available in the library.

### all()

Checking whether all borrowed books have been returned.

---

# 📁 Files

```text
Day_11/

├── Day_11.py
└── README.md
```

---

# 🎯 Key Takeaways

- `enumerate()` provides both the index and value while iterating.
- `any()` checks if at least one value is True.
- `all()` checks if every value is True.
- These built-in functions reduce code complexity and improve readability.
- They are commonly used in Python interviews and real-world applications.

---

# 📚 Interview Questions

## What does enumerate() do?

It returns both the index and the value while iterating over an iterable.

---

## What is the default starting index of enumerate()?

```python
0
```

---

## Difference between any() and all()?

- `any()` → Returns True if at least one element is True.
- `all()` → Returns True only if every element is True.

---

## When would you use any()?

When checking if at least one condition is satisfied.

---

## When would you use all()?

When every condition must be satisfied before proceeding.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn Python, C++, DSA, Linux, and AI step by step while documenting every concept with code, notes, and practical examples.

**Learn • Practice • Build • Repeat** 🚀