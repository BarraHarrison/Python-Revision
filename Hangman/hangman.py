# Hangman in Python
# For the words I am going to use countries from around the world
import random

# Extended list of countries
words = (
    "france", "belgium", "netherlands", "germany", "italy",
    "spain", "portugal", "sweden", "norway", "denmark",
    "finland", "poland", "greece", "ireland", "iceland",
    "canada", "brazil", "argentina", "chile", "mexico",
    "japan", "china", "india", "russia", "australia"
)

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
    """Displays the hangman art based on the number of wrong guesses."""
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    """Displays the current hint with guessed letters."""
    print(" ".join(hint))

def main():
    answer = random.choice(words)  
    hint = ["_"] * len(answer)     
    wrong_guesses = 0              
    guessed_letters = set()        
    is_running = True

    print("Welcome to Hangman! Guess the country!")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        # Prompt user for a letter
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            print(f"Good job! '{guess}' is in the word!")
            for idx, letter in enumerate(answer):
                if letter == guess:
                    hint[idx] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1

        # Check for win or lose conditions
        if "_" not in hint:
            display_hint(hint)
            print("Congratulations! You've guessed the word!")
            is_running = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            print(f"Game over! The correct word was: {answer}")
            is_running = False

if __name__ == "__main__":
    main()
