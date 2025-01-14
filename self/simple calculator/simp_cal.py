def calculator():
    print("simple calculator")

    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator(+,-,*,/): ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif  operator == "*":
            result  = num1 * num2
        elif  operator == "/":
            if num2 !=0:
                result  = num1 / num2
            else:
                result = "Error! Devision by zero"
        else:
            result = "Invalid operator!"
        print(f"REsult:  {result}")

        cont = input("Do you want to calculate again? (yes/no): ").lower()
        if cont != "yes":
            break
        
calculator()