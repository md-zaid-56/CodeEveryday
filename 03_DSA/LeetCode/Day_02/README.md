# 🧩 Day 002 - Valid Parentheses

> Solving LeetCode #20 using a Stack and understanding why Stack is the ideal data structure for bracket matching.

---

# 📌 Problem

Given a string `s` containing only the characters:

- `(`
- `)`
- `{`
- `}`
- `[`
- `]`

Determine whether the input string is **valid**.

A string is considered valid if:

- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches the most recent unmatched opening bracket.

---

## Example 1

```text
Input:
s = "()"

Output:
true
```

---

## Example 2

```text
Input:
s = "()[]{}"

Output:
true
```

---

## Example 3

```text
Input:
s = "(]"

Output:
false
```

---

## Example 4

```text
Input:
s = "([)]"

Output:
false
```

---

## Example 5

```text
Input:
s = "{[]}"

Output:
true
```

---

# 🧠 Approach 1 — Brute Force (String Replacement)

## Idea

Repeatedly remove valid adjacent bracket pairs:

- `()`
- `{}`
- `[]`

If the string becomes empty, it is valid.

Otherwise, it is invalid.

---

## Algorithm

1. While the string contains `()`, `{}`, or `[]`
2. Remove all matching adjacent pairs.
3. Repeat until no more replacements are possible.
4. If the string is empty, return `True`.
5. Otherwise, return `False`.

---

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        while "()" in s or "{}" in s or "[]" in s:

            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        return s == ""
```

---

## Dry Run

Input

```text
({[]})
```

```
({[]})

↓

({})

↓

()

↓

""
```

String becomes empty.

Return

```text
True
```

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n²)** |
| Space Complexity | **O(n)** |

### Why?

- Each `replace()` scans the entire string.
- Multiple scans are required until no valid pairs remain.
- Every replacement creates a new string.

---

# ⚡ Approach 2 — Stack (Optimal)

## Idea

A Stack follows the **LIFO (Last In, First Out)** principle.

The most recently opened bracket must be closed first.

Therefore, Stack is the ideal data structure for this problem.

---

## Algorithm

1. Create an empty stack.
2. Traverse each character.
3. If it is an opening bracket:
   - Push it onto the stack.
4. If it is a closing bracket:
   - If the stack is empty → Invalid.
   - Pop the top element.
   - Check whether it matches the current closing bracket.
5. After processing all characters:
   - If the stack is empty → Valid.
   - Otherwise → Invalid.

---

## Dry Run

Input

```text
({[]})
```

| Character | Action | Stack |
|-----------|--------|-------|
| ( | Push | ( |
| { | Push | ( { |
| [ | Push | ( { [ |
| ] | Pop | ( { |
| } | Pop | ( |
| ) | Pop | Empty |

Stack becomes empty.

Return

```text
True
```

---

### Invalid Example

Input

```text
([)]
```

| Character | Action | Stack |
|-----------|--------|-------|
| ( | Push | ( |
| [ | Push | ( [ |
| ) | Mismatch ❌ | Return False |

---

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            if ch in "([{":
                stack.append(ch)

            else:

                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[ch]:
                    return False

        return len(stack) == 0
```

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

### Why?

- Each character is processed exactly once.
- Stack operations (`push` and `pop`) take **O(1)** time.
- In the worst case, all opening brackets are stored in the stack.

---

# 📊 Comparison

| Approach | Time | Space | Data Structure |
|----------|------|-------|----------------|
| Brute Force | O(n²) | O(n) | String |
| Stack | O(n) | O(n) | Stack |

---

# 📚 Key Concepts Learned

- Stack Data Structure
- LIFO (Last In, First Out)
- Push Operation
- Pop Operation
- Dictionary (HashMap)
- Time Complexity
- Space Complexity
- Bracket Matching

---

# 💡 Why Stack?

Suppose the input is:

```text
({[]})
```

The brackets are opened in this order:

```
(
{
[
```

But they must close in reverse order:

```
]
}
)
```

This behavior follows **LIFO**, making Stack the perfect choice.

---

# 🎯 Interview Takeaways

- Always identify the required data structure before writing code.
- Bracket matching problems are classic Stack problems.
- HashMaps simplify matching opening and closing brackets.
- Push opening brackets and validate closing brackets immediately.
- At the end, the stack must be empty for the string to be valid.

---

# 🎓 What I Learned

- How the Stack data structure works.
- Why LIFO is important.
- Difference between a brute-force solution and an optimized solution.
- How dictionaries help simplify bracket matching.
- How to analyze time and space complexity.

---

# 🏷️ Tags

`Stack` `String` `HashMap` `Python` `LeetCode` `Easy`

---

# 📂 Files

```
Day_002_Valid_Parentheses/
│── README.md
│── brute_force.py
│── stack_solution.py
```

---

## ✅ Status

**Problem Solved Successfully** 🎉

- ✔️ Brute Force Solution
- ✔️ Optimized Stack Solution
- ✔️ Time Complexity Analysis
- ✔️ Space Complexity Analysis
- ✔️ Dry Run Completed

---

**LeetCode Problem #20 Completed 🚀**