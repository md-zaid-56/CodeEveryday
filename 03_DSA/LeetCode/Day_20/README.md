# 🧩 LeetCode #27 — Remove Element

## 📅 Day 20 — CodeEveryday Challenge

**Difficulty:** 🟢 Easy  
**Topics:** Array, Two Pointers  
**Pattern:** Read & Write Pointers  
**Approach:** In-place Array Modification

---

# 📖 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` **in-place**.

The order of the remaining elements may be changed.

Return the number of elements in `nums` which are not equal to `val`.

The first `k` elements of `nums` should contain the elements that are not equal to `val`.

---

# 🧪 Example 1

### Input

```text
nums = [3,2,2,3]

val = 3
```

### Output

```text
k = 2
```

The first `k` elements become:

```text
[2,2]
```

The remaining positions do not matter.

Conceptually:

```text
[2,2,_,_]
```

---

# 🧪 Example 2

### Input

```text
nums = [0,1,2,2,3,0,4,2]

val = 2
```

### Output

```text
k = 5
```

The first `k` elements can be:

```text
[0,1,3,0,4]
```

---

# 🥉 Approach 1 — Using Extra Array

## Idea

Create another list and store only the elements that are not equal to `val`.

Then copy those elements back into the original array.

---

## Code

```python
class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:

        result = []

        for num in nums:

            if num != val:

                result.append(num)

        for i in range(len(result)):

            nums[i] = result[i]

        return len(result)
```

---

# 🧠 How It Works

Suppose:

```text
nums = [3,2,2,3]

val = 3
```

Create:

```text
result = []
```

Process each element:

```text
3

3 == val

Ignore ❌
```

Next:

```text
2

2 != val

Keep ✅

result = [2]
```

Next:

```text
2

Keep ✅

result = [2,2]
```

Next:

```text
3

Ignore ❌
```

Finally:

```text
result = [2,2]
```

Copy the values back into `nums`.

Return:

```text
2
```

---

# ⏱️ Complexity — Extra Array Approach

### Time Complexity

```text
O(n)
```

We traverse the array and copy valid elements.

### Space Complexity

```text
O(n)
```

because we create another list.

---

# 🏆 Approach 2 — Two Pointers

The better approach modifies the original array directly.

We use two pointers:

```text
read

write
```

Each pointer has a different responsibility.

---

# 👀 Read Pointer

The `read` pointer scans every element.

Its job is to ask:

```text
Should this element be kept?
```

---

# ✍️ Write Pointer

The `write` pointer tells us:

```text
Where should the next valid element be placed?
```

---

# 💻 Optimal Code

```python
class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:

        write = 0

        for read in range(len(nums)):

            if nums[read] != val:

                nums[write] = nums[read]

                write += 1

        return write
```

---

# 🧠 Dry Run

Consider:

```text
nums = [3,2,2,3]

val = 3
```

Initially:

```text
write = 0
read  = 0
```

---

## Iteration 1

```text
nums[read] = 3
```

Compare:

```text
3 == val
```

Remove / Ignore ❌

`write` remains:

```text
0
```

---

## Iteration 2

```text
nums[read] = 2
```

Compare:

```text
2 != 3
```

Keep it ✅

Execute:

```python
nums[write] = nums[read]
```

So:

```text
nums[0] = 2
```

Array becomes conceptually:

```text
[2,2,2,3]
```

Then:

```text
write = 1
```

---

## Iteration 3

Current value:

```text
2
```

Keep it ✅

Write:

```text
nums[1] = 2
```

Then:

```text
write = 2
```

---

## Iteration 4

Current value:

```text
3
```

It matches `val`.

Ignore ❌

---

# ✅ Final Result

```text
write = 2
```

Therefore:

```text
k = 2
```

The useful part of the array is:

```text
nums[0:k]

[2,2]
```

---

# 🔥 The Core Pattern

This problem introduces an important Two Pointer variation:

```text
READ POINTER
     │
     │ Scans every element
     ▼
"Should I keep this?"
     │
     │ YES
     ▼
WRITE POINTER
     │
     │ Stores valid element
     ▼
Next Available Position
```

In simple words:

```text
READ → Explore

WRITE → Build
```

---

# 🤔 Why Don't We Delete Elements?

A beginner approach might use:

```python
nums.remove(val)
```

or:

```python
del nums[i]
```

while traversing.

This can create problems because deleting elements shifts the remaining elements.

Example:

```text
[2,2,3]
```

Delete index `0`:

```text
[2,3]
```

Now indexes have changed.

This can cause elements to be skipped if the loop is not handled carefully.

Instead, the read/write pointer technique avoids repeated deletions.

---

# 🚀 Why Is the Optimal Solution Better?

We don't create:

```python
result = []
```

Instead, we reuse the original array.

Therefore:

```text
Extra Array Approach

Time  → O(n)
Space → O(n)
```

versus:

```text
Two Pointer Approach

Time  → O(n)
Space → O(1)
```

---

