"""Without Recursion"""
n=int(input("Please enter your number:")) #Taking input from user
result=1                                 
while n>1:
  result=result*n             #Method
  n=n-1
print(result)                 #Printing result


"""With Recursion"""
def factorial(n):
    reuslt=0
    if n>0:
        result=n*factorial(n-1)     #Using Recursion 
    else:
        result=1
    return result
num=int(input("Please enter your number:"))
print(factorial(n))
