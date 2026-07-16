# 🐍 Python - Day 16

## 📅 Date

16 July 2026

---

# 📖 Module

## Exception Handling in Python

Today I learned how Python handles runtime errors gracefully using **Exception Handling**.

Instead of allowing the program to crash, exceptions help us display meaningful messages and continue execution whenever possible.

This module covered:

- try
- except
- else
- finally
- raise (Custom Exceptions)

These concepts are widely used in professional software, APIs, banking systems, data processing, and web applications.

---

# 📚 Topics Covered

- try
- except
- ValueError
- ZeroDivisionError
- PermissionError
- else
- finally
- raise

---

# 1️⃣ try

## Definition

The `try` block contains code that might generate an exception.

Python executes this block first.

If no error occurs, execution continues normally.

If an error occurs, Python immediately jumps to the matching `except` block.

---

## Syntax

```python
try:
    # risky code
```

---

## Example

```python
try:
    number = int(input("Enter Number: "))
```

---

# 2️⃣ except

## Definition

The `except` block catches and handles exceptions so the program does not terminate unexpectedly.

---

## Syntax

```python
except ValueError:
    print("Invalid Input")
```

---

## Handling Multiple Exceptions

```python
try:
    number = int(input("Enter Number: "))
    result = 100 / number

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# Common Exceptions

| Exception | Description |
|------------|-------------|
| ValueError | Invalid value provided |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | File does not exist |
| TypeError | Invalid data type |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| PermissionError | Operation not permitted |

---

# 3️⃣ else

## Definition

The `else` block executes **only if no exception occurs** inside the `try` block.

It is useful for writing code that should run only after successful execution.

---

## Syntax

```python
try:
    ...

except:
    ...

else:
    ...
```

---

## Example

```python
try:
    num = int(input("Enter Number: "))
    result = 100 / num

except ValueError:
    print("Invalid Input")

else:
    print("Division Successful")
    print(result)
```

---

# Why use else?

Instead of writing

```python
print(result)
```

outside the `try` block,

place it inside `else`.

This prevents errors caused by uninitialized variables.

---

# 4️⃣ finally

## Definition

The `finally` block executes **every time**, regardless of whether an exception occurs.

It is mainly used for cleanup operations.

---

## Syntax

```python
finally:
    print("Program Finished")
```

---

## Example

```python
try:
    number = int(input())

except ValueError:
    print("Invalid")

finally:
    print("Application Closed")
```

---

# Real-World Uses

- Closing database connections
- Closing files
- Logging users out
- Releasing system resources
- Writing logs

---

# 5️⃣ raise

## Definition

The `raise` keyword allows programmers to manually generate exceptions based on business rules.

Python cannot automatically detect logical mistakes such as negative ages or invalid marks.

Using `raise`, we can create these exceptions ourselves.

---

## Syntax

```python
raise ValueError("Error Message")
```

---

## Example

```python
age = int(input("Enter Age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# Example with PermissionError

```python
if age < 18:
    raise PermissionError("You must be at least 18.")
```

---

# Handling Raised Exceptions

```python
try:
    age = int(input("Enter Age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        raise PermissionError("You must be at least 18.")

except ValueError as e:
    print(e)

except PermissionError as e:
    print(f"{type(e).__name__}: {e}")

else:
    print("Access Granted")

finally:
    print("Application Closed")
```

---

# Understanding Exception Objects

Suppose

```python
except PermissionError as e:
```

Then

```python
print(e)
```

Output

```
You must be at least 18.
```

To print the exception name

```python
print(type(e).__name__)
```

Output

```
PermissionError
```

To print both

```python
print(f"{type(e).__name__}: {e}")
```

Output

```
PermissionError: You must be at least 18.
```

---

# Execution Flow

```
                try
                 │
         Exception Occurred?
            │            │
          Yes            No
            │             │
            ▼             ▼
         except         else
            │             │
            └──────┬──────┘
                   ▼
                finally
```

---

# 🌍 Real-World Applications

Exception handling is used in:

- Banking Systems
- ATM Software
- Login Systems
- Registration Forms
- APIs
- Machine Learning Pipelines
- File Processing
- Data Validation
- Payment Gateways

---

# 🧠 Interview Questions

## What is an Exception?

A runtime error that interrupts the normal flow of a program.

---

## Why use try?

To execute code that may generate exceptions.

---

## Why use except?

To catch and handle exceptions.

---

## When does else execute?

Only if no exception occurs.

---

## When does finally execute?

Always.

---

## What does raise do?

It manually creates an exception.

---

## Difference between raise and except?

| raise | except |
|--------|---------|
| Creates an exception | Handles an exception |

---

## Why catch specific exceptions?

Because it makes debugging easier and prevents hiding unexpected errors.

---

# 📊 Time Complexity

Exception handling itself has no meaningful algorithmic complexity.

The complexity depends on the code inside the `try` block.

---

# 📁 Files

```text
Day_16/

├── try_except.py
├── else_finally.py
├── raise_exception.py
└── README.md
```

---

# 🎯 Key Takeaways

- `try` contains risky code.
- `except` handles runtime errors.
- `else` executes only when no exception occurs.
- `finally` always executes.
- `raise` allows developers to create custom exceptions.
- Custom exceptions enforce business rules.
- Catching specific exceptions is better than using a generic `except`.

---

# 📈 Python Progress

## Completed Topics

- Variables
- Data Types
- Operators
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- *args
- **kwargs
- Lambda Functions
- map()
- filter()
- File Handling
- Reading Files
- Exception Handling
  - try
  - except
  - else
  - finally
  - raise

---

# 🚀 Next Topics

- Modules & Packages
- Virtual Environments
- Object-Oriented Programming (Classes & Objects)

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn Python, C++, DSA, Linux, Data Science, Machine Learning, and AI by writing code daily, documenting every concept, and solving interview-focused problems.

**Learn • Practice • Build • Repeat** 🚀