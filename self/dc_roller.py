import random

def roll_dice():
    while True:
        roll = input("Roll the dice? (yes/no): ").lower()
        if roll == "yes":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"You rolled a {dice1} and a {dice2}. Total: {dice1 + dice2}")
        elif roll == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

roll_dice()