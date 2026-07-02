z = 20 #Global Variable

def local_var():
    a = 20 # Local Variable
    print("Local Variable:",a)
    print("Global Variable:",z)   #Using LEGB Rule, In this python will first look for the 'z' variable in this function frame and if not found it will look into Enclosing function frame and then in Global Frame.
    print(locals()) # It will return local variables in this function frame in form of dictionary.

local_var()
print(globals()) # It will return all the variables in Global Frame in form of dictionary.

a = 5
def shadow():
    a=10
    print("Local Variable by using Shadowing:",a) # Local Variable will shadow the Global Variable by using LEGB rule.

shadow()
print("Global Variable after Shadowing:",a) # Global Variable will be printed as it is because that Loacl 'a' is destroyed because frame is no more in use.

