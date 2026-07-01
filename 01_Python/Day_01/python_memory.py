x=10
print("This is X memory Address:", id(x)) #Prints the memory address of X variable

x=20
print("This is X memory Address after change:", id(x))
print("This is 10 memory Address after change:", id(10)) #This means that 10 is still in memory 

b=20
print("This is B memory Address:", id(b)) #This means both x and b are pointing to the same memory address
# The Objects which has same memory address are Called as REFERENCE OBJECTS 
#The object stays until the garbage collector removes it from memory. also called as IMMUTABLE OBJECTS

a = [1,2,3]
print("This is A memory Address:", id(a)) #Prints the memory address of A

b= a.append(4) #This will change the original list and both a and b will point to the same memory address
print("This is B memory Address after append:", id(b)) #Prints the memory address
print("This is A memory Address after append:", id(a)) #Prints the memory address

c = a.copy() #This will create a new copy of the list and assign it to c
print("This is C memory Address after copy:", id(b)) #Prints the memory address
#The copy() method will create a new list object in memory and assign it to c. Therefore, c will have a different memory address than a and b.