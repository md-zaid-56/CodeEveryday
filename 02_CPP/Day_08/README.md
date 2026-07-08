# 💻 C++ - Day 08

## 📅 Date
08 July 2026

---

# 📖 Introduction

Today I learned one of the most fundamental concepts in programming: **Loops**.

Loops allow us to execute a block of code repeatedly, making programs shorter, cleaner, and more efficient. I also learned how to control loops using `break` and `continue`, and applied nested loops to solve pattern printing problems.

---

# 📚 Topics Covered

- for Loop
- while Loop
- do-while Loop
- break Statement
- continue Statement
- Nested Loops
- Triangle Pattern
- Reverse Triangle Pattern

---

# 1️⃣ for Loop

## Definition

A **for loop** is used when the number of iterations is known beforehand.

---

## Syntax

```cpp
for(initialization; condition; update)
{
    // Code
}
```

---

## Example

```cpp
#include <iostream>
using namespace std;

int main()
{
    for(int i = 1; i <= 5; i++)
    {
        cout << i << endl;
    }

    return 0;
}
```

### Output

```text
1
2
3
4
5
```

---

## Use Cases

- Printing numbers
- Traversing arrays
- Running a task a fixed number of times
- Pattern printing

---

# 2️⃣ while Loop

## Definition

A **while loop** executes as long as the given condition remains true.

It is generally used when the number of iterations is unknown.

---

## Syntax

```cpp
while(condition)
{
    // Code
}
```

---

## Example

```cpp
int i = 1;

while(i <= 5)
{
    cout << i << endl;
    i++;
}
```

### Output

```text
1
2
3
4
5
```

---

## Use Cases

- Login systems
- Menu-driven programs
- User input validation
- Infinite loops with exit conditions

---

# 3️⃣ do-while Loop

## Definition

A **do-while loop** executes the code block at least once before checking the condition.

---

## Syntax

```cpp
do
{
    // Code
}
while(condition);
```

---

## Example

```cpp
int i = 1;

do
{
    cout << i << endl;
    i++;
}
while(i <= 5);
```

### Output

```text
1
2
3
4
5
```

---

## Difference Between while and do-while

| while | do-while |
|--------|-----------|
| Checks condition first | Executes once before checking |
| May execute zero times | Executes at least once |

---

# 4️⃣ break Statement

## Definition

The **break** statement immediately terminates the loop.

---

## Syntax

```cpp
break;
```

---

## Example

```cpp
for(int i = 1; i <= 5; i++)
{
    if(i == 3)
        break;

    cout << i << endl;
}
```

### Output

```text
1
2
```

---

## Real-World Uses

- Search operations
- Game Over condition
- ATM PIN verification
- Exit menu systems

---

# 5️⃣ continue Statement

## Definition

The **continue** statement skips the current iteration and proceeds to the next iteration.

---

## Syntax

```cpp
continue;
```

---

## Example

```cpp
for(int i = 1; i <= 5; i++)
{
    if(i == 3)
        continue;

    cout << i << endl;
}
```

### Output

```text
1
2
4
5
```

---

## Real-World Uses

- Skip invalid input
- Ignore banned users
- Skip weekends
- Filter unwanted records

---

# break vs continue

| break | continue |
|--------|-----------|
| Stops the loop | Skips only one iteration |
| Exits immediately | Continues with next iteration |

---

# 6️⃣ Pattern Printing

## Concept

Pattern printing is based on **Nested Loops**.

- Outer Loop → Controls rows
- Inner Loop → Controls columns

---

# Pattern 1 : Triangle

## Code

```cpp
for(int row = 1; row <= 5; row++)
{
    for(int col = 1; col <= row; col++)
    {
        cout << "*";
    }

    cout << endl;
}
```

### Output

```text
*
**
***
****
*****
```

---

# Pattern 2 : Reverse Triangle

## Code

```cpp
for(int row = 5; row >= 1; row--)
{
    for(int col = 1; col <= row; col++)
    {
        cout << "*";
    }

    cout << endl;
}
```

### Output

```text
*****
****
***
**
*
```

---

# 🧠 Logic Behind Pattern Printing

Every pattern can be solved using three questions:

1. How many rows?
2. How many columns?
3. What should be printed?

Once these questions are answered, the pattern becomes much easier to implement.

---

# 📂 Files

```text
Day_08/
│
├── loop.cpp
├── loop_output.png
├── break.cpp
├── break_output.png
├── pattern.cpp
├── pattern_output.png
└── README.md
```

---

# 📊 Comparison of Loops

| Feature | for | while | do-while |
|----------|:---:|:-----:|:---------:|
| Initialization | Inside loop | Before loop | Before loop |
| Condition Checked | Before | Before | After |
| Executes at least once | ❌ | ❌ | ✅ |
| Best Use | Fixed iterations | Unknown iterations | Execute at least once |

---

# 💼 Real-World Applications

### for Loop

- Employee IDs
- Student roll numbers
- Pattern printing
- Array traversal

---

### while Loop

- ATM systems
- Login authentication
- Menu-driven applications
- Sensor monitoring

---

### do-while Loop

- Calculator menu
- Game menu
- ATM menu
- User choice systems

---

### break

- Stop searching after finding data
- Exit loops on success
- Emergency stop conditions

---

### continue

- Skip invalid records
- Ignore unwanted values
- Continue processing remaining data

---

# 🧠 Interview Questions

### When should you use a for loop?

When the number of iterations is known.

---

### When should you use a while loop?

When the number of iterations depends on a condition.

---

### What is the main difference between while and do-while?

A do-while loop executes at least once.

---

### What is the purpose of break?

To immediately terminate a loop.

---

### What is the purpose of continue?

To skip the current iteration and move to the next one.

---

### Why are nested loops used in pattern printing?

The outer loop controls the rows, while the inner loop controls the number of columns (or characters) printed in each row.

---

# 🎯 Key Takeaways

- Loops eliminate repetitive code.
- Choose the appropriate loop based on the problem.
- `break` exits a loop immediately.
- `continue` skips only the current iteration.
- Pattern printing improves logical thinking using nested loops.
- Every pattern can be solved by analyzing rows, columns, and what changes in each row.

---

# 📈 Progress

## C++ Roadmap

### Day 1 ✅

- First C++ Program
- Variables
- Data Types
- Input & Output

### Day 6 ✅

- Operators
- Type Conversion
- Conditional Statements

### Day 8 ✅

- for Loop
- while Loop
- do-while Loop
- break
- continue
- Nested Loops
- Triangle Pattern
- Reverse Triangle Pattern

---

# 🚀 Next Topics

- Arrays
- Strings
- Functions
- Recursion
- Pointers
- Structures
- Object-Oriented Programming (OOP)
- STL (Vector, Stack, Queue, Map)

---

# 🚀 CodeEveryday Challenge

Building strong programming fundamentals by learning one concept every day while documenting every topic with code, explanations, and practical examples.

**Learn • Practice • Build • Repeat** 🚀