def outer():
    """Demonstration of nonlocal keyword in Python"""
    x = 20
    print("X value inside the outer() before the modification:", x)
    def inner():
        nonlocal x   #If we comment this line then inner() will create a local variable x 
        x += 10 #after that this will throw an error because it will access the local variable x and not Enclosing variable
        print("X value inside the inner() after the modification:", x)

    inner()
    print("X value inside the outer() after the modification:", x)

outer()
