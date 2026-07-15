# 📚 Running Sum of 1D Array (LeetCode #1480)

## 🟢 Difficulty

Easy

---

# Pattern

✅ Prefix Sum

---

# Problem

Return the running sum of an array.

Example

Input

```
[1,2,3,4]
```

Output

```
[1,3,6,10]
```

---

# Brute Force

For every index, calculate the sum from the beginning.

### Time Complexity

```
O(n²)
```

### Space Complexity

```
O(n)
```

---

# Optimal

Update the array in-place.

```python
nums[i] += nums[i-1]
```

### Time Complexity

```
O(n)
```

### Space Complexity

```
O(1)
```

---

# 🌍 Applications

- Prefix Sum
- Financial Analysis
- Cumulative Sales
- Running Statistics

---

# 📁 Files

```
Day_15/

├── brute.py
├── optimal.py
├── optimal_solution.png
└── README.md
```

---

# 🎯 Key Takeaways

- Introduction to Prefix Sum.
- Optimize repeated summation.
- In-place array modification.