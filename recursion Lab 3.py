import sys
sys.setrecursionlimit(100000)

def factorial(n):
    #Provide code here
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))
        
print('factorial(5):', factorial(5))   
# Expected 120
def fib(n):
    # Provide your code here
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 1:
        return (fib(n-1) + fib(n-2))
    
        
print('fib(8):', fib(8))
# Expected 13

def addup(list):
    # Provide your code here
    if len(list) == 0:
        return 0
    else:
        return (list[0] + addup(list[1:]))

print('addup([1,2,3,4,5]):', addup([1,2,3,4,5]))
# Expected 15
print('addup(range(101)):', addup(range(101)))
# Expected 5050



