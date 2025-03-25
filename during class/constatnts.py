E = 2.71828182845904523536028747135266249775724709369995

def e_to_x(x):
    return E ** x
def compound_interest(amount):
    return amount * E

def main():
    print(e_to_x(1))
    print(compound_interest(1000))

main()