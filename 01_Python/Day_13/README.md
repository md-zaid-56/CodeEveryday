# 🐍 Python - Day 13

## 📅 Date

13 July 2026

---

# 📖 Introduction

Today I learned one of the most important topics in Python — **File Handling**.

Variables store data temporarily in RAM, but once a program terminates, that data is lost. File Handling allows us to store information permanently on disk, making it possible to save logs, reports, datasets, configuration files, and user information.

This topic is widely used in Software Development, Data Science, Automation, Machine Learning, and Backend Development.

---

# 📚 Topics Covered

- File Handling
- Opening Files
- File Modes
- Read Mode (`r`)
- Write Mode (`w`)
- Append Mode (`a`)
- Create Mode (`x`)
- `with open()`
- `read()`
- `readline()`
- `readlines()`
- Reading Files using `for` Loop
- `.strip()`

---

# 📂 What is File Handling?

File Handling is the process of creating, reading, writing, updating, and managing files using Python.

Unlike variables, files store data permanently.

---

# 🌍 Real-World Applications

- Student Management Systems
- Banking Applications
- Chat Applications
- Server Logs
- CSV Datasets
- Machine Learning
- Configuration Files
- Reports
- Text Editors

---

# 📂 Opening a File

## Syntax

```python
file = open("filename.txt", "mode")
```

Example

```python
file = open("student.txt", "r")
```

---

# 📚 File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read existing file |
| `"w"` | Write (creates or overwrites file) |
| `"a"` | Append data to existing file |
| `"x"` | Create a new file (fails if it already exists) |

---

# 📝 Write Mode (`w`)

Creates a new file if it doesn't exist.

If the file already exists, all previous content is removed.

## Example

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")
```

---

# ➕ Append Mode (`a`)

Adds new data at the end of the file.

Existing content remains unchanged.

## Example

```python
with open("notes.txt", "a") as file:
    file.write("\nMachine Learning")
```

---

# 📖 Read Mode (`r`)

Reads the contents of a file.

## Example

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

# 🆕 Create Mode (`x`)

Creates a new file.

If the file already exists,

Python raises

```text
FileExistsError
```

Example

```python
with open("notes.txt", "x") as file:
    file.write("Hello")
```

---

# ⭐ Why Use `with open()`?

Instead of manually opening and closing files,

```python
file = open("notes.txt", "r")

print(file.read())

file.close()
```

Python provides a cleaner approach.

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

Advantages

- Automatically closes the file
- Cleaner code
- Safer
- Prevents resource leaks

---

# 📖 Reading Methods

## 1️⃣ read()

Reads the **entire file**.

```python
with open("logs.txt", "r") as file:
    print(file.read())
```

### Best For

- Small files

---

## 2️⃣ readline()

Reads **one line at a time**.

```python
with open("logs.txt", "r") as file:
    print(file.readline())
```

Every call moves the file pointer to the next line.

---

## 3️⃣ readlines()

Reads the entire file and stores every line inside a list.

```python
with open("logs.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Output

```python
[
'Server Started\n',
'User Login\n',
'Database Connected\n'
]
```

---

## 4️⃣ Reading Using a for Loop ⭐ (Recommended)

```python
with open("logs.txt", "r") as file:

    for line in file:
        print(line.strip())
```

This method is memory-efficient because it reads one line at a time.

---

# 📊 Comparison

| Method | Returns | Best For |
|---------|----------|----------|
| `read()` | Entire file as one string | Small files |
| `readline()` | One line | Reading line-by-line |
| `readlines()` | List of lines | Small/Medium files |
| `for line in file` | One line at a time | Large files ⭐ |

---

# ✨ strip()

The `.strip()` method removes leading and trailing whitespace, including newline characters (`\n`).

Example

```python
print(line.strip())
```

Instead of

```text
Server Started

User Login

Database Connected
```

Output becomes

```text
Server Started
User Login
Database Connected
```

---

# 💼 Practical Programs

## Program 1

Created

```text
learning_log.txt
```

Operations

- Create File
- Write Data
- Append Data
- Read Data

---

## Program 2

Created

```text
logs.txt
```

Practiced

- `read()`
- `readline()`
- `readlines()`
- `for line in file`

---

# 📊 Time & Space Considerations

| Method | Memory Usage |
|----------|-------------|
| `read()` | High |
| `readline()` | Low |
| `readlines()` | High |
| `for line in file` | Very Low ⭐ |

---

# 🧠 Interview Questions

## What is File Handling?

File Handling is the process of creating, reading, writing, appending, and managing files to store data permanently.

---

## Difference between `"w"` and `"a"`?

| `"w"` | `"a"` |
|--------|-------|
| Overwrites existing content | Adds new content at the end |

---

## Difference between `"w"` and `"x"`?

| `"w"` | `"x"` |
|--------|-------|
| Creates or overwrites file | Creates only if the file doesn't exist |

---

## Difference between `read()`, `readline()`, and `readlines()`?

| Method | Returns |
|----------|---------|
| `read()` | Entire file |
| `readline()` | Single line |
| `readlines()` | List of lines |

---

## Why is `with open()` preferred?

Because it automatically closes the file after use, making the code safer and cleaner.

---

## Which method is recommended for reading large files?

```python
for line in file:
```

because it reads one line at a time without loading the entire file into memory.

---

## What does `.strip()` do?

Removes leading and trailing whitespace, including newline characters.

---

# 📁 Files Created

```text
Day_13/

├── file_handling.py
├── file_handling_output.png
├── file_read_methods.py
├── file_read_methods_output.png
├── learning_log.txt
├── logs.txt
└── README.md
```

---

# 🎯 Key Takeaways

- Files store data permanently.
- Different file modes are used for different operations.
- `with open()` is the recommended way to work with files.
- `read()` reads the entire file.
- `readline()` reads one line at a time.
- `readlines()` returns a list of lines.
- Reading files using a `for` loop is the most memory-efficient approach.
- `.strip()` removes unwanted newline characters.

---

# 📈 Python Progress

## Completed Topics

- Variables & Data Types
- Operators
- Type Conversion
- Functions
- Scope (LEGB)
- Closures
- Lambda Functions
- map()
- filter()
- List Comprehension
- Dictionary Comprehension
- zip()
- *args
- **kwargs
- Modules & Packages
- enumerate()
- any()
- all()
- File Handling

---

# 🚀 Next Topics

- Exception Handling (`try`, `except`, `finally`, `raise`)
- Object-Oriented Programming (OOP)
- Iterators & Generators
- Decorators
- JSON Handling
- Regular Expressions

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn Python, C++, DSA, Linux, Data Science, and AI step by step while documenting every concept with notes, examples, interview questions, and practical programs.

**Learn • Practice • Build • Repeat** 💻🔥