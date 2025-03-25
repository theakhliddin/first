""""def variables_practice():
    age = input("Enter your age: ")
    age_mnth = age * 12
    days_yr = 31*12
    pet = input("Enter the name of your first pet: ")
    pi = 3.14159

    print("Your age in months is:", age_mnth)
    print("The number of days in a year is:", days_yr)
    print("The name of your first pet is:", pet)
    print("The value of pi is:", pi)
variables_practice()


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

first = x ** y
second = x * y
third = x / y
fourth = x // y
fifth = x % y
sixth = x + y
seventh = x - y

print("The first result is:", first)
print("The second result is:", second)
print("The third result is:", third)
print("The fourth result is:", fourth)
print("The fifth result is:", fifth)
print("The sixth result is:", sixth)
print("The seventh result is:", seventh)

from 2.2 python program, define a function, 2.1 give example for programmming language 2 editor 3 compiler 4version control system 5 command line tool
6 compiled languaged 7 interpreted language 8 variables 9 python identifiers 10 ide 

1.1 syntax of ls, cd, cp, rm, mv, ls force, ls -force, mkdir, cd, cat,

write a command, make directy and subdirectory, create a file, copy a file, move a file, remove a file,

wild card, 
git restore, conflict, environment variables
"""


"""def study_session():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    otput = x + y
    print("The result is:", otput)
study_session()"""

"""def types():
    int("23")
    int("23.5")
    int("hello")
    
    float("23")
    float("23.5")
    float("hello")

    str("23")
    str("23.5")
    str("hello")
types()"""

"""def prmpt():
    x = int(input("Enter the first number: "))
    y = float(input("Enter the second number: "))


    print("12 + 14", x + y)
    print("12 - 14", x - y)
    print(int(("12 * 14", x * y)))
    print("12 / 14", x / y)
prmpt()"""

monhts_in_year = 12

def happy_birthday():
    name = input("Enter your name: ")
    month = input("Enter the month you were born: ")
    day = input("Enter the day you were born: ")
    year = input("Enter the year you were born: ")

    print(name, "you were born on", month, day, ",", year)

def main():
    happy_birthday()
    happy_birthday()
    happy_birthday()
main()