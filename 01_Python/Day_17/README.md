# 🐍 Python - Day 17

## 📅 Date

17 July 2026

---

# 📖 Introduction

Today I started learning one of the most important concepts in programming:

# Object-Oriented Programming (OOP)

Instead of writing programs using only variables and functions, OOP allows us to model real-world entities as **objects** that contain both **data (attributes)** and **behavior (methods)**.

This is the programming paradigm used in most real-world software applications, including web applications, machine learning libraries, games, and enterprise software.

---

# 📚 Topics Covered

- Classes
- Objects
- `__init__()` Constructor
- Instance Methods
- Object References
- Instance Variables
- Local Variables
- Memory Model (Basics)

---

# 1️⃣ Classes

## Definition

A **Class** is a blueprint used to create objects.

It defines what data an object should have and what actions it can perform.

---

## Real-Life Analogy

Think of a blueprint of a house.

One blueprint can build thousands of houses.

Similarly,

One class can create thousands of objects.

---

## Example

```python
class Student:
    pass
```

---

# 2️⃣ Objects

## Definition

An **Object** is an instance of a class.

Each object has its own identity and its own memory.

Example

```python
student1 = Student()
student2 = Student()
```

Although both belong to the same class, they are different objects.

---

# Memory Representation

```text
Class Student
      │
      ▼
 ┌────────────┐
 │ student1   │
 └────────────┘

 ┌────────────┐
 │ student2   │
 └────────────┘
```

---

# 3️⃣ Constructor (`__init__()`)

## Definition

`__init__()` is a special method that is automatically called immediately after an object is created.

Its purpose is to initialize the object's data.

---

## Syntax

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Creating an object

```python
student = Student("Zaid", 18)
```

---

# Important Interview Concept

Many beginners say

> "`__init__()` creates the object."

❌ This is incorrect.

The object is actually created by `__new__()`.

After the object is created,

Python automatically calls

```python
__init__()
```

to initialize it.

---

# Object Creation Flow

```text
Student()

      │

      ▼

__new__()

Creates Object

      │

      ▼

__init__()

Initializes Object

      │

      ▼

Ready to Use
```

---

# 4️⃣ The `self` Keyword

`self` represents the current object.

Example

```python
self.name = name
```

Left Side

```
Object Attribute
```

Right Side

```
Constructor Parameter
```

---

# Why do we use `self`?

Suppose

```python
student1 = Student("Zaid", 18)
```

Python internally behaves conceptually like:

```python
Student.__init__(student1, "Zaid", 18)
```

Therefore,

inside the constructor,

```python
self
```

refers to

```
student1
```

---

# 5️⃣ Instance Variables

Instance variables belong to an individual object.

Example

```python
self.name
self.age
self.course
```

Each object stores its own copy.

Example

```python
student1 = Student("Zaid",18)
student2 = Student("Luffy",56)
```

Memory

```text
student1

name = Zaid
age = 18

-------------------

student2

name = Luffy
age = 56
```

Changing

```python
student1.name
```

does not affect

```python
student2.name
```

because each object owns separate instance attributes.

---

# 6️⃣ Instance Methods

## Definition

Instance methods are functions inside a class that operate on a particular object.

Example

```python
class Employee:

    def display_info(self):
        print(self.name)
```

Calling

```python
emp.display_info()
```

internally behaves conceptually like

```python
Employee.display_info(emp)
```

Python automatically passes the object as the first argument.

---

# Real-World Example

A Bank Account

Data

- Holder Name
- Balance

Behavior

- Deposit
- Withdraw
- Check Balance

Objects should contain

```
State

+

Behavior
```

---

# 7️⃣ Object References

One of the most important concepts in Python.

Example

```python
student1 = Student("Zaid")

student2 = student1
```

Many beginners think Python creates another object.

❌ Wrong.

Python copies the reference.

Memory

```text
student1
      │
      ▼
+------------------+
| Student Object   |
| name = "Zaid"    |
+------------------+
      ▲
      │
student2
```

Both variables point to the same object.

Changing

```python
student2.name = "Luffy"
```

also changes

```python
student1.name
```

because both references point to the same object.

---

# 8️⃣ Local Variables vs Instance Variables

## Local Variable

```python
def give_raise(self, amount):

    increment = amount
```

- Exists only inside the function.
- Destroyed after the function finishes.

---

## Instance Variable

```python
self.salary
```

- Stored inside the object.
- Exists as long as the object exists.
- Can be accessed by every instance method.

---

# Common Beginner Mistakes

❌ Forgetting `self`

```python
def display():
```

Correct

```python
def display(self):
```

---

❌ Writing

```python
name = name
```

instead of

```python
self.name = name
```

---

❌ Thinking

```
student2 = student1
```

creates another object.

It only copies the reference.

---

# Memory Model

Creating

```python
emp = Employee("Zaid","AI",50000)
```

Memory

```text
emp

 │

 ▼

+----------------------+
| name = Zaid          |
| department = AI      |
| salary = 50000       |
+----------------------+
```

Methods modify this object's memory using

```python
self
```

---

# Real-World Applications

- Banking Systems
- Hospital Management
- Student Management
- Inventory Systems
- E-Commerce
- Machine Learning Libraries
- Web Frameworks

---

# 🧠 Interview Questions

## What is a Class?

A blueprint used to create objects.

---

## What is an Object?

An instance of a class.

---

## Does `__init__()` create the object?

❌ No.

It initializes an already created object.

Object creation is handled by `__new__()`.

---

## Why do we use `self`?

To refer to the current object whose method is being executed.

---

## What is an Instance Variable?

A variable that belongs to a specific object.

---

## Difference between Local Variable and Instance Variable?

| Local Variable | Instance Variable |
|----------------|-------------------|
| Lives inside a function | Lives inside an object |
| Temporary | Exists while the object exists |
| Cannot be accessed outside the function | Can be accessed through the object |

---

## What happens here?

```python
emp2 = emp1
```

No new object is created.

Only the reference is copied.

Both variables point to the same object.

---

## Why does

```python
self.salary += 5000
```

only change one employee?

Because

```python
self
```

references only the object on which the method was called.

---

# Files Created

```text
Day_17/

├── classes_objects.py
├── constructor.py
├── methods.py
└── README.md
```

---

# Key Takeaways

- Classes are blueprints.
- Objects are instances of classes.
- `__init__()` initializes an object.
- `self` refers to the current object.
- Instance variables belong to each object individually.
- Instance methods define an object's behavior.
- Variables store **references** to objects, not the objects themselves.
- Understanding references is essential for writing correct Python programs.

---

# 🚀 Progress

## Python Topics Completed

- Variables
- Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- `*args`
- `**kwargs`
- File Handling
- Exception Handling
- Modules
- Classes
- Objects
- Constructors (`__init__`)
- Instance Variables
- Instance Methods
- Object References

---

# 📚 Next Topics

- Encapsulation
- Access Modifiers
- Getters & Setters
- Inheritance
- Polymorphism
- Abstraction

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn Python, C++, DSA, Machine Learning, AI, Linux, and Software Engineering every day by building projects, solving coding problems, understanding concepts deeply, and documenting everything I learn.

**Learn • Practice • Build • Repeat** 🚀