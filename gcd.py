# GCD LCM Of Multiple Numbers
def findGCD(x,y):
    while(y):
        x,y = y,x%y
    return x

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
num1 = arr[0]
num2 = arr[1]

gcd = findGCD(num1, num2)
for i in range(2,n):
    gcd = findGCD(gcd, arr[i])
print(gcd)