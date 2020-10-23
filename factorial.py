import time
def factorial(n):
    fact = 1
    if n == 0 or n ==1:
        return 1
    else:
        for i in range(2,n+1):
            fact *= i
    return fact

def recursiveFactorial(n):
    # if n == 0or n==1:
    #     return 1
    # else:
    #     return n * recursiveFactorial(n-1)
    return 1 if (n == 0 or n == 1) else n * recursiveFactorial(n-1)
    # Better Program

n = int(input())
print(factorial(n))
print(recursiveFactorial(n))