# 💻 C++ - Day 10

## 📅 Date

10 July 2026

---

# 📖 Introduction

Today I learned one of the most important building blocks of C++ programming.

Instead of writing everything inside the `main()` function, I learned how to organize programs using **Functions**, make code more flexible using **Function Overloading**, and solve problems recursively using **Recursion**.

These concepts are fundamental in software development and are frequently asked in technical interviews.

---

# 📚 Topics Covered

- Functions
- Function Declaration
- Function Definition
- Function Call
- Parameters & Arguments
- Return Type
- Function Overloading
- Compile-Time Polymorphism
- Recursion
- Base Case
- Recursive Call
- Call Stack

---

# 1️⃣ Functions

## Definition

A **Function** is a reusable block of code that performs a specific task.

Functions help organize code, improve readability, and avoid repetition.

---

## Why Do We Use Functions?

- Code Reusability
- Better Readability
- Easier Maintenance
- Modular Programming
- Reduced Code Duplication

---

## Syntax

```cpp
return_type function_name(parameters)
{
    // Function Body

    return value;
}
```

---

## Example

```cpp
#include <iostream>
using namespace std;

int square(int num)
{
    return num * num;
}

int main()
{
    cout << square(5);

    return 0;
}
```

### Output

```text
25
```

---

# Function Components

## Return Type

Specifies what type of value the function returns.

Examples

```cpp
int
float
double
char
bool
void
string
```

---

## Function Name

Should describe the work performed.

Good Examples

```cpp
calculateSalary()

withdraw()

findLargest()

calculateGrade()
```

---

## Parameters

Variables declared inside the function definition.

Example

```cpp
int add(int a, int b)
```

`a` and `b` are parameters.

---

## Arguments

Values passed while calling the function.

```cpp
add(10,20);
```

`10` and `20` are arguments.

---

# Types of Functions

### No Parameters, No Return Value

```cpp
void greet()
```

---

### Parameters, No Return Value

```cpp
void display(string name)
```

---

### No Parameters, Return Value

```cpp
int getAge()
```

---

### Parameters and Return Value

```cpp
int add(int a, int b)
```

This is the most commonly used function type.

---

# Practical Example

Created a function

```cpp
char calculateGrade(int marks)
```

Rules

| Marks | Grade |
|--------|--------|
| 90+ | A |
| 75 - 89 | B |
| 60 - 74 | C |
| 40 - 59 | D |
| Below 40 | F |

---

# 2️⃣ Function Overloading

## Definition

Function Overloading allows multiple functions to have the **same name** but **different parameter lists**.

The compiler automatically selects the correct function based on the arguments.

---

## Why Function Overloading?

Instead of creating

```text
addTwoNumbers()

addThreeNumbers()

addFloatNumbers()

addFourNumbers()
```

We simply write

```cpp
add(...)
```

with different parameter lists.

---

## Example

```cpp
int add(int a, int b)
{
    return a + b;
}

int add(int a, int b, int c)
{
    return a + b + c;
}
```

---

## Different Data Types

```cpp
int square(int x);

double square(double x);
```

---

## Invalid Overloading

Changing only the return type is **not** allowed.

```cpp
int add(int,int);

float add(int,int);
```

❌ Compile Error

---

# Compile-Time Polymorphism

Function Overloading is an example of

```text
Compile-Time Polymorphism
```

because the compiler decides which function to call before execution.

---

# Practical Example

Created overloaded functions

```cpp
calculateBonus(int fixedBonus)

calculateBonus(int salary, int performance)

calculateBonus(int salary, int performance, int experience)
```

---

# 3️⃣ Recursion

## Definition

Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

---

# Structure of Recursion

Every recursive function has two parts.

### Base Case

Stops recursion.

### Recursive Call

Calls the function again with a smaller problem.

---

## Syntax

```cpp
return_type function(parameters)
{
    if(base_case)
        return;

    return function(smaller_problem);
}
```

---

# Example

```cpp
void countdown(int n)
{
    if(n == 0)
        return;

    cout << n << " ";

    countdown(n - 1);
}
```

Output

```text
5 4 3 2 1
```

---

# Call Stack

Recursive calls are stored in the **Call Stack**.

