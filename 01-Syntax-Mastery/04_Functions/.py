"""
Rock Paper Scissors Engine

User vs Computer game using clean functional separation
"""

import random

def user_choice():
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if choice not in ("rock", "paper", "scissors"):
        return None
    return choice

def computer_choice():
    return random.choice(("rock", "paper", "scissors"))

def winner(user, computer):
    if user == computer:
        return "Draw"
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock")
    }
    if (user, computer) in wins:
        return "User Wins"
    return "Computer Wins"

def play():
    user = user_choice()
    if user is None:
        print("Invalid choice")
        return
    computer = computer_choice()
    result = winner(user, computer)
    print(f"\nUser chose     : {user}")
    print(f"Computer chose : {computer}")
    print(f"Result         : {result}")

while True:
    play()
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        break