# 🐍 Python — Day 23

## 🚀 CodeEveryday | Basics to Advance

Day 23 focused on continuing Object-Oriented Programming in Python.

Today's main goal was to understand how a class can protect and control its internal state instead of allowing unrestricted modification.

---

# 📚 Topics Covered

1. Encapsulation
2. Public, Non-Public & Name-Mangled Attributes
3. Getters and Setters
4. `@property`
5. Property Setters
6. Validation using Properties
7. Name Mangling
8. Object State Protection

---

# 1️⃣ Encapsulation

Encapsulation means bundling:

```text
Data
+
Methods that operate on that data
+
Controlled access to object state
```

inside a class.

Example:

```python
class Product:

    def __init__(self, name, price, stock):

        self.name = name
        self.price = price
        self.stock = stock
```

The object contains its own state:

```text
Product Object
│
├── name
├── price
└── stock
```

But there is a problem.

External code can directly write:

```python
product1.stock = -5000
```

Python will allow this if `stock` is a normal public attribute.

This can put the object into an invalid state.

---

# 🧠 Object Invariant

An invariant is a rule that should always remain true for an object's valid state.

For example:

```text
Product:

stock >= 0
```

For an employee:

```text
salary > 0
```

For a student:

```text
0 <= marks <= 100
```

For a bank account:

```text
withdrawal <= available balance
```

A well-designed class should try to protect these rules.

---

# 🌍 Real-World Example

Consider a banking system.

We should not allow external code to directly manipulate:

```text
balance
```

Instead, operations should happen through controlled methods:

```text
deposit()
withdraw()
transfer()
```

Flow:

```text
User Request
     ↓
Controlled Method
     ↓
Validation
     ↓
Business Rules
     ↓
Modify Internal State
```

This is one of the main purposes of encapsulation.

---

# 2️⃣ Public Attributes

A normal attribute is publicly accessible.

Example:

```python
class Product:

    def __init__(self, name):

        self.name = name
```

Outside the class:

```python
product1.name
```

works.

Modification also works:

```python
product1.name = "PC"
```

Therefore:

```text
self.name

      ↓

Public Attribute

      ↓

Can normally be accessed
and modified externally
```

Public attributes are not automatically bad.

They are useful when unrestricted access is acceptable.

---

# 3️⃣ Single Underscore `_attribute`

Example:

```python
self._price = price
```

This is commonly described as a protected attribute, but Python does not actually enforce protected access here.

Outside the class:

```python
print(product1._price)
```

still works.

Modification also works:

```python
product1._price = 5000
```

Therefore:

```text
_price

   ↓

Non-Public Convention

   ↓

"Internal use — avoid accessing directly"

   ↓

But Python does NOT block access
```

A more accurate interview explanation is:

> A single leading underscore indicates that an attribute is intended for internal or non-public use by convention, but Python does not enforce access restrictions on it.

---

# 4️⃣ Double Underscore `__attribute`

Example:

```python
self.__stock = stock
```

Trying:

```python
product1.__stock
```

does not directly access the attribute created inside the class.

Python applies:

```text
NAME MANGLING
```

---

# 🔥 Name Mangling

Suppose:

```python
class Product:

    def __init__(self):

        self.__stock = 10
```

Python approximately transforms:

```text
__stock
```

into:

```text
_Product__stock
```

Conceptually:

```text
self.__stock

       ↓

Name Mangling

       ↓

self._Product__stock
```

Therefore, the object's internal namespace contains something similar to:

```text
_Product__stock
```

rather than simply:

```text
__stock
```

---

# 🧪 Important Experiment

Suppose:

```python
product1.__stock = 50
```

This does NOT necessarily modify the original name-mangled attribute.

The object may conceptually contain:

```text
_Product__stock = 10

__stock = 50
```

These are two different attribute names.

The method inside `Product` using:

```python
self.__stock
```

continues accessing:

```text
_Product__stock
```

Therefore, it may still display:

```text
10
```

---

# 🔍 Inspecting Object Attributes

We can inspect an object's instance namespace using:

```python
print(product1.__dict__)
```

Example output may look like:

```python
{
    'name': 'PC',
    '_price': 5000,
    '_Product__stock': 10,
    '__stock': 50
}
```

This helps us understand what attributes actually exist on the instance.

---

# ⚠️ Is `__attribute` Truly Private?

No.

It is still technically possible to access the mangled name:

```python
product1._Product__stock
```

Therefore:

```text
__stock
    ↓
Name Mangling
    ↓
_Product__stock
    ↓
Still technically accessible
```

Double underscore does NOT provide security.

---

# 🎤 Interview Question

## Does Python support private attributes like C++?

A strong answer:

