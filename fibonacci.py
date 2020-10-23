def fibonacci(n):
    a = 0
    b = 1
    c = 0
    print(a, end="")
    print(b, end="")
    for i in range(n-2):
        c = a + b
        a = b 
        b = c
        print(c,end="")

def recursiveFibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

n = int(input())
fibonacci(n)
recursiveFibonacci(n)