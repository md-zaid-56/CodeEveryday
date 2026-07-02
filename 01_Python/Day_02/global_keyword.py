z = 0
def demo_error():
    z += 10  # This will throw the error because 'z' is treated as local variable because it has '=' (assignment) operator
    print(z)

#demo_error() # UnboundLocalError: cannot access local variable 'z' where it is not associated with a value

print("Global Variable before modification:",z) 

def global_change():
    global z # This will tell python that we are using the global variable 'z'
    z += 10
    print("Modify Global var in local frame:",z) 

global_change() 
print("Global Variable after modification:",z) # Global Variable is updated because we used 'global' keyword in that function

s = [1,2,3]
print("Global Variable [list] before modification:",s)

def list_modification():
    s.append(4) # This will not throw the error because first of all it is mutable object and we are not using '='(assignment) operator to it
    print("Modify Global [list] var in local frame:",s)

list_modification()
print("Global Variable [list] after modification:",s)