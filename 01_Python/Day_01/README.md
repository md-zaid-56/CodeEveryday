# 🐍 Day 001 - Python Memory Model

> Understanding how Python stores variables and objects in memory.

---

# 🎯 Objective

Learn how Python handles variables, objects, references, mutable and immutable data types.

---

# 📚 Topics Covered

- Variables
- Objects
- References
- Memory Allocation
- `id()` Function
- `type()` Function
- Mutable Objects
- Immutable Objects
- Assignment
- Copy vs Reference

---

# 🧠 How Python Stores Variables

When we write:

```python
x = 10
```

Python performs three steps:

1. Creates an integer object `10`.
2. Creates the variable name `x`.
3. Makes `x` reference the integer object.

```
Variable

x
│
▼

Memory
┌───────┐
│  10   │
└───────┘
```

> Python variables do **not** store values.
> They store **references** to objects.

---

# 🔍 Checking Object Identity

The `id()` function returns the unique identity (memory reference) of an object during its lifetime.

```python
x = 10

print(id(x))
```

Example Output

```text
140573864019216
```

---

# Multiple Variables Referencing the Same Object

```python
x = 10
y = x

print(id(x))
print(id(y))
```

Output

```text
140573864019216
140573864019216
```

Both variables point to the same object.

```
x ───┐
     │
     ▼
    10
     ▲
     │
y ───┘
```

---

# Every Value is an Object

Python is an object-oriented language.

Everything is an object.

```python
print(type(10))
print(type(3.14))
print(type("Hello"))
print(type(True))
print(type([1,2,3]))
```

Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'list'>
```

---

# Immutable Objects

Immutable objects cannot be modified after creation.

Examples

- int
- float
- bool
- str
- tuple

Example

```python
x = 10
x = 20
```

Python does **not** modify `10`.

Instead, it creates a new object `20` and makes `x` reference it.

```
Before

x → 10

After

10

x → 20
```

---

# Mutable Objects

Mutable objects can be modified without creating a new object.

Examples

- list
- dictionary
- set

Example

```python
numbers = [1,2,3]

numbers.append(4)
```

The list is modified in place.

```
numbers

↓

[1,2,3,4]
```

---

# Verifying with id()

```python
numbers = [1,2,3]

print(id(numbers))

numbers.append(4)

print(id(numbers))
```

Output

```text
Same Memory Address
```

The object remains the same.

---

# Reference Example

```python
a = [1,2,3]

b = a

b.append(4)

print(a)
```

Output

```text
[1,2,3,4]
```

Reason:

Both variables reference the same list.

```
a ───┐
     │
     ▼

[1,2,3]

     ▲
     │
b ───┘
```

---

# Copy Example

```python
a = [1,2,3]

b = a.copy()

b.append(4)

print(a)
print(b)
```

Output

```text
[1,2,3]
[1,2,3,4]
```

Reason:

`copy()` creates a new object.

```
a ───► [1,2,3]

b ───► [1,2,3,4]
```

---

# Difference Between Assignment and Copy

| Assignment | Copy |
|------------|------|
| Shares the same object | Creates a new object |
| Changes affect both variables | Changes affect only the copied object |
| Faster | Uses additional memory |

---

# Key Functions Learned

## id()

Returns the identity (memory reference) of an object.

```python
print(id(x))
```

---

## type()

Returns the data type of an object.

```python
print(type(x))
```

---

# Key Takeaways

- Variables store references, not values.
- Everything in Python is an object.
- Immutable objects create new objects when changed.
- Mutable objects are modified in place.
- `id()` helps verify object identity.
- `type()` identifies an object's type.
- Assignment shares references.
- `copy()` creates independent objects.

---

# 📌 Interview Questions

### Q1. Do Python variables store values?

No.

They store references to objects.

---

### Q2. What does `id()` return?

It returns the unique identity (memory reference) of an object during its lifetime.

---

### Q3. Difference between mutable and immutable objects?

| Mutable | Immutable |
|----------|-----------|
| Can be modified | Cannot be modified |
| Same object after modification | New object created after reassignment |

---

### Q4. Why does changing one list affect another?

Because both variables reference the same object.

---

# 🎯 What I Learned Today

- How Python stores variables in memory.
- Difference between assignment and copying.
- Mutable vs immutable objects.
- Usage of `id()` and `type()`.
- Importance of object references.

---

## 📅 Day 001 Status

✅ Python Memory Model Completed

**Next Topic:** Functions, Scope, and Object Mutability in Python.