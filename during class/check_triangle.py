def check_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))
        
        if a <= 0 or b <= 0 or c <= 0:
            print("Side lengths should be positive numbers.")
        elif a + b > c and a + c > b and b + c > a:
            triangle_type = check_triangle_type(a, b, c)
            print(f"The triangle is {triangle_type}.")
        else:
            print("The given lengths do not form a triangle.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()