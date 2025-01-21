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

def deposit(balance):
   try:
       pass
   except:
       pass


def withdraw(balance):
    print("**************************")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("**************************")

    if amount > balance:
        print("**************************")
        print("Insufficient funds")
        print("**************************")
    elif amount < 0:
        print("**************************")
        print("Amount must be greater than 0")
        print("**************************")
    else:
        balance -= amount
        print("**************************")
        print(f"${amount:.2f} has been withdrawn.")
        print("**************************")
    return balance

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**************************")
        print("      Banking Program     ")
        print("**************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**************************")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("**************************")
            print("That is not a valid choice")
            print("**************************")

    print("**************************")
    print("Thank you! Have a nice day")
    print("**************************")

if __name__ == '__main__':
    main()
