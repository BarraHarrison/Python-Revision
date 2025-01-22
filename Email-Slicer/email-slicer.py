# Email slicer program

def email_slicer():
    print("Welcome to the email slicer program!")

    while True:
        email = input("Enter your email or type 'exit' to quit the program: ").strip()

        if email.lower() == "exit":
            print("Thank you for using the email slicer program. Bye Bye!")
            break

        if "@" not in email or email.count("@") != 1:
            print("Invalid email address. Please try again.")
            continue

if __name__ == "__main__":
    email_slicer()