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


