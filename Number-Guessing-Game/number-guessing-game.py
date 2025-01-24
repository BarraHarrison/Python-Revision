import random

def number_guessing_game(scoreboard):
    def get_difficulty():
        """Prompt the user to choose a difficulty level and return the range"""
        print("Welcome to the Python Number Guessing Game")
        print("Select a difficulty level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")

        while True:
            choice = input("Enter 1, 2 or 3: ").strip()
            if choice == "1":
                return 1, 10
            if choice == "2":
                return 1, 50
            if choice == "3":
                return 1, 100
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")

    def update_scoreboard(player_name, scoreboard, guesses):
        """Update the scoreboard with the player's scores."""
        if not isinstance(scoreboard, dict):
            raise TypeError("Scoreboard must be a dictionary.")
        if player_name in scoreboard:
            scoreboard[player_name] = min(scoreboard[player_name], guesses)
        else:
            scoreboard[player_name] = guesses


    def display_scoreboard(scoreboard):
        """Display the scoreboard with the best scores coming first"""
        print("\n--- Scoreboard ---")
        for player, score in sorted(scoreboard.items(), key=lambda item: item[1]):
            print(f"{player}: {score} guesses")
        print("--------------------\n")

    # Setting up the game based on difficulty
    lowest_number, highest_number = get_difficulty()
    answer = random.randint(lowest_number, highest_number)
    guesses = 0

    print(f"\nGuess a number between {lowest_number} and {highest_number}")
    player_name = input("Enter your name: ").strip()

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
  
        guess = int(guess)
        guesses += 1

        if not (lowest_number <= guess <= highest_number):
            print(f"Your guess is out of range. Please choose a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! Good job {player_name}! The answer was {answer}")
            print(f"You guessed it in {guesses} tries.")
            update_scoreboard(scoreboard, player_name, guesses)
            display_scoreboard(scoreboard)
            break

if __name__ == "__main__":
    scoreboard = {}
    while True:
        number_guessing_game(scoreboard)
        play_again = input("n\Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break