# 📚 Min Stack (LeetCode #155)

## 🟡 Difficulty

Medium

---

# 📖 Problem Statement

Design a stack that supports the following operations in **constant time O(1)**:

- `push(val)`
- `pop()`
- `top()`
- `getMin()`

The `getMin()` function should always return the minimum element currently present in the stack.

---

# Example

## Input

```text
["MinStack","push","push","push","getMin","pop","top","getMin"]

[[],[-2],[0],[-3],[],[],[],[]]
```

---

## Output

```text
[null,null,null,null,-3,null,0,-2]
```

---

## Explanation

```text
push(-2)

Stack
-2

Minimum = -2
```

---

```text
push(0)

Stack
-2
 0

Minimum = -2
```

---

```text
push(-3)

Stack
-2
 0
-3

Minimum = -3
```

---

```text
getMin()

Output

-3
```

---

```text
pop()

Stack

-2
 0
```

---

```text
top()

Output

0
```

---

```text
getMin()

Output

-2
```

---

# 🥉 Approach 1 : Brute Force

## Idea

Store all elements in a normal stack.

Whenever `getMin()` is called,

- Traverse the entire stack.
- Find the minimum element.

---

## Code

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = self.stack[0]

        for num in self.stack:
            if num < minimum:
                minimum = num

        return minimum
```

---

## Dry Run

Stack

```text
5
2
7
1
```

Calling

```text
getMin()
```

Checks

```
5

↓

2

↓

7

↓

1
```

Returns

```text
1
```

---

## Complexity

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| push | O(1) |
| pop | O(1) |
| top | O(1) |
| getMin | O(n) |

---

### Space Complexity

```text
O(n)
```

---

# 🏆 Approach 2 : Optimal (Two Stacks)

## Pattern

**Stack + Auxiliary Stack**

---

## Idea

Maintain two stacks.

### Main Stack

Stores every element.

```text
5
2
7
1
```

---

### Min Stack

Stores the minimum element at every stage.

```text
5
2
2
1
```

Whenever a value is pushed,

store

```text
min(currentValue, previousMinimum)
```

Now,

the top of the Min Stack is always the minimum element.

---

## Code

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

---

# 🧠 Dry Run

Initially

```text
Stack      MinStack
```

---

Push 5

```text
Stack      MinStack

5          5
```

---

Push 2

```text
Stack      MinStack

5          5
2          2
```

---

Push 7

```text
Stack      MinStack

5          5
2          2
7          2
```

Minimum remains

```text
2
```

---

Push 1

```text
Stack      MinStack

5          5
2          2
7          2
1          1
```

---

Pop

```text
Stack      MinStack

5          5
2          2
7          2
```

Current minimum automatically becomes

```text
2
```

No searching required.

---

# 📊 Complexity Comparison

| Operation | Brute Force | Optimal |
|-----------|------------:|---------:|
| push | O(1) | O(1) |
| pop | O(1) | O(1) |
| top | O(1) | O(1) |
| getMin | O(n) | **O(1)** |

---

## Space Complexity

Both approaches

```text
O(n)
```

---

# 🧠 Why Two Stacks?

Suppose

```text
Stack

5
2
7
1
```

Current minimum

```text
1
```

Now

```text
pop()
```

If we store only one minimum variable,

we lose the previous minimum.

With another stack,

the previous minimum is already stored.

---

# 🌍 Real-World Applications

- Browser History
- Undo / Redo
- Expression Evaluation
- Text Editors
- Memory Management
- Operating Systems
- Financial Systems
- Database Transactions

---

# 🧠 Interview Questions

## What is a Min Stack?

A stack that supports retrieving the minimum element in constant time.

---

## Why can't we use one variable?

If the minimum element is removed,

we don't know what the previous minimum was.

---

## Why use another stack?

The auxiliary stack stores the minimum value corresponding to every element in the main stack.

---

## What pattern is used?

```text
Stack + Auxiliary Stack
```

---

## Why is the optimal solution O(1)?

Because the minimum element is always stored at the top of the Min Stack.

No traversal is required.

---

# 📁 Folder Structure

```text
Day_10/

├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 📚 Pattern Progress

| Pattern | Problems Solved |
|----------|-----------------|
| Hash Map | ✅ |
| Stack | ✅ Valid Parentheses |
| Stack Design | ✅ Min Stack |
| Greedy | ✅ |
| Hash Set | ✅ |
| Two Pointers | ✅ Valid Palindrome |
| Two Pointers | ✅ Is Subsequence |
| Frequency Counting | ✅ |

---

# 🎯 Key Takeaways

- A normal stack cannot efficiently return the minimum element.
- An auxiliary stack stores the minimum value at every level.
- Both stacks grow and shrink together.
- Every operation (`push`, `pop`, `top`, `getMin`) works in **O(1)** time.
- This problem introduces the important interview pattern of **designing data structures** rather than just solving algorithmic questions.

---

# 🚀 CodeEveryday Challenge

Part of my **Basics to Advance** journey where I solve one LeetCode problem every day, compare brute-force and optimal solutions, understand the underlying pattern, and document each problem with detailed explanations and complexity analysis.

**Think • Design • Optimize • Repeat** 🚀