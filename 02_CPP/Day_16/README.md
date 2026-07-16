# 💻 C++ - Day 16

## 📅 Date

16 July 2026

---

# 📖 Introduction

Today I learned two of the most important searching algorithms in Computer Science:

- Linear Search
- Binary Search

Searching is one of the fundamental operations in programming. Choosing the right searching algorithm can significantly improve application performance.

I also learned why **Binary Search requires a sorted array** and how it reduces the search space by half after every comparison.

---

# 📚 Topics Covered

- Linear Search
- Binary Search
- Time Complexity Comparison
- Best, Average & Worst Cases

---

# 1️⃣ Linear Search

## Definition

Linear Search checks every element of an array one by one until the target element is found or the array ends.

It is the simplest searching algorithm.

---

## Algorithm

1. Start from index 0.
2. Compare the current element with the target.
3. If they are equal, return the index.
4. Otherwise, move to the next element.
5. If the loop finishes, the element is not present.

---

## Example

Array

```text
22 18 67 24 68
```

Target

```text
18
```

Search Process

```
22 ❌
18 ✅
```

Result

```
Index = 1
Position = 2
```

---

## C++ Logic

```cpp
for(int i = 0; i < size; i++)
{
    if(arr[i] == target)
    {
        found = true;
        break;
    }
}
```

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

---

## Space Complexity

```
O(1)
```

---

# Advantages

- Works on sorted arrays.
- Works on unsorted arrays.
- Very easy to implement.

---

# Disadvantages

- Slow for large datasets.
- May check every element.

---

# 2️⃣ Binary Search

## Definition

Binary Search searches only on **sorted arrays**.

Instead of checking every element, it repeatedly divides the search space into two halves.

---

# Why Sorted Array?

Suppose

```
10 20 30 40 50
```

Searching for

```
40
```

Middle

```
30
```

Since

```
40 > 30
```

the left half can safely be ignored.

Without sorting, this decision would be impossible.

---

# Algorithm

1. Set

```cpp
low = 0;
high = size - 1;
```

2. Find

```cpp
mid = (low + high) / 2;
```

3. Compare

```
arr[mid]
```

with target.

- Equal → Found
- Target greater → Search right half
- Target smaller → Search left half

Repeat until found or search space becomes empty.

---

# C++ Logic

```cpp
while(low <= high)
{
    int mid = (low + high) / 2;

    if(arr[mid] == target)
    {
        found = true;
        break;
    }
    else if(arr[mid] < target)
    {
        low = mid + 1;
    }
    else
    {
        high = mid - 1;
    }
}
```

---

# Better Mid Calculation

Instead of

```cpp
int mid = (low + high) / 2;
```

Professional code uses

```cpp
int mid = low + (high - low) / 2;
```

This prevents integer overflow when working with very large arrays.

---

# Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

---

# Space Complexity

```
O(1)
```

---

# Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|----------|---------------|---------------|
| Sorted Array Required | ❌ No | ✅ Yes |
| Best Case | O(1) | O(1) |
| Worst Case | O(n) | O(log n) |
| Easy to Implement | ✅ | ✅ |
| Suitable for Large Data | ❌ | ✅ |

---

# 🌍 Real-World Applications

## Linear Search

- Student Record Search
- Small Inventory Systems
- Contact Lists
- Attendance Records

---

## Binary Search

- Dictionary Search
- Search Engines
- Database Indexing
- Phone Contacts
- Gaming Leaderboards
- E-commerce Search

---

# 🧠 Interview Questions

## When should we use Linear Search?

When the data is unsorted or the dataset is small.

---

## Why does Binary Search require a sorted array?

Because it decides which half to discard using the ordering of elements.

---

## Why is Binary Search faster?

Because after every comparison it removes half of the remaining search space.

---

## Which search works on unsorted arrays?

Linear Search.

---

## Which search is preferred for large datasets?

Binary Search.

---

## Why use `break` after finding the target?

Because continuing the search is unnecessary once the target has been found.

---

## Why is

```cpp
low + (high - low) / 2
```

better than

```cpp
(low + high) / 2
```

It avoids integer overflow.

---

# ⚠️ Common Mistakes

❌ Using Binary Search on an unsorted array.

---

❌ Forgetting to update

```cpp
low
```

or

```cpp
high
```

inside the loop.

---

❌ Forgetting

```cpp
break;
```

after finding the target.

---

❌ Printing

```
Element Found
```

multiple times because the loop continues.

---

# 📁 Files

```text
Day_16/

├── linear_search.cpp
├── linear_search_output.png
├── binary_search.cpp
├── binary_search_output.png
└── README.md
```

---

# 🎯 Key Takeaways

- Linear Search checks every element.
- Binary Search repeatedly halves the search space.
- Binary Search only works on sorted arrays.
- Binary Search is significantly faster for large datasets.
- Understanding time complexity helps in selecting the right algorithm.

---

# 📈 C++ Progress

## Completed Topics

- Variables
- Data Types
- Operators
- Input / Output
- Conditions
- Loops
- break
- continue
- Pattern Printing
- Functions
- Function Overloading
- Recursion
- Arrays
- User Input
- Display Arrays
- Sum of Array
- Average of Array
- Maximum Element
- Minimum Element
- Linear Search
- Binary Search

---

# 🚀 Next Topics

- Passing Arrays to Functions
- Multi-dimensional Arrays
- Vectors (STL)
- Strings in C++
- Sorting Algorithms

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I learn C++, Python, DSA, Linux, Data Science, Machine Learning, and AI by solving problems, documenting concepts, and building strong programming fundamentals every day.

**Learn • Practice • Build • Repeat** 🚀