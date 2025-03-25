def calculate_circle_area(radius):
    pi = 3.141592653589793
    return pi * radius * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area}")

if __name__ == "__main__":
    main()
