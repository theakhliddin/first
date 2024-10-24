#factorila recursion

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)
    
def main():
    number = int(input("Enter number: "))
    result =  factorial(number)
    print(result)