def add(num1, num2):
    addResult = num1 + num2
    return addResult

def exponent(num1, num2):
    expResult = num1**num2
    return expResult

def main():
    num1 = int(input('enter first number: '))
    num2 = int(input("enter second number: "))
    placeHolderVar = add(num1, num2)
    print(placeHolderVar)
    
    mixExpression = placeHolderVar * 5
    print(mixExpression)
    
    result=exponent(num1, num2)
    print(result)

main()