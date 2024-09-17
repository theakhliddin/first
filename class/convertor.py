"""" This will convert user currency to AED"""

USD_to_AED_Rate = 3.67

def converter(recievedVal):
    converted_to_AED = recievedVal + USD_to_AED_Rate
    return converted_to_AED

def default_Convertion():
    print("The current rate of USD to AED is: ", USD_to_AED_Rate)

def main():
    input1 = input(("input first value: "))
    input2 = input(("input second value: "))
    result = converter(input1)
    print(input1, "is a equvalent to ", result, "AED")
    default_Convertion()    
main()