# 🐍 Day 002 - Functions, Scope & Global Keyword

> Understanding how Python executes functions, manages memory, and resolves variables using namespaces.

---

# 🎯 Objective

Learn how Python executes functions internally, how variables are stored in different scopes, and how the `global` keyword affects namespace resolution.

---

# 📚 Topics Covered

- Functions
- Function Objects
- Parameters vs Arguments
- Return Statement
- Default Parameters
- Keyword Arguments
- Multiple Return Values
- `print()` vs `return()`
- Local Scope
- Global Scope
- Namespaces
- Function Frames
- LEGB Rule
- Shadowing
- `global` Keyword
- `globals()`
- `locals()`

---

# 🧠 Functions

A function is a reusable block of code that performs a specific task.

```python
def greet():
    print("Hello, Welcome to the Challenge!")
```

Calling the function:

```python
greet()
```

Output

```text
Hello, Welcome to the Challenge!
```

---

# 🔹 Functions are Objects

Everything in Python is an object, including functions.

```python
def greet():
    pass

print(type(greet))
```

Output

```text
<class 'function'>
```

---

# 🔹 Parameters vs Arguments

### Parameters

Variables defined in the function definition.

```python
def add(a, b):
    return a + b
```

Here `a` and `b` are **parameters**.

### Arguments

Values passed while calling the function.

```python
add(10, 20)
```

Here `10` and `20` are **arguments**.

---

# 🔹 Default Parameters

```python
def greet(name="Guest"):
    print(name)
```

```python
greet()
```

Output

```text
Guest
```

```python
greet("Zaid")
```

Output

```text
Zaid
```

---

# 🔹 Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=22, name="Zaid")
```

Output

```text
Zaid 22
```

---

# 🔹 Multiple Return Values

```python
def multiply_divide(a, b):
    return a * b, a / b
```

```python
mul, div = multiply_divide(10, 2)
```

Python actually returns a **tuple**.

---

# 🔹 print() vs return()

### print()

Displays the value on the console.

```python
def add(a, b):
    print(a + b)
```

### return()

Returns the value back to the caller.

```python
def add(a, b):
    return a + b
```

Using `return` makes the result reusable.

---

# 🌍 Scope

Scope defines where a variable can be accessed.

Python mainly uses:

- Local Scope
- Global Scope

---

# 🔹 Global Scope

Variables declared outside functions.

```python
x = 100
```

Accessible throughout the program.

---

# 🔹 Local Scope

Variables declared inside functions.

```python
def demo():
    y = 20
```

Accessible only inside that function.

---

# 🧠 Function Frames

Whenever a function is called, Python creates a **Function Frame**.

```
Global Namespace

↓

Function Call

↓

Function Frame

↓

Function Ends

↓

Frame Destroyed
```

All local variables are destroyed after the function finishes.

---

# 📦 Namespaces

Python stores variables inside namespaces.

Think of a namespace as a dictionary.

Global Namespace

```python
{
    "x":100,
    "name":"Zaid"
}
```

Local Namespace

```python
{
    "a":20,
    "b":30
}
```

---

# 🔍 LEGB Rule

Whenever Python searches for a variable, it follows this order:

```
L → Local

↓

E → Enclosing

↓

G → Global

↓

B → Built-in
```

The first matching variable is used.

---

# 🎭 Shadowing

A local variable can hide a global variable having the same name.

```python
x = 100

def demo():
    x = 50
    print(x)

demo()

print(x)
```

Output

```text
50
100
```

Both variables belong to different namespaces.

---

# 🌐 globals()

Returns the Global Namespace.

```python
print(globals())
```

---

# 🌐 locals()

Returns the Local Namespace.

```python
def demo():
    a = 10
    print(locals())
```

Output

```python
{'a':10}
```

---

# 🌍 global Keyword

Used when we want to modify a global variable inside a function.

```python
count = 0

def increment():
    global count
    count += 1
```

Without `global`, Python creates a local variable and raises an `UnboundLocalError`.

---

# Mutable Objects & global

Mutable objects can be modified without using `global`.

```python
numbers = [1,2,3]

def demo():
    numbers.append(4)
```

Output

```text
[1,2,3,4]
```

Reason:

`append()` modifies the existing object instead of creating a new one.

---

# ⚠️ Reassignment Requires global

```python
numbers = numbers + [4]
```

This creates a new object.

Since assignment occurs, Python treats the variable as local unless `global` is used.

---

# 📊 Summary

| Topic | Learned |
|--------|---------|
| Functions | ✅ |
| Parameters & Arguments | ✅ |
| Default Parameters | ✅ |
| Keyword Arguments | ✅ |
| Multiple Returns | ✅ |
| print() vs return() | ✅ |
| Local Scope | ✅ |
| Global Scope | ✅ |
| Function Frames | ✅ |
| Namespaces | ✅ |
| LEGB Rule | ✅ |
| Shadowing | ✅ |
| globals() | ✅ |
| locals() | ✅ |
| global Keyword | ✅ |

---

# 💡 Key Takeaways

- Functions are first-class objects.
- Variables store references, not values.
- Every function call creates a new function frame.
- Local variables are destroyed after function execution.
- Python searches variables using the LEGB Rule.
- `global` allows reassignment of global variables.
- Mutable objects can often be modified without using `global`.
- `append()` modifies an object, whereas `=` creates a new reference.

---

# 🎯 Interview Questions

### Q1. Difference between Parameters and Arguments?

Parameters are variables in the function definition, while arguments are the values passed during the function call.

---

### Q2. Difference between `print()` and `return()`?

`print()` displays the output.

`return` sends the value back to the caller.

---

### Q3. What is the LEGB Rule?

Python searches variables in this order:

Local → Enclosing → Global → Built-in

---

### Q4. What is Shadowing?

A local variable hides a global variable having the same name.

---

### Q5. Why does `x += 1` require `global`?

Because it performs reassignment (`x = x + 1`), making Python treat `x` as a local variable.

---

### Q6. Why doesn't `append()` require `global`?

Because it modifies the existing object rather than creating a new reference.

---

# 📂 Files

```
Day_002/
│── README.md
│── function.py
│── scope.py
│── global_keyword.py
```

---

# 📅 Day 2 Status

✅ Functions  
✅ Scope  
✅ LEGB Rule  
✅ Namespaces  
✅ Shadowing  
✅ `global` Keyword  

**Next Topic:** Nested Functions, `nonlocal`, Closures & Lambda Functions.