# 💻 C++ - Day 17

## 📅 Date

17 July 2026

---

# 📖 Introduction

Today's focus was on understanding **how arrays behave in memory** and how they interact with functions.

Instead of simply learning array operations, I explored **how C++ passes arrays to functions**, why arrays **decay into pointers**, and how in-place algorithms modify the original memory.

I also learned one of the most important interview techniques:

> **The Two Pointer Technique**

which is used in many array and string problems.

---

# 📚 Topics Covered

- Passing Arrays to Functions
- Array Decay
- Pointer Basics
- `sizeof()` with Arrays
- Array Reversal
- Two Pointer Technique
- In-place Algorithms

---

# 1️⃣ Passing Arrays to Functions

## Definition

Instead of passing every element individually, C++ allows an entire array to be passed to a function.

Example

```cpp
void printArray(int arr[], int size)
{
    for(int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}
```

Calling

```cpp
int arr[] = {10,20,30,40,50};

printArray(arr,5);
```

---

# Why Do We Pass Arrays?

Without functions

```cpp
for(...)
{
    // Print
}

for(...)
{
    // Sum
}

for(...)
{
    // Find Maximum
}
```

The same loop gets repeated.

With functions

```cpp
printArray(arr,size);
sumArray(arr,size);
maxArray(arr,size);
```

Code becomes reusable, modular and easier to maintain.

---

# 🧠 Under the Hood

One of the most important C++ concepts.

When an array is passed to a function,

```cpp
printArray(arr,size);
```

the entire array is **NOT copied**.

Instead,

the array **decays into a pointer** to its first element.

Memory

```text
Main Function

arr

 │

 ▼

+----+----+----+----+----+
|10  |20  |30  |40  |50  |
+----+----+----+----+----+

          ▲

          │

Pointer received inside function
```

Therefore,

modifying

```cpp
arr[0]
```

inside the function changes the original array.

---

# Array Decay

When passed to a function,

```cpp
int arr[]
```

becomes

```cpp
int* arr
```

Therefore,

these are equivalent.

```cpp
void display(int arr[]);
```

```cpp
void display(int* arr);
```

---

# Why Do We Pass Size Separately?

Inside a function,

```cpp
sizeof(arr)
```

returns the size of the pointer,

not the array.

Example

Outside function

```cpp
sizeof(arr)
```

Output

```
20
```

Inside function

```cpp
sizeof(arr)
```

Output (64-bit system)

```
8
```

---

# Memory Explanation

Outside

```text
Array

10 20 30 40 50
```

Inside

```text
Pointer

↓

10
```

The function only knows the address.

It does not know how many elements exist.

Therefore,

the size must also be passed.

---

# Common Mistake

Many beginners think

```cpp
sum =+ arr[i];
```

means

```cpp
sum += arr[i];
```

❌ Wrong.

Correct

```cpp
sum += arr[i];
```

Equivalent to

```cpp
sum = sum + arr[i];
```

Whereas

```cpp
sum =+ arr[i];
```

means

```cpp
sum = (+arr[i]);
```

It simply assigns the positive value of the current element.

---

# 2️⃣ Array Reversal

## Definition

Array Reversal means rearranging the elements in reverse order.

Example

Original

```text
10 20 30 40 50
```

Reversed

```text
50 40 30 20 10
```

---

# Brute Force Approach

Create another array.

Example

```text
Original

10 20 30 40 50

↓

New Array

50 40 30 20 10
```

Complexity

```
Time  : O(n)

Space : O(n)
```

---

# Optimal Approach

Use Two Pointers.

---

# Two Pointer Technique

Initial

```text
L               R

10 20 30 40 50
```

Swap

```text
50 20 30 40 10
```

Move pointers

```text
   L       R

50 20 30 40 10
```

Swap

```text
50 40 30 20 10
```

Pointers meet.

Done.

---

# Algorithm

```cpp
left = 0;

right = size - 1;

while(left < right)
{
    swap(arr[left], arr[right]);

    left++;

    right--;
}
```

