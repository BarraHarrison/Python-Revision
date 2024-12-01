# Hangman in Python
# For the words I am going to use countries from around the world
import random

words = ("france", "belgium", "netherlands", "germany", "italy")

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
    answer = random.choice(words)
    print(answer)

if __name__ == "__main__":
    main()