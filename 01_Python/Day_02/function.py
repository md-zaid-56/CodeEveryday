def greet(): #No Parameter
    print("Hello,Welcome to the Challenge!")

def name(name="Guest"):   #Default parameter
    print(f"Hello {name}")

def add_no(a,b):   #Everything passed in Function Definition is Known as Formal Parameter/Parameters
    print("Addition of two numbers:",a+b)

def sub_no(a,b):
    return a-b #return value

def mul_div_no(a,b):
    return a*b,a/b #Multiple return Values 

greet()
name()    #No argument passed
name("Zaid") #One Argument Passed
add_no(5, 2)     #Eveything passed in Funtion Calling is Known as Actual Parameter/Arguments
c = sub_no(b=2,a=5) #value returned stored in variable c
print("Subtraction of two numbers:",c)
a,b=5,2 
z,s = mul_div_no(a,b) #Multiple return values, Python always return multiple values in the form of tuple
print("Multiplication of two numbers:",z)
print("Division of two numbers:",s)