def is_this_palindrome(s):
    return s == s[::-1]

s = "racecar"
ans = is_this_palindrome(s)
if ans:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")