x=5 #this variable is ignored because of the enclosing variable x 
y=2 #Global variable
print("Global variable x & y:",x,y)
def calculator():
    "The Calculator Performs only Addition & substraction"
    
    x=18 #Enclosing variable

    def add():
        print("Accessing Enclosing variable x:",x)
        print("Accessing Global variable y:",y)
        print("Addition:",x+y) #x accesses Enclosing variable and y accesses Global variable

    def subtract():
        print("Subtraction:",x-y)

    add()
    subtract()

calculator()