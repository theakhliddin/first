def is_equalateral(a, b, c):
    if a == b and b == c and c == a:
        return "Yes"
    else:
        return "No"
print(is_equalateral(5, 5, 7))