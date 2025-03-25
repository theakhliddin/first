def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

def modulus(x, y):
    return x % y

def main():
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Modulus', modulus)
    }

    print("Select operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"{num1} {operation_name} {num2} = {result}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
