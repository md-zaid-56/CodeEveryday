try :
    num = int(input("Enter a number: "))
    div = 5/num

except ValueError :
    print("Please Enter valid value & in digits")

except ZeroDivisionError :
    print("Value Can't be Divided by ZERO")

else :
    print("Number is: ",num)
    print("Division : ",div)

finally :
    print("Thank you for using calculator")
