# 🧩 LeetCode #169 — Majority Element

## 📅 Day 23 — CodeEveryday

**Difficulty:** 🟢 Easy  
**Topics:** Array, Hash Map, Counting  
**Advanced Algorithm:** Boyer-Moore Voting Algorithm

---

# 📖 Problem Statement

Given an integer array:

```text
nums
```

return the:

```text
Majority Element
```

The majority element is the element that appears:

```text
more than n / 2 times
```

where:

```text
n = length of array
```

The problem guarantees that a majority element always exists.

---

# Example 1

```text
Input:

nums = [3,2,3]
```

Output:

```text
3
```

Because:

```text
3 appears 2 times

n = 3

n // 2 = 1

2 > 1
```

Therefore:

```text
3
```

---

# Example 2

```text
Input:

nums = [2,2,1,1,1,2,2]
```

Frequency:

```text
2 → 4 times

1 → 3 times
```

Array length:

```text
n = 7
```

Majority threshold:

```text
n // 2

7 // 2

= 3
```

For `2`:

```text
4 > 3
```

Therefore:

```text
Output = 2
```

---

# 🧠 What Does Majority Mean?

This is important.

Majority does NOT mean:

```text
Element with highest frequency
```

It specifically means:

```text
frequency > n / 2
```

Example:

```text
[1,1,2,2,3]
```

Frequencies:

```text
1 → 2

2 → 2

3 → 1
```

The highest frequency is:

```text
2
```

But:

```text
n = 5

n / 2 = 2.5
```

No element occurs more than half the array.

Therefore there is:

```text
NO majority element
```

However, LeetCode #169 guarantees that a majority element exists.

---

# 🥉 Approach 1 — Frequency Dictionary

We count how many times every number occurs.

```python
class Solution:

    def majorityElement(self, nums):

        count = {}

        for num in nums:

            if num in count:

                count[num] += 1

            else:

                count[num] = 1


        for num in count:

            if count[num] > len(nums) // 2:

                return num
```

---

# 🧠 How Dictionary Counting Works

Input:

```text
[2,2,1,1,1,2,2]
```

Initially:

```text
count = {}
```

Read first `2`:

```text
{
    2: 1
}
```

Read second `2`:

```text
{
    2: 2
}
```

Read `1`:

```text
{
    2: 2,
    1: 1
}
```

Continue:

```text
{
    2: 4,
    1: 3
}
```

Now check:

```text
count[num] > len(nums) // 2
```

For `2`:

```text
4 > 3

TRUE
```

Return:

```text
2
```

---

# ⏱️ Complexity — Dictionary Approach

We traverse the array:

```text
O(n)
```

We also store frequencies:

```text
O(n)
```

Therefore:

```text
Time Complexity:

O(n)


Space Complexity:

O(n)
```

Can we keep:

```text
O(n) Time
```

but reduce space to:

```text
O(1)?
```

Yes.

🔥 Boyer-Moore Voting Algorithm.

---

# 🚀 Approach 2 — Boyer-Moore Voting Algorithm

This is the most interesting solution.

We maintain only two variables:

```text
candidate

count
```

Algorithm:

```text
count == 0

      ↓

Choose current number
as candidate


Current Number == Candidate

      ↓

count++


Current Number != Candidate

      ↓

count--
```

At the end:

```text
candidate = Majority Element
```

when the problem guarantees that a majority exists.

---

# 💻 Boyer-Moore Code

```python
class Solution:

    def majorityElement(self, nums):

        candidate = None

        count = 0


        for num in nums:

            if count == 0:

                candidate = num


            if num == candidate:

                count += 1

            else:

                count -= 1


        return candidate
```

---

# 🧠 Dry Run

Input:

```text
[2,2,1,1,1,2,2]
```

Start:

```text
candidate = None

count = 0
```

---

## Number = 2

Since:

```text
count == 0
```

Choose:

```text
candidate = 2
```

Same as candidate:

```text
count = 1
```

State:

```text
candidate = 2

count = 1
```

---

## Number = 2

Same candidate:

```text
count = 2
```

---

## Number = 1

Different:

```text
count = 1
```

---

## Number = 1

Different:

```text
count = 0
```

Now the votes for candidate `2` have been cancelled.

---

## Number = 1

Because:

```text
count == 0
```

New candidate:

```text
candidate = 1
```

Then:

```text
count = 1
```

---

## Number = 2

Different:

```text
count = 0
```

---

## Number = 2

Count is zero.

Choose:

```text
candidate = 2
```

Then:

