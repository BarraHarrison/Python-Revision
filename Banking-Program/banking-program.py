# Python Banking Program

# Constants
MENU = """
**************************
    Banking Program
**************************
1. Show Balance
2. Deposit
3. Withdraw
4. View Transactions
5. Exit
**************************
"""
INVALID_CHOICE = "That is not a valid choice. Please enter a number between 1 and 5."
INVALID_AMOUNT = "Invalid Amount. Please enter a positive number."
INSUFFICIENT_FUNDS = "Insufficient funds to complete the withdrawal"

def show_balance(balance):
    print(f"**************************\nYour balance is ${balance:.2f}\n**************************")

def deposit(balance, transactions):
    try:
        amount = float(input("Enter an amount to be deposited: "))
        if amount <= 0:
            print(INVALID_AMOUNT)
            return balance
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} has been deposited.")
        return balance
    except ValueError:
        print(INVALID_AMOUNT)
        return balance


def withdraw(balance, transactions):
    try:
        amount = float(input("Enter the amount to be withdrawn: "))
        if amount <= 0:
            print(INVALID_AMOUNT)
        elif amount > balance:
            print(INSUFFICIENT_FUNDS)
        else:
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} has been withdrawn.")
        return balance
    except ValueError:
        print(INVALID_AMOUNT)
        return balance

def view_transactions(transactions):
    print("**************************\nTransaction History")
    if not transactions:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction}")
    print("**************************")

def main():
    balance = 0.0
    transactions = []
    while True:
        print(MENU)
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance, transactions)
        elif choice == "3":
            balance = withdraw(balance, transactions)
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            print("**************************\nThank you! Have a nice day.\n**************************")
            break
        else:
            print(INVALID_CHOICE)

if __name__ == '__main__':
    main()
