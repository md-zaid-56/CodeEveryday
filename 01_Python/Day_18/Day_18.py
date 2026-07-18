print("=" * 50)
print("1. divmod() Function")
print("=" * 50)
# divmod() gives us quotient and remainder both
num1 = 17
num2 = 5
result = divmod(num1, num2)
print(f"Numbers: {num1} and {num2}")
print(f"Result: {result}")
print(f"Quotient: {result[0]}")
print(f"Remainder: {result[1]}")


print("\n" + "=" * 50)
print("2. bin() Function")
print("=" * 50)
# bin() converts normal integer number into binary
number = 10
binary = bin(number)
print(f"Number: {number}")
print(f"Binary: {binary}")


print("\n" + "=" * 50)
print("3. ord() and chr() Functions")
print("=" * 50)
# ord() gives Unicode value of character
character = "A"
value = ord(character)
print(f"Character: {character}")
print(f"Unicode Value: {value}")


# chr() does opposite of ord()
# it converts Unicode value into character

number = 90
character = chr(number)
print(f"\nUnicode Value: {number}")
print(f"Character: {character}")