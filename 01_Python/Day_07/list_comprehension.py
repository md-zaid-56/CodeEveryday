#Problem 1
prices = [250,1200,450,999,1500,300]
discounted_price = [ i-i/10 for i in prices if i>=1000] #Deduct 10% from prices where price>=1000
print(discounted_price)

#problem 2
marks = [35, 78, 91, 42, 88, 29, 67]
result = ["Pass" if mark>=40 else "Fail" for mark in marks]
print(result)