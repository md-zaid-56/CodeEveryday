# 💻 C++ - Day 14

## 📅 Date

14 July 2026

---

# 📖 Introduction

Today I continued learning **Arrays in C++** by exploring common array operations that are frequently asked in coding interviews.

Instead of just storing values, I learned how to process data using arrays by taking user input, calculating totals, finding averages, and identifying the maximum and minimum values.

These operations form the foundation for many Data Structures and Algorithms (DSA) problems.

---

# 📚 Topics Covered

- Arrays (User Input)
- Displaying Array Elements
- Sum of Array
- Average of Array
- Maximum Element
- Minimum Element
- Difference Between Maximum and Minimum

---

# 1️⃣ User Input in Arrays

## Definition

Arrays allow us to store multiple values of the same data type in contiguous memory locations.

Instead of hardcoding values, users can enter them during program execution.

---

## Syntax

```cpp
int arr[5];

for(int i = 0; i < 5; i++)
{
    cin >> arr[i];
}
```

---

## Example

```cpp
int marks[5];

for(int i = 0; i < 5; i++)
{
    cout << "Enter Marks : ";
    cin >> marks[i];
}
```

---

## Time Complexity

```
O(n)
```

---

# 2️⃣ Displaying Array Elements

After storing values, they can be displayed using another loop.

```cpp
for(int i = 0; i < 5; i++)
{
    cout << arr[i] << endl;
}
```

---

## Time Complexity

```
O(n)
```

---

# 3️⃣ Sum of Array Elements

## Definition

The sum is calculated by adding every element of the array.

---

## Logic

Initialize

```cpp
int sum = 0;
```

Add every element

```cpp
sum += arr[i];
```

---

## Example

```cpp
int sum = 0;

for(int i = 0; i < 5; i++)
{
    sum += arr[i];
}
```

---

## Time Complexity

```
O(n)
```

---

# 4️⃣ Average of Array

Average is calculated using

```
Average = Sum / Number of Elements
```

---

## Example

```cpp
float average;

average = (float)sum / 5;
```

---

## Why Type Casting?

Without type casting,

```cpp
average = sum / 5;
```

C++ performs integer division.

Example

```
98 / 5 = 19
```

With type casting

```cpp
average = (float)sum / 5;
```

Output

```
19.6
```

---

# 5️⃣ Finding Maximum Element

## Definition

Traverse the array and compare every element with the current maximum.

---

## Logic

```cpp
int maximum = arr[0];

for(int i = 1; i < 5; i++)
{
    if(arr[i] > maximum)
    {
        maximum = arr[i];
    }
}
```

---

# 6️⃣ Finding Minimum Element

## Definition

Traverse the array and compare every element with the current minimum.

---

## Logic

```cpp
int minimum = arr[0];

for(int i = 1; i < 5; i++)
{
    if(arr[i] < minimum)
    {
        minimum = arr[i];
    }
}
```

---

# 7️⃣ Difference Between Maximum and Minimum

Once maximum and minimum are known,

```cpp
difference = maximum - minimum;
```

Example

```
Maximum = 100
Minimum = -2

Difference = 102
```

---

# 🌍 Real-World Applications

Arrays are used in:

- Student Result Systems
- Employee Salary Records
- Sales Reports
- Temperature Monitoring
- Sensor Data
- Financial Applications
- Inventory Systems

---

# 📊 Time Complexity Summary

| Operation | Complexity |
|------------|------------|
| User Input | O(n) |
| Display Array | O(n) |
| Sum | O(n) |
| Average | O(1) (after sum) |
| Maximum | O(n) |
| Minimum | O(n) |

---

# 📦 Space Complexity

All operations use only a few additional variables.

```
O(1)
```

---

# 🧠 Interview Questions

## Why do arrays start from index 0?

Because array indexing is based on memory offsets from the first element.

---

## Why initialize maximum and minimum with arr[0]?

Using the first element ensures the algorithm works correctly for positive, negative, and mixed values.

---

## Why is average stored in float?

To preserve decimal values after division.

---

## Can sum be calculated while taking input?

Yes.

Example

```cpp
for(int i = 0; i < 5; i++)
{
    cin >> arr[i];
    sum += arr[i];
}
```

This avoids an additional loop.

---

## Why start searching for maximum/minimum from index 1?

Because index 0 has already been used to initialize both variables.

---

# ⚠️ Common Mistakes

❌ Using

```cpp
int maximum = 0;
```

Fails for negative numbers.

Always use

```cpp
int maximum = arr[0];
```

---

❌ Forgetting type casting

```cpp
average = sum / 5;
```

Correct

```cpp
average = (float)sum / 5;
```

---

❌ Using

```cpp
i <= 5
```

Correct

```cpp
i < 5
```

to avoid accessing memory outside the array.

---

# 📁 Files

```text
Day_14/

├── user_input_array.cpp
├── user_input_array_output.png
├── sum_average.cpp
├── sum_average_output.png
├── min_max.cpp
├── min_max_output.png
└── README.md
```

---

# 🎯 Key Takeaways

- Arrays store multiple values of the same data type.
- Loops make array traversal simple.
- Sum and average are basic array operations.
- Maximum and minimum are found using comparisons.
- Initializing maximum and minimum with the first element prevents logical errors.
- Arrays are the foundation of many DSA problems.

---

# 📈 Progress

## Completed C++ Topics

- Variables
- Data Types
- Input / Output
- Operators
- Type Casting
- Conditions
- Loops
- break
- continue
- Pattern Printing
- Functions
- Function Overloading
- Recursion
- Arrays (Basics)
- User Input in Arrays
- Displaying Arrays
- Sum of Array
- Average Calculation
- Maximum & Minimum Element

---

# 🚀 Next Topic

- Linear Search
- Binary Search (Introduction)
- Multi-dimensional Arrays

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn C++, Python, DSA, Linux, Data Science, Machine Learning, and AI step by step while documenting every concept with notes, code, interview questions, and practical examples.

**Learn • Practice • Build • Repeat** 🚀