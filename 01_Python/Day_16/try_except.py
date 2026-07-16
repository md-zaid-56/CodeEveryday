try :
    num = int(input("Enter number:"))
    div = num/5
except ValueError :
    print("Enter a Valid value & in numbers:")
except ZeroDivisionError :
    print("Value Can't be divided by zero")

print("Number was: ",num)
print("Number/5 : ",div)
print("Whole Code Executed")