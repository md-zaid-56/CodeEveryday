# 🐍 Python - Day 09

## 📅 Date
09 July 2026

---

# 📖 Introduction

Today I explored some of Python's most powerful intermediate concepts that are widely used in real-world software development.

Instead of learning isolated syntax, I focused on understanding how Python handles dynamic function arguments and how large applications organize their code using modules.

These concepts are heavily used in frameworks like **FastAPI**, **Django**, **Flask**, and many Machine Learning libraries.

---

# 📚 Topics Covered

- *args
- **kwargs
- Modules
- Packages
- Import Statements
- Module Aliasing

---

# 1️⃣ *args

## Definition

`*args` allows a function to accept **any number of positional arguments**.

Python automatically stores these arguments as a **tuple**.

---

## Syntax

```python
def function_name(*args):
    pass
```

---

## Example

```python
def calculate_bill(*prices):

    total = 0

    for price in prices:
        total += price

    return total


print(calculate_bill(500, 1200))
print(calculate_bill(1200, 1500, 250))
```

### Output

```text
1700
2950
```

---

## Internal Working

```python
calculate_bill(10,20,30)
```

Internally,

```python
args = (10,20,30)
```

Python stores positional arguments inside a **tuple**.

---

## Why Tuple?

- Immutable
- Faster than list
- Memory efficient
- Function arguments are generally read-only

---

## Real-World Uses

- Shopping Cart
- Calculator
- Student Marks
- Data Analysis
- Logging Functions

---

# 2️⃣ **kwargs

## Definition

`**kwargs` allows a function to accept **any number of keyword arguments**.

Python stores them inside a **dictionary**.

---

## Syntax

```python
def function_name(**kwargs):
    pass
```

---

## Example

```python
def register_employee(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


register_employee(
    name="Zaid",
    position="Data Scientist",
    department="AI"
)
```

---

### Output

```text
name: Zaid
position: Data Scientist
department: AI
```

---

## Internal Working

```python
register_employee(
    name="Zaid",
    age=22
)
```

becomes

```python
details = {
    "name": "Zaid",
    "age": 22
}
```

---

## Why Dictionary?

Because keyword arguments have

- Keys
- Values

which are naturally represented by a dictionary.

---

## Real-World Uses

- Employee Registration
- API Parameters
- Configuration Files
- User Profiles
- Dynamic Settings

---

# *args vs **kwargs

| *args | **kwargs |
|--------|-----------|
| Positional Arguments | Keyword Arguments |
| Stored as Tuple | Stored as Dictionary |
| Uses * | Uses ** |

---

# 3️⃣ Modules

## Definition

A **Module** is simply a Python file (`.py`) containing reusable code.

---

## Example

```text
calculator.py
```

---

## calculator.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

---

## Import Entire Module

```python
import calculator

print(calculator.add(5,6))
```

---

## Import Specific Function

```python
from calculator import add

print(add(5,6))
```

---

## Module Alias

```python
import calculator as calc

print(calc.add(5,6))
```

---

## Why Modules?

- Code Reusability
- Better Organization
- Easier Maintenance
- Cleaner Projects
- Team Collaboration

---

# 4️⃣ Packages

## Definition

A **Package** is a directory containing multiple Python modules.

---

## Example

```text
StudentManagement/

students/
│
├── login.py
├── attendance.py
├── marks.py
└── fees.py
```

---

# Module vs Package

| Module | Package |
|---------|----------|
| Single Python file | Folder containing modules |
| Reusable code | Collection of modules |

---

# Built-in Modules

Python provides many built-in modules.

### math

```python
import math

print(math.sqrt(25))
```

---

### random

```python
import random

print(random.randint(1,10))
```

---

### datetime

```python
import datetime

print(datetime.datetime.now())
```

---

# Practical Files

```text
Day_09/

├── args.py
├── kwargs.py
├── calculator.py
├── main.py
└── README.md
```

---

# 📊 Summary

| Concept | Purpose |
|----------|----------|
| *args | Accept unlimited positional arguments |
| **kwargs | Accept unlimited keyword arguments |
| Module | Reusable Python file |
| Package | Collection of modules |
| Alias | Shorter module name |

---

# 💼 Real-World Applications

## *args

- Billing System
- Shopping Cart
- Student Marks
- Calculator

---

## **kwargs

- Employee Registration
- User Profile
- Configuration Settings
- API Request Parameters

---

## Modules

- Banking Software
- Library Management System
- Machine Learning Projects
- FastAPI Applications

---

## Packages

- Django Apps
- Python Libraries
- AI Projects
- Enterprise Applications

---

# 🧠 Interview Questions

### What is *args?

A function parameter that accepts any number of positional arguments.

---

### What is **kwargs?

A function parameter that accepts any number of keyword arguments.

---

### Why is *args stored as a tuple?

Because tuples are immutable, lightweight, and efficient for storing positional arguments.

---

### Why is **kwargs stored as a dictionary?

Because keyword arguments are key-value pairs.

---

### What is a Module?

A Python file containing reusable code.

---

### What is a Package?

A directory containing multiple modules.

---

### Difference between Module and Package?

| Module | Package |
|---------|----------|
| Python File | Folder |
| Single Unit | Collection of Modules |

---

### Why do we use Modules?

- Reusability
- Readability
- Scalability
- Easier Maintenance

---

# 🎯 Key Takeaways

- `*args` accepts unlimited positional arguments.
- `**kwargs` accepts unlimited keyword arguments.
- Python stores `*args` as a tuple.
- Python stores `**kwargs` as a dictionary.
- Modules help organize reusable code.
- Packages group multiple related modules together.
- Modular programming makes projects cleaner and easier to maintain.

---

# 📈 Python Progress

## Day 01 ✅

- Python Memory
- Variables

---

## Day 02 ✅

- Functions
- Scope
- LEGB Rule
- Global Keyword

---

## Day 03 ✅

- Closures
- Nested Functions
- First-Class Functions
- Nonlocal Keyword

---

## Day 05 ✅

- Lambda Functions
- map()
- filter()

---

## Day 07 ✅

- List Comprehension
- Dictionary Comprehension
- zip()

---

## Day 09 ✅

- *args
- **kwargs
- Modules
- Packages
- Import Statements
- Module Aliasing

---

# 🚀 Next Topics

- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- Iterators & Generators
- Decorators
- Virtual Environments

---

# 🚀 CodeEveryday Challenge

Building strong Python fundamentals one concept at a time by learning, practicing, documenting, and applying every topic through real-world examples.

**Learn • Practice • Build • Repeat** 🐍