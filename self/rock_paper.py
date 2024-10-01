import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Enter rock, paper, scissors: ").lower()
    
    if user_choice == computer_choice:
        print(f"It's a tie! Both chose {user_choice}")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
            print(f"You win! {user_choice} beats {computer_choice}")
    else:
        print(f"You lose! {computer_choice}  beats {user_choice}")

rock_paper_scissors()