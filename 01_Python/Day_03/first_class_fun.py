def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

op = { #Storing functions in a dictionary
    "+":add,
    "-":subtract
}

print("Storing function in dictionary:",op["+"](48,12))
print("Storing function in dictionary:",op["-"](100,5))

x=add
print("Storing function in variable ", x(5,6))
