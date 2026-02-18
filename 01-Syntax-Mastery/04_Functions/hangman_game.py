"""
Simple hangman game where you guess letters to reveal a word
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

    print("=== Hangman ===")

    while attempts > 0:
        print("\nWord:", display_word(secret, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Type one letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter (a-z)")
            continue

        if guess in guessed_letters:
            print("You already tried that one")
            continue

        guessed_letters.add(guess)

        if guess not in secret:
            attempts -= 1
            print("Nope, that letter is not in the word")

        if is_word_guessed(secret, guessed_letters):
            print("\nNice! You got the word:", secret)
            return

    print("\nOut of tries. The word was:", secret)

def main():
    run_game()

if __name__ == "__main__":
    main()