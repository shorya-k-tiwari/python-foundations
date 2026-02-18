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