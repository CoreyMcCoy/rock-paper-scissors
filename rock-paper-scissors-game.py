# Make a simple "rock paper scissors" game.

# Import the random module
import random

# Define the game rules
rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Define the game options
options = ["rock", "paper", "scissors"]

# Define the game loop
while True:
    # Get the user's choice
    user_choice = input("Choose rock, paper, or scissors: ")
    # Get the computer's choice
    computer_choice = random.choice(options)
    # Print the choices
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    # Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    # Check for a win
    elif rules[user_choice] == computer_choice:
        print("You win!")
    # Otherwise, the computer wins
    else:
        print("The computer wins!")
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    # If they don't want to play again, break out of the loop
    if play_again != "y":
        break

# Print a goodbye message
print("Thanks for playing!")

# Run the program
# python rock-paper-scissors-game.py
