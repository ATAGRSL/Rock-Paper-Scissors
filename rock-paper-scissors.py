import random

def play_game(user_input, computer_pick):
    if user_input == "rock" and computer_pick == "scissors":
        print("You won! Rock beats Scissors.")
        return "user"
    elif user_input == "paper" and computer_pick == "rock":
        print("You won! Paper beats Rock.")
        return "user"
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won! Scissors beats Paper.")
        return "user"
    elif user_input == computer_pick:
        print("It's a tie!")
        return "tie"
    else:
        print("You lost! " + computer_pick + " beats " + user_input + ".")
        return "computer"

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
ties = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    result = play_game(user_input, computer_pick)

    if result == "user":
        user_wins += 1
    elif result == "computer":
        computer_wins += 1
    else:
        ties += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("You tied", ties, "times.")
print("Goodbye!")