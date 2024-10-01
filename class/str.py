"""
print("She said \"I dont like broccoli\"")
print("A \t B \t C \t D \t E")
print("This/is\\a/test\\.")
print("This \n is a string \n with newlines in \n the middle")
print("She \t said \"I \\ \n don't \t like \\  \n broccoli\"")
"""


"""
length = len(StringMessage)
print(length)
print(StringMessage[0])
print(StringMessage[3])
"""
"""
StringMessage = "Yoda"

def count():
    counter = 0 
    while counter < len(StringMessage):
        print(StringMessage[counter])
        counter = counter + 1

def countback():
    counter = 1
    while counter <= len(StringMessage):
        print(StringMessage[counter])
        counter = counter +  1

def main():
    print("Yoda")
    count()
    countback()    
    """
"""    
input1 = ""
while True:
    input1 = input("Enter something: ")
    if input1 == "x":
        break
print("Exiting the loop... ")
"""
"""
while True:
    input1=input("Enter something: ")
    if input1=="y":
        #print("you entered  y")
        continue
    print(input1)
    if input1=="x":
        break
print("exiting the loop...")
"""

count = 0
while count < 10:
    count = count + 1
    if count == 4:
        continue
    print(count)
print("Done!")