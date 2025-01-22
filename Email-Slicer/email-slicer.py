# Email slicer program
# The email slcier program has been refactored and enhanced since I created the file in December

def welcome_message():
    print("Welcome to the email slicer program")
    print("You can analyze emails, view statistics and more.")
    print("Type 'exit' at any time to quit the program.")


def slice_email():
    print("Welcome to the email slicer program!")

    while True:
        email = input("Enter your email or type 'exit' to quit the program: ").strip()

        if email.lower() == "exit":
            print("Thank you for using the email slicer program. Bye Bye!")
            break

        if "@" not in email or email.count("@") != 1:
            print("Invalid email address. Please try again.")
            continue

        try:
            username, domain = email.split("@")
            if not username or not domain:
                raise ValueError("Incomplete email address.")
            print(f"Your username is {username} and the domain is {domain}.")
        except ValueError as error:
            print(f"Error: {error}. Please provide a valid email address.")

def email_statistics():
    """Provides statistics about the email."""
    username, domain = slice_email(email)
    if username:
        return {
            "username_length": len(username),
            "domain_length": len(domain),
            "total_length": len(email)
        }
    return {}

def main():
    pass

if __name__ == "__main__":
    main()