> Python does not enforce private instance attributes in the same way as C++. A double-leading underscore triggers name mangling, which helps prevent accidental access and name collisions, especially with inheritance, but the attribute can still technically be accessed using its mangled name.

---

# 📊 Attribute Naming Comparison

| Syntax | Meaning | Directly Accessible? | Enforced Restriction? |
|---|---|---:|---:|
| `name` | Public | Yes | No |
| `_name` | Non-public convention | Yes | No |
| `__name` | Name-mangled | Not through the simple external name | Not true privacy |

---

# 5️⃣ Getters

A getter is used to retrieve an internal value through a controlled method.

Example:

```python
class Product:

    def __init__(self, stock):

        self.__stock = stock

    def get_stock(self):

        return self.__stock
```

Usage:

```python
print(product1.get_stock())
```

Flow:

```text
Outside Code
     ↓
get_stock()
     ↓
Internal Attribute
     ↓
Return Value
```

---

# 6️⃣ Setters

A setter controls how an internal value is modified.

Example:

```python
def set_stock(self, stock):

    if stock < 0:

        raise ValueError("Stock cannot be negative")

    self.__stock = stock
```

Now validation happens before changing the internal state.

```text
New Value
    ↓
Setter
    ↓
Validation
  ↙     ↘
Invalid  Valid
  ↓       ↓
Reject   Store
```

---

# 7️⃣ The `@property` Decorator

Python properties allow method logic to be accessed using normal attribute syntax.

Example:

```python
class Employee:

    def __init__(self, salary):

        self.__salary = salary

    @property
    def salary(self):

        return self.__salary
```

Normally a method is called using:

```python
object.method()
```

But because `salary` uses:

```python
@property
```

we access it like:

```python
employee.salary
```

No parentheses are required.

---

# 🧠 How `@property` Works Conceptually

When we write:

```python
print(employee.salary)
```

conceptually:

```text
employee.salary
      ↓
Property Getter
      ↓
salary(self)
      ↓
return self.__salary
      ↓
Value Returned
```

From outside, it looks like an attribute.

Internally, method logic executes.

---

# 8️⃣ Property Setter

A setter can be attached to a property:

```python
@salary.setter
def salary(self, value):

    if value <= 0:

        raise ValueError("Salary must be greater than 0")

    self.__salary = value
```

Now:

```python
employee.salary = 75000
```

looks like normal assignment.

But internally:

```text
employee.salary = 75000
          ↓
@salary.setter
          ↓
Validation
          ↓
Is value valid?
      ↙       ↘
    NO         YES
     ↓           ↓
Exception      Store Value
```

This gives us:

```text
Clean Attribute Syntax
+
Validation
+
Controlled State
```

---

# 💻 Day 23 Employee Program

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


    @property
    def salary(self):

        return self.__salary


    @salary.setter
    def salary(self, value):

        if value <= 0:

            raise ValueError(
                "Salary must be greater than 0"
            )

        self.__salary = value


Emp1 = Employee("Zaid", 50000)

print("=" * 5, "Employee Details", "=" * 5)

print(
    f"\nEmployee Name:{Emp1.name}"
    f"\nEmployee Salary:{Emp1.salary}"
)
```

Output:

```text
===== Employee Details =====

Employee Name:Zaid
Employee Salary:50000
```

---

# ❌ Invalid Salary Test

```python
Emp1.salary = -5000
```

The setter receives:

```text
-5000
```

Validation:

```text
-5000 <= 0

TRUE
```

Therefore:

```text
ValueError:
Salary must be greater than 0
```

The invalid value is not stored.

---

# 🔥 Important Concept — Validation During Initialization

Inside the constructor:

```python
self.salary = salary
```

Notice that we are NOT directly writing:

```python
self.__salary = salary
```

Because `salary` is a property, this:

```python
self.salary = salary
```

calls the setter.

Therefore:

```text
Employee("Zaid", 50000)

        ↓

__init__()

        ↓

self.salary = 50000

        ↓

@salary.setter

        ↓

Validation

        ↓

self.__salary = 50000
```

This means validation also happens when the object is first created.

Example:

```python
Employee("Zaid", -50000)
```

will be rejected immediately.

This prevents creating an Employee with an invalid initial salary.

---

# 9️⃣ Property vs Internal Storage

This distinction is extremely important.

```text
salary

      ↓

PUBLIC INTERFACE

      ↓

@property
@salary.setter


------------------------


__salary

      ↓

INTERNAL STORAGE

      ↓

Actual Value
```

Therefore:

```python
Emp1.salary
```

does not directly represent the storage mechanism.

It is the controlled interface.

The actual value is stored in:

```python
self.__salary
```

---

# 🚨 Infinite Recursion Mistake

A common mistake is:

```python
@property
def salary(self):

    return self.salary
