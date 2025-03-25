def calculate_square_area(side_length):
    return side_length ** 2

def main():
    side_length = float(input("Enter the side length of the square: "))
    area = calculate_square_area(side_length)
    print(f"The area of the square is: {area}")

if __name__ == "__main__":
    main()