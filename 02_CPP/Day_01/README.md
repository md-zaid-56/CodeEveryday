# 💻 C++ - Day 01

## 📅 Date
**04 July 2026**

---

# 📖 Topics Covered

Today marks the beginning of my C++ journey as part of the **CodeEveryday - Basics to Advance Challenge**.

The focus was on understanding how C++ programs are compiled and executed, learning primitive data types, variables, and interacting with users using `cin` and `cout`.

---

# 📚 Concepts Learned

---

# 1️⃣ Introduction to C++

## Definition

C++ is a **general-purpose, compiled, high-performance programming language** developed by **Bjarne Stroustrup**.

Unlike Python, C++ is a **statically typed** language and gives programmers greater control over memory and system resources.

---

## Key Points

- Compiled Language
- High Performance
- Supports Object-Oriented Programming
- Used in Game Development, Operating Systems, AI Libraries, Robotics and Embedded Systems

---

## Compilation Process

```text
C++ Source Code
        │
        ▼
Compiler (g++)
        │
        ▼
Executable File
        │
        ▼
Program Output
```

Compile

```bash
g++ first.cpp -o first
```

Run

```bash
./first
```

---

# 2️⃣ Variables & Data Types

## Definition

A **variable** is a named memory location used to store data.

Every variable has:

- Name
- Data Type
- Value
- Memory Location

---

## Primitive Data Types

| Data Type | Example | Size (Approx.) |
|------------|---------|---------------:|
| int | 10 | 4 Bytes |
| float | 3.14 | 4 Bytes |
| double | 3.141592653 | 8 Bytes |
| char | 'A' | 1 Byte |
| bool | true / false | 1 Byte |

---

## sizeof() Operator

Used to determine the memory occupied by a data type or variable.

Example

```cpp
cout << sizeof(int);
```

---

# 3️⃣ Input & Output

## cout

Used to display output on the screen.

Example

```cpp
cout << "Hello World";
```

---

## cin

Used to receive input from the keyboard.

Example

```cpp
cin >> age;
```

---

## Input & Output Operators

| Operator | Purpose |
|-----------|----------|
| << | Output Stream |
| >> | Input Stream |

---

# 📂 Files Created

```text
Day_01/
│
├── first.cpp
├── var.cpp
├── cout_cin.cpp
└── README.md
```

---

# 🧠 Programs Implemented

## Program 1

### First C++ Program

Learned

- Structure of a C++ program
- `#include`
- `using namespace std`
- `main()`
- `cout`
- `return 0`

---

## Program 2

### Variables & Data Types

Implemented

- int
- float
- double
- char
- bool

Also explored

- `sizeof()` operator
- Memory occupied by each data type

---

## Program 3

### cin & cout

Implemented

- Taking user input
- Displaying user input
- Reading integers
- Reading character arrays
- Printing formatted output

---

# 📌 Key Takeaways

- C++ is a compiled language.
- Variables store values directly in memory.
- Every variable requires a data type.
- Different data types occupy different memory sizes.
- `cout` is used for output.
- `cin` is used for input.
- `sizeof()` helps determine memory usage.

---

# 📈 Progress

## C++ Roadmap

- ✅ Introduction
- ✅ Variables
- ✅ Primitive Data Types
- ✅ sizeof()
- ✅ Input (`cin`)
- ✅ Output (`cout`)

---

# 🚀 Next Topics

- Operators
- Type Conversion
- Conditional Statements
- Loops
- Functions
- Arrays
- Strings
- Pointers
- References
- Object-Oriented Programming

---

## 🎯 Challenge Progress

**CodeEveryday – Basics to Advance**

- ✅ C++ Day 1 Completed
- 📅 Daily Learning
- 📂 Daily GitHub Push
- 🧩 Daily LeetCode Problem

---

⭐ *Learning C++ one concept at a time while building a strong foundation for DSA, CUDA Programming, and AI Development.*