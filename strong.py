# Strong Number: Sum of factorial of digits of a number is equal to that number
def factorial(n):
    return 1 if (n == 0 or n== 1) else n * factorial(n-1)

def isStrongNumber(n):
    sum = 0
    for a in n:
        sum += factorial(int(a))
    return "Yes" if (sum == int(n)) else "No"

number = input()
print(isStrongNumber(number))
