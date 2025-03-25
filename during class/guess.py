#guess number
import random
def guess():
    number = random.randint(1, 10) 
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != number:
        if guess > number:
            print("Choose another number, Too high!")
        else:
            print("Choose another number, Too low")
        guess = int(input("Guess again: "))
    print("That's correct, you got it!")


def main():
    guess()

if __name__ == "__main__":
    main()  