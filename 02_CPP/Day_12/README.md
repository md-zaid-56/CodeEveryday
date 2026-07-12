# 💻 C++ - Day 12

## 📅 Date

12 July 2026

---

# 📖 Topic

## Arrays (Introduction)

An array is a collection of elements of the same data type stored in contiguous memory locations.

Instead of creating multiple variables,

```cpp
int a = 10;
int b = 20;
int c = 30;
```

we use

```cpp
int arr[3] = {10,20,30};
```

---

# Syntax

```cpp
data_type array_name[size];
```

Example

```cpp
int marks[5];
```

---

# Initialization

```cpp
int marks[5] = {78,85,92,67,88};
```

---

# Accessing Elements

```cpp
marks[0]
marks[1]
marks[2]
```

Arrays start from index **0**.

---

# Traversing an Array

```cpp
for(int i=0;i<5;i++)
{
    cout<<marks[i];
}
```

---

# Complexity

Access by Index

```
O(1)
```

Traversal

```
O(n)
```

---

# Real-World Applications

- Student Marks
- Employee IDs
- Monthly Sales
- Sensor Readings

---

# Key Takeaways

- Stores similar data together.
- Fixed size.
- Fast index access.
- Foundation of many data structures.

---

# Files

```text
Day_12/
├── arrays.cpp
└── README.md
```