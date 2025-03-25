total = 0

while True:
    number = int(input("Enter a positive number (0 to stop): "))
    if number == 0:
        break
    elif number > 0:
        total += number
    else:
        print("Please enter a positive number.")

print(f"The total sum of the entered numbers is: {total}")