# 📈 Best Time to Buy and Sell Stock (LeetCode #121)

## 🟢 Difficulty
Easy

---

# 📖 Problem Statement

You are given an array `prices` where:

- `prices[i]` represents the price of a stock on the **i-th day**.

You want to maximize your profit by:

- Buying **one** stock.
- Selling **one** stock.
- You must buy before you sell.

If no profit can be made, return `0`.

---

## Example

### Input

```text
prices = [7,1,5,3,6,4]
```

### Output

```text
5
```

### Explanation

Buy on Day 2 at price **1**

Sell on Day 5 at price **6**

Profit

```text
6 - 1 = 5
```

---

# 🧠 Approach 1 : Brute Force

## Idea

Try every possible buying day with every possible selling day.

Calculate every profit and store the maximum.

---

## Algorithm

1. Pick one day as the buying day.
2. Try selling on every later day.
3. Calculate the profit.
4. Update the maximum profit.
5. Repeat for every buying day.

---

## Complexity

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

---

# 🚀 Approach 2 : Greedy (Optimal)

## Idea

Instead of checking every previous buying day, we only need to remember the **lowest stock price seen so far**.

For every price:

- Update the minimum buying price.
- Calculate the current profit.
- Update the maximum profit.

---

## Algorithm

1. Initialize

```python
min_price = float("inf")
max_profit = 0
```

2. Traverse the array once.

3. If the current price is smaller than `min_price`

- Update `min_price`.

Otherwise

- Calculate

```text
Current Profit = Current Price - Minimum Price
```

- Update `max_profit`.

4. Return `max_profit`.

---

# 🖥 Dry Run

Input

```text
[7,1,5,3,6,4]
```

| Price | Minimum Price | Current Profit | Maximum Profit |
|-------:|--------------:|---------------:|---------------:|
| 7 | 7 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | 5 | 5 |
| 4 | 1 | 3 | 5 |

Final Answer

```text
5
```

---

# 💻 Greedy Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            else:
                profit = price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit
```

---

# ⏱ Complexity Analysis

## Time Complexity

```text
O(n)
```

Only one traversal of the array.

---

## Space Complexity

```text
O(1)
```

Only two variables are used.

---

# 🔑 Key Concepts Learned

- Greedy Algorithm
- Running Minimum
- Single Pass Traversal
- Optimization
- Time Complexity Improvement
- Problem Solving Strategy

---

# 📊 Brute Force vs Greedy

| Feature | Brute Force | Greedy |
|----------|-------------|---------|
| Time Complexity | O(n²) | O(n) |
| Space Complexity | O(1) | O(1) |
| Nested Loops | ✅ | ❌ |
| Interview Preferred | ❌ | ✅ |

---

# 💡 Interview Takeaway

The brute-force solution compares every buying day with every selling day.

The optimized Greedy solution observes that **only the minimum stock price encountered so far is needed** to calculate the maximum possible profit for the current day.

This reduces the time complexity from **O(n²)** to **O(n)**.

---

# 📁 Folder Structure

```text
Best_Time_To_Buy_And_Sell_Stock/
│
├── brute.py
├── greedy.py
└── README.md
```

---

# 🎯 Skills Practiced

- Arrays
- Greedy Algorithms
- Optimization
- Time Complexity Analysis
- Interview Problem Solving

---

## 🚀 Part of my **#CodeEveryday - Basics to Advance Challenge**

Learning one concept, one problem, and one commit every single day.