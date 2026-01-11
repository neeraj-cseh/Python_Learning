# def factorial (n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * (factorial(n-1))
    
# print (factorial(4))
# print (factorial(3))
# print (factorial(2))
# print (factorial(1))

#Fibonacci Sequence
def f(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return (f(x-1)+f(x-2))
    
print (f(4))