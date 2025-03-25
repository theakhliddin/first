def guessing_game():
    number = input("Enter a number between 1 and 10: ")
    number = int(number)
    if number < 1 or number > 10:
        raise ValueError("Number is out of range")
    print("You guessed: ", number)
guessing_game()