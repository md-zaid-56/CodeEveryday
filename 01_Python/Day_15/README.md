# 🐍 Python - Day 15

## 📅 Date

15 July 2026

---

# 📚 Topics Covered

- sorted()
- reversed()
- sum()

---

# 1️⃣ sorted()

Returns a new sorted list without modifying the original list.

## Example

```python
numbers = [5,2,9,1]

print(sorted(numbers))
```

Output

```
[1,2,5,9]
```

### Time Complexity

```
O(n log n)
```

---

# 2️⃣ reversed()

Returns an iterator that accesses the list in reverse order.

```python
numbers = [1,2,3]

print(list(reversed(numbers)))
```

Output

```
[3,2,1]
```

### Time Complexity

```
O(n)
```

---

# 3️⃣ sum()

Calculates the total of all numeric elements.

```python
numbers = [5,2,9]

print(sum(numbers))
```

Output

```
16
```

### Time Complexity

```
O(n)
```

---

# 🌍 Real-World Applications

- Sorting Leaderboards
- Reversing Logs
- Calculating Sales
- Computing Marks
- Data Analysis

---

# 📁 Files

```
Day_15/

├── day_15.py
├── day_15_output.png
└── README.md
```

---

# 🎯 Key Takeaways

- `sorted()` creates a new sorted list.
- `reversed()` reverses the iteration order.
- `sum()` quickly totals numeric values.