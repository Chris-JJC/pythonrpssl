import random
import os

"""
Rock,Paper,Scissors Spock and Lizard app
Chris Bowers
June 2025
rock_paper_scissors_spock_lizard.py
Assisted by ChatGPT
"""

score_file = "scorecard.txt"


def welcome_user():
    print(f'\nWelcome to Rock, Paper, Scissors, Spock, and Lizard.!')


def get_player_name():
    player_name = input("Please enter your name: ")
    print(f"\nNice to meet you, {player_name}! Let's play!\n")
    return player_name


def get_computer_choice(options):
    computer_choice = random.choice(options)
    print(f"\nComputer chose: {computer_choice}")
    return computer_choice


def chat_solution(user_choice, computer_choice):
    win_rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif computer_choice in win_rules[user_choice]:
        print("You win!")
        return "win"
    else:
        print("Computer wins!")
        return "loss"


# [Start update_score_file function]
def update_score_file(scores):
    try:
        with open(score_file, 'w') as f:
            for key in scores:
                f.write(f"{key}:{scores[key]}\n")
        print("Scorecard updated!")
    except Exception as e:
        print(f"Error writing to scorecard file: {e}")
# [End update_score_file function]


# [Start load_score_file function]
def load_score_file():
    scores = {"win": 0, "loss": 0, "tie": 0}
    if os.path.exists(score_file):
        try:
            with open(score_file, 'r') as f:
                for line in f:
                    key, value = line.strip().split(":")
                    scores[key] = int(value)
        except Exception as e:
            print(f"Error reading scorecard file: {e}")
    return scores
# [End load_score_file function]


def get_player_choice(options):
    user_choice = ""
    while user_choice not in options:
        user_choice = input("Enter rock, paper, scissors, spock, or lizard (or type 'exit' to quit): ").strip().lower()
        if user_choice not in options:
            print("Invalid choice. Please select rock, paper, scissors, lizard, or spock.")
    return user_choice


# [Start main function]
def main():
    print(f"\n[Debug] Current working directory: {os.getcwd()}")
    options = ("rock", "paper", "scissors", "lizard", "spock", "exit")
    welcome_user()
    player_name = get_player_name()
    scores = load_score_file()
    # Reset the scorecard at the start of the game
    scores = {"win": 0, "loss": 0, "tie": 0}
    update_score_file(scores)

    while True:
        user_choice = get_player_choice(options)
        if user_choice == "exit":
            break

        computer_choice = get_computer_choice(options)
        result = chat_solution(user_choice, computer_choice)

        if result == "win":
            scores["win"] += 1
        elif result == "loss":
            scores["loss"] += 1
        else:
            scores["tie"] += 1

        update_score_file(scores)

    print(f"\nThanks for playing, {player_name}!")
    print(f"Final Scores - Wins: {scores['win']}, Losses: {scores['loss']}, Ties: {scores['tie']}")
# [End main function]


if __name__ == "__main__":
    main()
