import math

def cal_area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * radius ** 2
    return area
def cal_circle_area_from_diameter(diameter):
    if diameter < 0:
        raise ValueError("Diameter cannot be negative")
    radius = diameter / 2
    area = cal_area_circle(radius)
    return area

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area = cal_area_circle(radius)
    print(f"Area of the circle with radius {radius} is {area:.2f} square units")

    diameter = float(input("Enter the diameter of the circle: "))
    area = cal_circle_area_from_diameter(diameter)
    print(f"Area of the circle with diameter {diameter} is {area:.2f} square units")