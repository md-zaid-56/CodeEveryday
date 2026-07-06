# 💻 C++ - Day 06

## 📅 Date
06 July 2026

---

# 📖 Introduction

Today I learned the fundamentals of **Operators**, **Type Conversion (Casting)**, and **Conditional Statements** in C++. These concepts are the foundation of decision-making and mathematical operations in programming.

---

# 📚 Topics Covered

## 1️⃣ Operators

### Definition

Operators are special symbols used to perform operations on variables and values.

---

### Types of Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus | `a % b` |

---

### Relational Operators

| Operator | Description |
|----------|-------------|
| `==` | Equal To |
| `!=` | Not Equal To |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |

---

### Logical Operators

| Operator | Description |
|----------|-------------|
| `&&` | Logical AND |
| `||` | Logical OR |
| `!` | Logical NOT |

---

### Assignment Operators

| Operator | Description |
|----------|-------------|
| `=` | Assignment |
| `+=` | Add and Assign |
| `-=` | Subtract and Assign |
| `*=` | Multiply and Assign |
| `/=` | Divide and Assign |

---

### Increment & Decrement

| Operator | Description |
|----------|-------------|
| `++` | Increment by 1 |
| `--` | Decrement by 1 |

---

## Example

```cpp
int a = 5;
int b = 2;

cout << a + b << endl;
cout << a - b << endl;
cout << a * b << endl;
cout << a / b << endl;
cout << a % b << endl;
```

---

# 2️⃣ Type Conversion (Casting)

## Definition

Type Conversion is the process of converting one data type into another.

---

## Types

### Implicit Type Conversion

Performed automatically by the compiler.

Example

```cpp
int a = 18;
float b = a;
```

Output

```text
18 → 18.0
```

---

### Explicit Type Conversion (Type Casting)

Performed manually by the programmer.

Example

```cpp
float pi = 3.14567;
int x = (int)pi;
```

Output

```text
3
```

---

## Type Promotion

Example

```cpp
int a = 5;
double b = 7.87256;

cout << a + b;
```

Output

```text
12.87256
```

The integer is automatically promoted to a double before addition.

---

# 3️⃣ Conditional Statements

## Definition

Conditional statements allow a program to make decisions based on whether a condition is true or false.

---

## if Statement

```cpp
if(condition)
{
    // Code executes if condition is true
}
```

---

## if-else Statement

```cpp
if(condition)
{
    // True Block
}
else
{
    // False Block
}
```

---

## else-if Ladder

```cpp
if(condition1)
{
}
else if(condition2)
{
}
else
{
}
```

---

## Example

```cpp
int jerseyNumber;

cin >> jerseyNumber;

if(jerseyNumber == 7)
{
    cout << "You Love CR7";
}
else if(jerseyNumber == 10)
{
    cout << "You Love Messi";
}
else
{
    cout << "Player not found";
}
```

---

# 📂 Files

```text
Day_06/
│
├── Operator.cpp
├── type_casting.cpp
├── condition.cpp
└── README.md
```

---

# 📊 Concepts Learned

- Arithmetic Operators
- Relational Operators
- Logical Operators
- Assignment Operators
- Increment & Decrement Operators
- Implicit Type Conversion
- Explicit Type Casting
- Type Promotion
- Integer Division
- Floating Point Division
- if Statement
- if-else Statement
- else-if Ladder

---

# Key Takeaways

- Operators perform mathematical and logical operations.
- Integer division removes the decimal part.
- Type casting converts one data type into another.
- Implicit conversion happens automatically.
- Explicit conversion is performed by the programmer.
- Conditional statements help programs make decisions.
- The `else-if` ladder is useful for handling multiple conditions.

---

# Interview Questions

### What is an operator?

A symbol that performs operations on variables or values.

---

### What is the difference between `=` and `==`?

`=` is an assignment operator.

`==` is a comparison operator.

---

### What is implicit type conversion?

Automatic conversion performed by the compiler.

---

### What is explicit type casting?

Manual conversion performed by the programmer.

---

### Why does `5 / 2` return `2`?

Because both operands are integers, resulting in integer division.

---

### Difference between `if` and `if-else`?

- `if` executes code only when the condition is true.
- `if-else` executes one block if true and another block if false.

---

# Folder Structure

```text
02_CPP/
└── Day_06/
    ├── Operator.cpp
    ├── type_casting.cpp
    ├── condition.cpp
    └── README.md
```

---

# Progress

## C++ Roadmap

### Day 1 ✅

- Introduction to C++
- Variables
- Data Types
- Input & Output

### Day 2 ✅

- Operators
- Type Conversion
- Conditional Statements

---

# Next Topics

- Switch Statement
- Loops (for, while, do-while)
- Patterns
- Functions
- Arrays

---

# 🚀 CodeEveryday Challenge

Building strong C++ fundamentals one concept at a time while progressing towards becoming an AI/ML Engineer & Software Developer.