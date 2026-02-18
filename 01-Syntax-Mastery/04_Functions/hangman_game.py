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