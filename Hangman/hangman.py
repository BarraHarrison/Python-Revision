# Hangman in Python
import random

words = ("apple", "orange", "carrot", "broccoli", "potatoe")

# Dictionary of key
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/   "),
    6: (" o ",
        "/|\\",
        "/ \\")
    }

def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    pass

if __name__ == "__main__":
    main()