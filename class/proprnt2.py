def prompt_and_print():
    """
    Prompts the user to enter two numeric values (one at a time).
    Prints the results of adding, subtracting, multiplying, and dividing the two numbers.
    Uses int() and float() functions as needed and prints results directly.
    """
    # Prompt user for the first numeric value and convert to float
    num1 = float(input("Enter the first number: "))
    
    # Prompt user for the second numeric value and convert to float
    num2 = float(input("Enter the second number: "))
    
    # Print results directly without additional variables
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division: {num1} / {num2} = {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}")

# Call the function to test it
prompt_and_print()
