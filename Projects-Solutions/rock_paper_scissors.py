import random

from enum import IntEnum

# Input numbers instead of strings
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# user selects between rock, paper and scissors
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

# Make the computer choose
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1) # len starts counting from 1. '-1' added for random integer from 0 to 2.
    action = Action(selection)
    return action

# After both players made their choice, time to find out who wins
def determine_winner(user_action, computer_action):
    # Printing the choices that the user and the computer made
    print(f"\nYou chose {user_action.name}, computer chose {computer_action.name}.\n")
    # compare players' choices
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


while True: # <<< while loop to create recurring events
    try:
        user_action = get_user_selection()
    except ValueError as e:
    # Value Error exception if the user selection is invalid
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)
    # without that check, the code will run indefinitely
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

