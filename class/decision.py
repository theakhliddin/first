def main():
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    c = int(input("Input the third number: "))
    result = is_equilateral(a, b, c)
    print(result)

def is_equilateral(a, b, c):
    if a == b and b == c and c == a:
        return "YEs"
    else:
        return "No"

main()