```

This causes:

```text
salary getter
    ↓
self.salary
    ↓
salary getter
    ↓
self.salary
    ↓
salary getter
    ↓
...
```

Eventually:

```text
RecursionError
```

Correct:

```python
@property
def salary(self):

    return self.__salary
```

---

# 🚨 Infinite Recursion in Setter

Wrong:

```python
@salary.setter
def salary(self, value):

    self.salary = value
```

Flow:

```text
self.salary = value
       ↓
Setter
       ↓
self.salary = value
       ↓
Setter
       ↓
...
```

Again:

```text
Infinite Recursion
```

Correct:

```python
@salary.setter
def salary(self, value):

    self.__salary = value
```

---

# 🔑 Golden Rule

Inside a property's getter/setter:

```text
Property
    ↓
Should access
    ↓
Different Internal Storage
```

Example:

```text
salary
   ↓
__salary
```

Not:

```text
salary
   ↓
salary
   ↓
salary
   ↓
∞
```

---

# 🔟 Read-Only Property

Suppose:

```python
class Account:

    def __init__(self):

        self.__balance = 1000

    @property
    def balance(self):

        return self.__balance
```

We have a getter but no setter.

Reading:

```python
print(account.balance)
```

works.

But attempting:

```python
account.balance = 5000
```

raises an:

```text
AttributeError
```

because no setter exists.

This can be useful when external code should be able to read a value but not assign to it directly.

---

# 🔥 Interview Question

Consider:

```python
class Account:

    def __init__(self):

        self.__balance = 1000

    @property
    def balance(self):

        print("Getter Called")

        return self.__balance


account = Account()

print(account.balance)
```

Output order:

```text
Getter Called
1000
```

Why?

First:

```python
account.balance
```

invokes the getter.

The getter prints:

```text
Getter Called
```

Then it returns:

```text
1000
```

Finally, the outer:

```python
print()
```

prints that returned value.

---

# 🧠 Connecting All Day 23 Concepts

Today's concepts connect like this:

```text
OBJECT
   ↓
Contains State
   ↓
State Must Remain Valid
   ↓
ENCAPSULATION
   ↓
Control Interaction
   ↓
Attribute Naming
   ├── public
   ├── _non-public convention
   └── __name mangling
   ↓
GETTERS / SETTERS
   ↓
@property
   ↓
VALIDATION
   ↓
Protect Object Invariants
```

---

# 🎯 Beginner vs Strong Understanding

### Beginner

```text
Encapsulation means private variables.
```

### Better

```text
Encapsulation bundles data and methods.
```

### Stronger Understanding

```text
Encapsulation combines state and behavior
while controlling how an object's state is
accessed and modified so that the object
maintains valid invariants.
```

---

# 💡 Key Takeaways

- Encapsulation is broader than simply making attributes private.
- Public attributes can be directly accessed and modified.
- `_attribute` is primarily a non-public convention.
- `__attribute` triggers name mangling.
- Name mangling is not true security.
- `__dict__` helps inspect an object's instance namespace.
- Getters provide controlled reading.
- Setters provide controlled modification.
- `@property` provides attribute-like syntax backed by methods.
- `@property.setter` allows validation during assignment.
- A property should use separate internal storage.
- Using the same property inside its getter/setter can cause infinite recursion.
- Constructor assignments can intentionally go through property setters for validation.
- Raising exceptions can prevent invalid objects from being created.

---

# 📁 Day 23 Files

```text
01_Python/
└── Day_23/
    │
    ├── encapsulation.py
    ├── access_modifier.py
    ├── property.py
    └── README.md
```

---

# 🚀 Day 23 Python Progress

```text
OOP Foundations
      ↓
Classes & Objects          ✅
      ↓
Constructors               ✅
      ↓
Instance Attributes        ✅
      ↓
Instance Methods           ✅
      ↓
Object References          ✅
      ↓
Encapsulation              ✅
      ↓
Access Conventions         ✅
      ↓
Name Mangling              ✅
      ↓
Getters & Setters          ✅
      ↓
@property                      ✅
      ↓
Property Validation        ✅
      ↓
NEXT → Inheritance 🔜
```

---

# 🧠 Today's Biggest Lesson

Good programming is not only about asking:

```text
"Can this code run?"
```

We should also ask:

```text
Can this object enter an invalid state?

Who is allowed to modify this data?

Should modification go through validation?

What interface should the class expose?

Can I change the internal implementation
without breaking outside code?
```

That is the difference between simply writing classes and starting to think about **object-oriented design**.

---

## 🔥 Basics to Advance

> Don't just learn how to create objects.

Learn how to design objects that protect their own valid state.

**Learn → Understand → Experiment → Break → Debug → Design Better 🚀**