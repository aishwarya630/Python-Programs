def palindrome(n):
    res = n[::-1]
    return "Yes" if (res == n) else "No"

user_input = input()
print(palindrome(user_input))