# 📊 Complexity Comparison

| Approach | Time | Extra Space |
|---|---:|---:|
| Extra Array | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |

The Two Pointer solution satisfies the **in-place modification** requirement.

---

# 🧠 Important Interview Concept — In-place

An in-place algorithm modifies the existing data structure without creating another data structure proportional to the input size.

Here:

```python
nums[write] = nums[read]
```

reuses the original `nums` array.

Therefore, the extra space complexity is:

```text
O(1)
```

---

# 🔥 Interview Question 1

Why does `write` start at `0`?

Because index `0` is initially the first available position where a valid element can be stored.

Every time we find a valid element:

```python
write += 1
```

So `write` always points to the next available position.

---

# 🔥 Interview Question 2

Why do we return:

```python
write
```

?

Because `write` also represents the number of valid elements stored.

Suppose:

```text
write = 5
```

Then valid elements occupy:

```text
Index:

0
1
2
3
4
```

That means:

```text
5 valid elements
```

---

# 🔥 Interview Question 3

Is this safe?

```python
nums[write] = nums[read]
```

when:

```text
write == read
```

Yes.

For example:

```python
nums[0] = nums[0]
```

This simply assigns the same value back to the same position.

Nothing is corrupted.

---

# 🆚 LeetCode #26 vs #27

Both problems use Two Pointers, but the purpose is different.

| #26 Remove Duplicates | #27 Remove Element |
|---|---|
| Removes duplicate values | Removes a specific value |
| Input must be sorted | Sorting is not required |
| Detects new unique values | Keeps values not equal to `val` |
| Uses two pointers | Uses read/write pointers |
| In-place | In-place |
| O(n) optimal time | O(n) optimal time |
| O(1) extra space | O(1) extra space |

This shows an important DSA lesson:

> The same pattern can solve different problems when the responsibilities of the pointers change.

---

# 🌍 Real-World Thinking

The Read/Write Pointer pattern can be thought of as a **filtering system**.

Suppose:

```text
Incoming Data
      ↓
READ POINTER
      ↓
Check Condition
   ↙       ↘
Reject     Accept
             ↓
        WRITE POINTER
             ↓
       Store Valid Data
```

Similar ideas appear when:

- Filtering invalid records
- Removing unwanted values
- Cleaning datasets
- Compressing arrays
- Processing streams of data

---

# 🎯 Pattern Recognition

Don't memorize this as only:

```text
"Remove Element Problem"
```

Remember the reusable pattern:

```text
Read Pointer
     ↓
Inspect Element
     ↓
Does it satisfy condition?
     ↓
    YES
     ↓
Write Pointer
     ↓
Store Element
     ↓
Move Write Pointer
```

This pattern appears in many array and string problems.

---

# ⚠️ Common Mistakes

### ❌ Creating another array when in-place modification is required

```python
result = []
```

Works logically, but uses:

```text
O(n)
```

extra space.

---

### ❌ Incrementing `write` for every element

Wrong:

```python
for read in range(len(nums)):

    write += 1
```

`write` should move only when we keep a valid element.

---

### ❌ Returning `len(nums)`

The original array length does not change.

We must return the number of valid elements:

```python
return write
```

---

### ❌ Caring about elements after `k`

Suppose:

```text
k = 2
```

Only:

```text
nums[0:2]
```

matters.

The remaining values can be anything.

---

# 🧪 Interview Challenge

Given:

```python
nums = [0,1,2,2,3,0,4,2]

val = 2
```

Without running the program, determine:

```text
1. What is k?

2. What are the first k elements?

3. What happens to the remaining elements?

4. Why is nums[write] = nums[read]
   safe when read == write?

5. Why does this algorithm use O(1)
   extra space?
```

---

# 💡 Key Takeaways

- Two pointers do not always mean `left` and `right`.
- Pointers can have different responsibilities.
- `read` scans the input.
- `write` tracks where valid data should be stored.
- The original array can be reused instead of creating another array.
- In-place modification reduces extra space from `O(n)` to `O(1)`.
- Elements after the first `k` positions do not matter.
- Pattern recognition is more valuable than memorizing code.

---

# 📁 Files

```text
03_DSA/
└── Day_20/
    ├── brute.py
    ├── optimal.py
    ├── accepted_solution.png
    └── README.md
```

---

# 🚀 Day 20 — CodeEveryday

Today's focus was intentionally lighter:

```text
DSA
 ↓
LeetCode #27
 ↓
Brute Force
 ↓
Two Pointers
 ↓
Read / Write Pattern
 ↓
In-place Modification
 ↓
O(n) Time + O(1) Extra Space
```

The goal isn't just:

```text
Accepted ✅
```

The real goal is:

```text
Understand the Problem
        ↓
Build a Simple Solution
        ↓
Find the Bottleneck
        ↓
Optimize
        ↓
Recognize the Pattern
        ↓
Explain WHY It Works
```

**Learn • Solve • Analyze • Improve • Repeat 🚀**