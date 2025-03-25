try:
    x_input = input("Enter a number: ")
    y_input = input("Enter another number: ")
    x = int(x_input)
    y = int(y_input)

    print("x / y = ", (x / y))
except ValueError:
    print("Invalid integer")
    print("Please try again")
except ZeroDivisionError:
    print("Cannot divide by zero")
    print("Please try again")
except ArithmeticError:
    print("Arithmetic error")
    print("Please try again")