```
function(5)

↓

function(4)

↓

function(3)

↓

function(2)

↓

function(1)

↓

Base Case

↓

Return

↓

Return

↓

Return
```

---

# Why Base Case is Important?

Without a Base Case

```cpp
hello()

↓

hello()

↓

hello()

↓

...
```

Program eventually crashes with

```text
Stack Overflow
```

---

# Factorial Example

```cpp
int factorial(int n)
{
    if(n == 1)
        return 1;

    return n * factorial(n - 1);
}
```

---

# Practical Examples

## Employee ID Generator

Recursive function

```cpp
printEmployeeID(1005)
```

Output

```text
Employee ID : 1005
Employee ID : 1004
Employee ID : 1003
Employee ID : 1002
Employee ID : 1001
```

---

## Recursive Sum

Function

```cpp
sum(5)
```

Output

```text
15
```

---

# 📊 Summary

| Concept | Purpose |
|----------|----------|
| Function | Reusable block of code |
| Parameters | Variables inside function definition |
| Arguments | Values passed during function call |
| Function Overloading | Same function name with different parameters |
| Compile-Time Polymorphism | Compiler chooses function before execution |
| Recursion | Function calling itself |
| Base Case | Stops recursion |
| Recursive Call | Solves smaller sub-problem |
| Call Stack | Stores active recursive calls |

---

# 🌍 Real-World Applications

## Functions

- ATM Software
- Banking Systems
- Student Management
- Hospital Management
- Inventory Systems

---

## Function Overloading

- Calculator
- Fee Calculator
- Bonus Calculator
- Payment Systems
- Mathematical Libraries

---

## Recursion

- Folder Traversal
- File Explorer
- Binary Search Trees
- Graph Algorithms
- Backtracking
- Dynamic Programming
- Tree Traversals

---

# 🧠 Interview Questions

## What is a Function?

A reusable block of code that performs a specific task.

---

## Difference between Parameters and Arguments?

| Parameters | Arguments |
|------------|-----------|
| Declared in function definition | Passed during function call |

---

## Why do we use Functions?

- Reusability
- Readability
- Easy Maintenance

---

## What is Function Overloading?

Using the same function name with different parameter lists.

---

## Can Function Overloading happen by changing only the return type?

No.

The compiler only checks parameter lists while selecting overloaded functions.

---

## What type of Polymorphism is Function Overloading?

Compile-Time Polymorphism.

---

## What is Recursion?

A function calling itself to solve a smaller version of the same problem.

---

## What are the two essential parts of Recursion?

- Base Case
- Recursive Call

---

## Why is Base Case important?

Without a Base Case, recursion never stops, causing a Stack Overflow.

---

## What is Call Stack?

A memory structure that stores active function calls during program execution.

---

# 📁 Files Created

```text
Day_10/

├── function.cpp
├── function_output.png
├── function_overloading.cpp
├── function_overloading_output.png
├── recursion.cpp
├── recursion_output.png
└── README.md
```

---

# 🎯 Key Takeaways

- Functions make programs modular and reusable.
- Parameters receive values, while arguments pass values.
- Function Overloading improves code readability by allowing multiple functions with the same name.
- Function Overloading is an example of Compile-Time Polymorphism.
- Every recursive function must have a Base Case.
- Recursion solves complex problems by breaking them into smaller sub-problems.
- Understanding the Call Stack is the key to mastering recursion.

---

# 📈 C++ Progress

## Day 01 ✅

- Variables
- Data Types
- Input / Output

---

## Day 06 ✅

- Operators
- Type Casting
- Conditions

---

## Day 08 ✅

- Loops
- break
- continue
- Pattern Printing

---

## Day 10 ✅

- Functions
- Parameters & Arguments
- Return Types
- Function Overloading
- Compile-Time Polymorphism
- Recursion
- Base Case
- Recursive Call
- Call Stack

---

# 🚀 Next Topics

- Arrays
- Strings
- Pointers
- References
- Dynamic Memory Allocation
- STL (Vector, Stack, Queue, Map)
- Object-Oriented Programming in C++

---

# 🚀 CodeEveryday Challenge

Learning C++ one concept at a time by understanding the fundamentals, solving real-world problems, writing clean code, and documenting every topic with notes and examples.

**Learn • Practice • Build • Repeat** 💻🔥