---

# Why `left < right`?

Correct

```cpp
while(left < right)
```

Incorrect

```cpp
while(left != right)
```

Reason

For even-sized arrays,

`left != right`

may continue even after pointers cross each other, causing unnecessary operations or undefined behavior.

The correct stopping condition is

```cpp
left < right
```

---

# Time Complexity

| Operation | Complexity |
|-----------|-----------:|
| Reverse Array | O(n) |

---

# Space Complexity

```
O(1)
```

No extra array is created.

Only

- left
- right
- temp

are used.

---

# In-place Algorithm

An algorithm that modifies the original array without allocating another array.

Example

```cpp
reverseArray(arr,size);
```

The original array itself changes.

---

# Important Memory Concept

Suppose

```cpp
reverseArray(arr,5);
```

The function receives a pointer to the original array.

Therefore,

modifying

```cpp
arr[0]
```

inside the function modifies

```cpp
arr[0]
```

inside `main()` as well.

No copying occurs.

---

# Real-World Applications

## Passing Arrays

- Data Processing
- Banking Systems
- Scientific Computing
- Image Processing
- Machine Learning

---

## Array Reversal

- Music Playlist Reversal
- Image Rotation
- Audio Processing
- Undo / Redo Systems
- Reverse Strings
- Palindrome Problems

---

# 🧠 Interview Questions

## Why do arrays decay into pointers?

To efficiently pass the address of the first element instead of copying the entire array.

---

## Is

```cpp
void display(int arr[])
```

different from

```cpp
void display(int* arr)
```

❌ No.

They are equivalent in function parameters.

---

## Why does

```cpp
sizeof(arr)
```

change inside a function?

Because `arr` becomes a pointer inside the function.

---

## Why is

```cpp
while(left < right)
```

used instead of

```cpp
while(left != right)
```

To prevent pointers from crossing each other and accessing invalid memory.

---

## What is an In-place Algorithm?

An algorithm that modifies the original data structure without using significant additional memory.

---

## Why is Two Pointer Technique efficient?

Each iteration places **two elements** in their correct positions, reducing unnecessary work.

---

# Common Beginner Mistakes

❌ Using

```cpp
sum =+ arr[i];
```

instead of

```cpp
sum += arr[i];
```

---

❌ Hardcoding

```cpp
printArray(arr,5);
```

instead of

```cpp
printArray(arr,size);
```

---

❌ Using

```cpp
while(left != right)
```

instead of

```cpp
while(left < right)
```

---

❌ Thinking arrays are copied into functions.

Only the pointer is passed.

---

# Files Created

```text
Day_17/

├── passing_arrays.cpp
├── reverse_array.cpp
└── README.md
```

---

# Key Takeaways

- Arrays decay into pointers when passed to functions.
- Functions modify the original array because they receive its address.
- `sizeof()` behaves differently inside and outside functions.
- Two Pointer Technique is one of the most important interview patterns.
- Array reversal can be done efficiently in **O(n)** time and **O(1)** space.
- Small syntax mistakes like `=+` and `+=` can completely change program behavior.
- Thinking about memory and references is more valuable than memorizing syntax.

---

# 📈 C++ Progress

## Completed Topics

- Variables
- Data Types
- Operators
- Input / Output
- Conditional Statements
- Loops
- break
- continue
- Functions
- Function Overloading
- Recursion
- Arrays
- User Input in Arrays
- Sum & Average
- Maximum & Minimum
- Linear Search
- Binary Search
- Passing Arrays to Functions
- Array Decay
- Pointer Basics
- Array Reversal
- Two Pointer Technique

---

# 🚀 Next Topics

- Array Copy
- Multi-Dimensional Arrays
- Strings
- Character Arrays
- Vectors (STL)
- Sorting Algorithms

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn C++, Python, DSA, Machine Learning, AI, Linux, and Software Engineering every day by understanding concepts deeply, solving real interview problems, and documenting everything I learn.

**Learn • Practice • Build • Repeat** 🚀