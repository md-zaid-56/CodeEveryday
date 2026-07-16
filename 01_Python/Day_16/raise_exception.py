try :
    age = int(input("Enter Age: "))

    if age<0 :
        raise ValueError("Enter Valid Age")
    
    if age<18 :
        raise PermissionError("You must be atleast 18")
    
except ValueError as e:
    print(e)

except PermissionError as p:
    print(p)

else :
    print("Access Granted")

finally :
    print("Application Closed")