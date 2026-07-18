# 🐍 Python - Day 18

## 📅 Date

18 July 2026

---

# 📚 Topics Covered

Today I learned some useful Python built-in functions:

- `divmod()`
- `bin()`
- `ord()`
- `chr()`

The main goal was to understand what these functions do and where they can be useful instead of writing unnecessary logic manually.

---

# 1️⃣ divmod()

The `divmod()` function performs division and gives us two values:

- Quotient
- Remainder

## Example

```python
result = divmod(17, 5)

print(result)
```

Output:

```text
(3, 2)
```

Here:

```text
17 / 5

Quotient  = 3
Remainder = 2
```

We can access them using:

```python
result[0]
result[1]
```

---

## Without divmod()

Normally we could write:

```python
quotient = 17 // 5
remainder = 17 % 5
```

Using `divmod()`:

```python
quotient, remainder = divmod(17, 5)
```

This gives both results together.

---

# 🌍 Real-World Example

Suppose we have:

```text
135 minutes
```

We want to convert it into hours and remaining minutes.

```python
hours, minutes = divmod(135, 60)
```

Result:

```text
2 Hours
15 Minutes
```

---

# 2️⃣ bin()

The `bin()` function converts an integer into its binary representation.

## Example

```python
number = 10

print(bin(number))
```

Output:

```text
0b1010
```

Here:

```text
0b
```

indicates that the number is represented in binary.

So:

```text
Decimal : 10
Binary  : 1010
```

---

# Why is Binary Important?

Computers internally work using binary values:

```text
0
1
```

Understanding binary becomes important when learning:

- Bit Manipulation
- Operating Systems
- Computer Architecture
- Networking
- Low-Level Programming
- DSA Bitwise Problems

---

# 3️⃣ ord()

The `ord()` function converts a character into its Unicode code point.

Example:

```python
print(ord("A"))
```

Output:

```text
65
```

Another example:

```python
print(ord("a"))
```

Output:

```text
97
```

---

# 4️⃣ chr()

`chr()` performs the opposite operation of `ord()`.

It converts a Unicode code point into its corresponding character.

Example:

```python
print(chr(65))
```

Output:

```text
A
```

Therefore:

```text
Character

A

 ↓ ord()

65

 ↓ chr()

A
```

---

# 🧠 Interview Concepts

## What does divmod() return?

It returns a tuple containing:

```text
(quotient, remainder)
```

---

## Difference between `/`, `//`, `%` and `divmod()`?

```text
/        → Division

//       → Floor Division

%        → Remainder

divmod() → Quotient + Remainder
```

---

## What does bin() return?

`bin()` returns a **string representation** of the binary number.

Example:

```python
result = bin(10)

print(type(result))
```

Output:

```text
<class 'str'>
```

This is an important interview trap.

---

## Difference between ord() and chr()?

```text
ord()

Character → Unicode Code Point
```

```text
chr()

Unicode Code Point → Character
```

They perform opposite operations.

---

# 🔥 Tricky Interview Question

What will this print?

```python
print(ord("A") + 1)
```

Output:

```text
66
```

Now:

```python
print(chr(ord("A") + 1))
```

Output:

```text
B
```

This technique can be useful when working with characters and alphabets.

---

# Key Takeaways

- `divmod()` gives quotient and remainder together.
- `bin()` converts integers into binary representation.
- `ord()` converts a character into its Unicode code point.
- `chr()` converts a Unicode code point back into a character.
- `ord()` and `chr()` are opposite operations.
- `bin()` returns a string, not an integer.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey.

The goal is not just to memorize syntax, but to understand:

> What does it do?  
> Why does it exist?  
> Where can I use it?

**Learn • Understand • Practice • Build • Repeat 🚀**