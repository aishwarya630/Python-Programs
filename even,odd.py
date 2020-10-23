def evenNumbers(s,e):
    for n in range(s,e+1):
        if (n % 2 != 0):
            print(n, end=" ") 

def oddNumbers(s,e):
    for n in range(s,e+1):
        if (n % 2 == 0): 
            print(n, end=" ") 

start = int(input())
end = int(input())
print("Even Numbers: ")
evenNumbers(start,end)
print("\nOdd Numbers: ")
oddNumbers(start,end)