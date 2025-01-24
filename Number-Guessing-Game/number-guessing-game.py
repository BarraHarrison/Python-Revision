import random

def number_guessing_game():
    lowest_number = 1
    highest_number = 100
    answer = random.randint(lowest_number, highest_number)
    guesses = 0

    print("Weclome to the Python Number Guessing Game")
    print(f"Guess a number between {lowest_number} and {highest_number}")

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
            print(f"CORRECT! The answer was {answer}")
            print(f"You guessed it in {guesses} tries.")
            break

if __name__ == "__main__":
    number_guessing_game()