```text
count = 1
```

Final:

```text
candidate = 2
```

Answer:

```text
2
```

---

# 🔥 Why Does Boyer-Moore Work?

Think about:

```text
CANCELLATION
```

Suppose the majority element is:

```text
M
```

Because it appears more than:

```text
n / 2
```

times, there are fewer non-majority elements than majority elements.

We can pair:

```text
One Majority Element

with

One Non-Majority Element
```

and cancel both.

Example:

```text
M X

cancel
```

Even after cancelling as many opposite elements as possible:

```text
some M must remain
```

because `M` originally appeared more than all other elements combined.

That surviving candidate is the majority.

---

# 🎯 Visual Intuition

Consider:

```text
[2,2,1,1,1,2,2]
```

Think of different elements cancelling each other:

```text
2 vs 1

cancel


2 vs 1

cancel
```

Remaining conceptually:

```text
1 vs 2

cancel
```

One:

```text
2
```

survives.

Therefore:

```text
Majority = 2
```

---

# 📊 Comparison

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |
| Sorting | O(n log n) | Depends |
| Boyer-Moore | O(n) | O(1) |

Best optimized approach:

```text
Boyer-Moore

Time  → O(n)

Space → O(1)
```

---

# ⚠️ Important Interview Trap

Consider:

```text
[1,2,3]
```

Run Boyer-Moore.

It will still produce some:

```text
candidate
```

But there is actually:

```text
NO majority
```

So does Boyer-Moore always guarantee the candidate is a majority?

```text
NO
```

It guarantees that only when:

```text
The problem guarantees
a majority element exists
```

LeetCode #169 provides that guarantee.

---

# 🔥 What If Majority Is NOT Guaranteed?

Then use two passes.

First:

```text
Find Candidate
```

using Boyer-Moore.

Second:

```text
Count Candidate Frequency
```

Then verify:

```text
frequency > n // 2
```

Example:

```python
candidate = None

count = 0

for num in nums:

    if count == 0:

        candidate = num

    if num == candidate:

        count += 1

    else:

        count -= 1


frequency = 0

for num in nums:

    if num == candidate:

        frequency += 1


if frequency > len(nums) // 2:

    return candidate

return -1
```

---

# 🧠 Interview Question

What is the difference between:

```text
Most Frequent Element
```

and:

```text
Majority Element
```

Answer:

```text
Most Frequent:

Appears more often than every
other individual element.


Majority:

Appears more than n / 2 times.
```

A most frequent element is not necessarily a majority element.

---

# 🔥 Interview Prediction

Consider:

```text
nums = [3,3,4,2,3,3,3]
```

Without using a dictionary, determine the majority.

Length:

```text
7
```

Threshold:

```text
7 // 2 = 3
```

Frequency of `3`:

```text
5
```

Therefore:

```text
5 > 3
```

Answer:

```text
3
```

---

# 🧠 Pattern Recognition

Do not memorize:

```text
LeetCode 169
=
Boyer-Moore
```

Understand the deeper idea:

```text
One element occurs
MORE THAN HALF
        ↓
Opposite elements can
cancel each other
        ↓
Majority cannot be
completely cancelled
        ↓
Candidate survives
```

This is why the algorithm works.

---

# 🎤 Strong Interview Explanation

Instead of saying:

> "If count becomes zero, I change candidate."

Explain:

> "The Boyer-Moore Voting Algorithm treats different elements as cancelling votes. Because the majority element occurs more than half the time, it cannot be completely cancelled by all non-majority elements. Therefore, when a majority is guaranteed, the final surviving candidate must be the majority element."

Then mention:

```text
Time  → O(n)

Space → O(1)
```

---

# 📁 Day 23 DSA Files

```text
03_DSA/
└── Day_23/
    └── 169_Majority_Element/
        ├── majority_element.py
        └── README.md
```

---

# 🚀 Day 23 DSA

Today:

```text
Frequency Counting
       ↓
Hash Map
       ↓
O(n) Time + O(n) Space
       ↓
Can Space Be Improved?
       ↓
Boyer-Moore Voting
       ↓
Candidate + Votes
       ↓
Cancellation Principle
       ↓
O(n) Time + O(1) Space
```

---

# 🎯 Key Takeaway

There are two levels to solving this problem:

```text
Level 1:

"I can count frequencies."


Level 2:

"I recognize that a > n/2 guarantee
allows cancellation and eliminates
the need to store frequencies."
```

That second level is where algorithmic thinking improves.

**Learn → Solve → Optimize → Understand WHY 🚀**