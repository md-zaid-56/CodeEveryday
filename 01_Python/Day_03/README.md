# 🐍 Python - Day 03

## 📅 Date
**03 July 2026**

---

# 📖 Topics Covered

Today focused on **Advanced Python Functions**, understanding how nested functions work internally, variable lookup using the LEGB rule, closures, and treating functions as first-class objects.

---

# 📚 Concepts Learned

## 1️⃣ Nested Functions

### Definition
A **Nested Function** is a function defined inside another function.

### Learned
- Creating functions inside another function
- Function frames
- Lifetime of nested functions
- Why nested functions cannot be accessed outside the outer function
- Memory model of nested functions

### Example

```python
def outer():

    def inner():
        print("Hello")

    inner()

outer()
```

---

## 2️⃣ Enclosing Scope (LEGB Rule)

### Definition

The **Enclosing Scope** is the scope of the outer function that surrounds a nested function.

Python searches variables in the following order:

```text
Local
↓

Enclosing
↓

Global
↓

Built-in
```

### Learned

- How Python searches variables
- Difference between Local and Enclosing scope
- Variable shadowing
- Scope resolution

Example

```python
def outer():

    x = 10

    def inner():
        print(x)

    inner()
```

---

## 3️⃣ nonlocal Keyword

### Definition

The `nonlocal` keyword allows a nested function to modify variables belonging to its enclosing function.

### Learned

- Why Python creates a new local variable by default
- Difference between reading and modifying variables
- How `nonlocal` works internally
- Difference between `global` and `nonlocal`

Example

```python
def outer():

    x = 20

    def inner():

        nonlocal x
        x += 10

    inner()

    print(x)
```

Output

```text
30
```

---

## 4️⃣ Closures

### Definition

A **Closure** is a nested function that remembers variables from its enclosing scope even after the outer function has finished execution.

### Learned

- Capturing variables
- Closure object
- Persistent state
- Internal working of closures
- Practical applications

Example

```python
def counter():

    count = 0

    def increment():

        nonlocal count
        count += 1
        return count

    return increment
```

Output

```text
1
2
3
```

---

## 5️⃣ First-Class Functions

### Definition

Functions in Python are **First-Class Objects**, meaning they can be:

- Stored in variables
- Passed as arguments
- Returned from functions
- Stored inside collections

### Learned

✔ Store functions in variables

✔ Store functions in dictionaries

✔ Pass functions as arguments

✔ Return functions from other functions

Example

```python
def add(a, b):
    return a + b

calculator = {
    "+": add
}

print(calculator["+"](10, 20))
```

---

# 📂 Files Created

```text
Day_03/
│
├── nested_fun.py
├── enclosing_scope.py
├── nonlocal_keyword.py
├── closure.py
├── first_class_fun.py
└── README.md
```

---

# 🧠 Key Takeaways

- Nested functions improve code organization.
- Python follows the **LEGB Rule** for variable lookup.
- `nonlocal` modifies variables from the enclosing scope.
- Closures preserve state even after the outer function returns.
- Functions are objects and can be treated like variables.

---

# 🎯 Interview Concepts Covered

- Nested Functions
- LEGB Rule
- Enclosing Scope
- Variable Shadowing
- global vs nonlocal
- Closures
- Function Objects
- First-Class Functions

---

# 📈 Progress

## Python Roadmap

- ✅ Python Memory Management
- ✅ Variables & Objects
- ✅ References
- ✅ Functions
- ✅ Parameters
- ✅ Return Statement
- ✅ Scope
- ✅ LEGB Rule
- ✅ Global Keyword
- ✅ Nested Functions
- ✅ Enclosing Scope
- ✅ nonlocal Keyword
- ✅ Closures
- ✅ First-Class Functions

---

# 🚀 What's Next?

Upcoming Python Topics:

- Decorators
- Lambda Functions
- map(), filter(), reduce()
- Iterators
- Generators
- Comprehensions
- Exception Handling
- File Handling
- Object-Oriented Programming (OOP)

---

## 💻 Repository

Part of my **"Basics to Advance - CodeEveryday Challenge"** 🚀

GitHub Repository:
**https://github.com/md-zaid-56/CodeEveryday**

---

⭐ *Learning consistently, one day at a time.*