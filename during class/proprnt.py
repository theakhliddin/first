def prompt_and_print():
    """
    Prompts the user to enter two numeric values (one at a time).
    Prints the results of adding, subtracting, multiplying, and dividing the two numbers.
    """
    # Prompt user for the first numeric value
    num1 = float(input("Enter the first number: "))
    
    # Prompt user for the second numeric value
    num2 = float(input("Enter the second number: "))
    
    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
    
    # Print results
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

# Call the function to test it
prompt_and_print()
