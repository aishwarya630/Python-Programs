def armstrong(n):
    sum = 0
    for a in n:
        sum += int(a)**3
    return "Yes" if(sum == int(n)) else "No"

number = input()
print(armstrong(number))