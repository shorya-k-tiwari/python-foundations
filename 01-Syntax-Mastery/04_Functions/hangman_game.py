"""
Hangman Game
Player guesses letters to reveal the hidden word
"""

import random

WORDS = ["python", "algorithm", "function", "variable", "iteration"]

def pick_word():
    return random.choice(WORDS)

def display_word(secret, guessed_letters):
    display = ""
    for ch in secret:
        if ch in guessed_letters:
            display += ch + " "
        else:
            display += "_ "
    return display.strip()

def is_word_guessed(secret, guessed_letters):
    for ch in secret:
        if ch not in guessed_letters:
            return False
    return True


def run_game():
    secret = pick_word()
    guessed_letters = set()
    attempts = 6

    print("=== Hangman Game ===")

    while attempts > 0:
        print("\nWord:", display_word(secret, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single alphabet letter")
            continue

        if guess in guessed_letters:
            print("Already guessed")
            continue

        guessed_letters.add(guess)

        if guess not in secret:
            attempts -= 1
            print("Wrong guess!")

        if is_word_guessed(secret, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret)
            return

    print("\nGame Over! The word was:", secret)


def main():
    run_game()

    
if __name__ == "__main__":
    main()