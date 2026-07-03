def closure():
    """Learning about closure"""

    x = 10 #Enclosing variable

    def inn():
        nonlocal x
        x +=1
        print(x)
    return inn

z = closure()
z()
z()