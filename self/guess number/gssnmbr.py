import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0
    
    print("Guess a number between 1 and 100!")
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif  guess > number_to_guess:
            print("Too high!")
            
    print(f"NIICCCE, You've guessed the number in {attempts} attempts. ")

guessing_game()