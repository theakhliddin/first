# even_or_odd.py

def check_even_or_odd(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    number = input("Please provide a number: ")
    check_even_or_odd(number)
