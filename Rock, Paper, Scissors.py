import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in choices:
        print("Invalid choice. Try again.")
        user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if _name_ == "_main_":
    play()
