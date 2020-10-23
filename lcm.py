def findLCM(num1,num2):
    x = num1
    y = num2
    while(num2):
        num1,num2 = num2,num1%num2
    gcd = num1
    lcm = x*y/gcd
    return int(lcm)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
num1 = arr[0]
num2 = arr[1]

lcm = findLCM(num1, num2)

for i in range(2,n):
    lcm = findLCM(lcm,arr[i])
print(lcm)