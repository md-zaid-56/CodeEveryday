def calculations(*prices): 
    '''Function used to Calculate total sum of prices'''
    sum = 0 
    for price in prices:
        sum += price
    return sum

print("Total price is Bill 1: ",calculations(500,1200))
print("Total price is Bill 1: ",calculations(1200,1500,250))