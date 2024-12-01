import random

# Slot Machine in Python
def spin_row():
    """Simulates spinning a row of the slot machine."""
    symbols = ["⭐️", "🎄", "💙", "🥦", "💰"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    """Prints a row of the slot machine."""
    print("  |  ".join(row))

def get_payout(row, bet):
    """Determines the payout based on the symbols in the row."""
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        if symbol == "💰":
            return bet * 10
        elif symbol == "⭐️":
            return bet * 5
        elif symbol == "💙":
            return bet * 3
        elif symbol == "🎄":
            return bet * 2
        elif symbol == "🥦":
            return bet
    return 0

def main():
    balance = 100

    print("Welcome to the Python Slot Machine Game")
    print("Symbols: ⭐️ 🎄 💙 🥦 💰")

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")

        # Input Validation for bet amount
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue
            
        # Deducting the bet from the balance
        balance -= bet

        # Spinning the slot machine
        row = spin_row()
        print("\nSpinning.....,")
        print_row(row)

        # Calculating the payout
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout}")
            balance += payout
        else:
            print("Sorry, you lost this round.")

    print("\nGame Over! You ran out of balance.")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
