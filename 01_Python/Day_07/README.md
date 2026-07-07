# 🐍 Python - Day 07

## 📅 Date
07 July 2026

---

# 📖 Introduction

Today I learned three important intermediate-level Python concepts:

- List Comprehensions
- Dictionary Comprehensions
- zip() Function

These features help write cleaner, shorter, and more Pythonic code. They are widely used in Data Science, Machine Learning, Backend Development, and Automation.

---

# 📚 Topics Covered

# 1️⃣ List Comprehensions

## Definition

A **List Comprehension** is a concise way to create a new list from an existing iterable using a single line of code.

---

## Syntax

```python
new_list = [expression for item in iterable]
```

---

## Example

```python
numbers = [1, 2, 3, 4, 5]

square = [num ** 2 for num in numbers]

print(square)
```

### Output

```text
[1, 4, 9, 16, 25]
```

---

## Filtering Example

```python
numbers = range(1, 11)

even = [num for num in numbers if num % 2 == 0]

print(even)
```

### Output

```text
[2, 4, 6, 8, 10]
```

---

## Conditional Expression

```python
marks = [35, 78, 91, 42, 88, 29, 67]

result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(result)
```

### Output

```text
['Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass']
```

---

# 2️⃣ Dictionary Comprehensions

## Definition

A **Dictionary Comprehension** is a concise way to create dictionaries using a single line of code.

---

## Syntax

```python
new_dict = {
    key: value
    for item in iterable
}
```

---

## Example

```python
numbers = [1, 2, 3, 4, 5]

square = {
    num: num ** 2
    for num in numbers
}

print(square)
```

### Output

```text
{
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
```

---

## Filtering Example

```python
courses = [
    "Python",
    "C++",
    "Machine Learning",
    "SQL"
]

course_lengths = {
    course: len(course)
    for course in courses
    if len(course) > 5
}

print(course_lengths)
```

### Output

```text
{
    'Python':6,
    'Machine Learning':16
}
```

---

# 3️⃣ zip() Function

## Definition

The **zip()** function combines two or more iterables element by element into a zip object (iterator).

---

## Syntax

```python
zip(iterable1, iterable2)
```

---

## Example 1

```python
names = ["Zaid", "Ali", "Sara"]

marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)
```

### Output

```text
Zaid 90
Ali 85
Sara 95
```

---

## Example 2

Convert into Dictionary

```python
student_ids = [101, 102, 103]

student_names = [
    "Zaid",
    "Ali",
    "Sara"
]

students = dict(zip(student_ids, student_names))

print(students)
```

### Output

```text
{
    101:'Zaid',
    102:'Ali',
    103:'Sara'
}
```

---

## Example 3

Using Three Iterables

```python
ids = [101,102,103]

names = ["Zaid","Ali","Sara"]

marks = [91,85,96]

result = list(zip(ids, names, marks))

print(result)
```

### Output

```text
[
    (101,'Zaid',91),
    (102,'Ali',85),
    (103,'Sara',96)
]
```

---

# 📂 Files

```text
Day_07/
│
├── list_comprehension.py
├── dictionary_comprehension.py
├── zip.py
└── README.md
```

---

# 🧠 Concepts Learned

## List Comprehensions

- Creating Lists
- Transforming Data
- Filtering Data
- Conditional Expressions

---

## Dictionary Comprehensions

- Creating Dictionaries
- Filtering Dictionary Entries
- Mapping Keys to Values

---

## zip()

- Combining Two Iterables
- Combining Three Iterables
- Creating Dictionaries using zip()
- Creating Lists of Tuples
- Working with Multiple Iterables

---

# 💼 Real-World Applications

### List Comprehensions

- Data Cleaning
- Feature Engineering
- Automation Scripts
- Data Transformation

---

### Dictionary Comprehensions

- API Responses
- JSON Processing
- Data Mapping
- Configuration Files

---

### zip()

- CSV File Processing
- Student Record Management
- Machine Learning Feature Mapping
- Combining Related Data
- Database Operations

---

# 📊 Comparison

| Feature | Output |
|---------|--------|
| List Comprehension | List |
| Dictionary Comprehension | Dictionary |
| zip() | Iterator (Zip Object) |

---

# 🎯 Key Takeaways

- List Comprehensions create lists in a clean and Pythonic way.
- Dictionary Comprehensions create key-value pairs efficiently.
- Filtering can be added using the `if` keyword.
- Conditional expressions allow transforming every element.
- `zip()` combines multiple iterables element by element.
- `dict(zip())` is a common way to create dictionaries.
- `zip()` stops when the shortest iterable ends.

---

# 🧠 Interview Questions

### What is a List Comprehension?

A concise way to create a new list from an iterable.

---

### Difference between Filtering and Conditional Expressions?

Filtering removes unwanted elements.

Conditional expressions transform every element.

---

### What is a Dictionary Comprehension?

A concise way to create dictionaries using key-value pairs.

---

### What does zip() return?

A zip object (iterator).

---

### What happens if iterables have different lengths?

`zip()` stops at the shortest iterable.

---

### Why use dict(zip())?

It quickly converts two related iterables into a dictionary.

---

# 📈 Progress

## Python Roadmap

### Day 2 ✅

- Functions
- Scope (LEGB)
- Global Keyword

### Day 3 ✅

- Nested Functions
- Enclosing Scope
- nonlocal
- Closures
- First-Class Functions

### Day 5 ✅

- Lambda Functions
- map()
- filter()

### Day 7 ✅

- List Comprehensions
- Dictionary Comprehensions
- zip()

---

# 🚀 Next Topics

- enumerate()
- *args
- **kwargs
- Modules & Packages
- File Handling
- Exception Handling
- Iterators
- Generators
- Decorators
- Object-Oriented Programming (OOP)

---

# 🚀 CodeEveryday Challenge

Building strong Python fundamentals one concept at a time while progressing towards becoming an AI/ML Engineer & Software Developer.

Learning • Building • Practicing • Growing 🚀