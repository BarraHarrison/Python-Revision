# Email slicer program
# The email slcier program has been refactored and enhanced since I created the file in December

def welcome_message():
    print("Welcome to the email slicer program")
    print("You can analyze emails, view statistics and more.")
    print("Type 'exit' at any time to quit the program.")


def slice_email(email):
    """Slices the email into the username and the domain"""
    try:
        if "@" not in email or email.count("@") != 1:
            raise ValueError("Invalid email address.")

        username, domain = email.split("@")
        if not username or not domain:
            raise ValueError("Incomplete email address.")
        
        return username, domain
    except ValueError as error:
        return None, str(error)



def email_statistics(email):
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
    welcome_message()

    while True:
        email = input("Enter your email or type 'exit' to quit: ").strip()

        if email.lower() == "exit":
            print("Thank you for using the email slicer program. Bye Bye!")
            break

        username, domain = slice_email(email)

        if username:
            print(f"Your username is '{username}' and the domain is '{domain}'.")
            stats = email_statistics(email)
            print("Email Statistics:")
            print(f"- Username Length: {stats['username_length']} characters")
            print(f"- Domain Length: {stats['domain_length']} characters")
            print(f"- Total Email Length: {stats['total_length']} characters")
        else:
            print(f"Error: {domain}. Please provide a valid email address.")

if __name__ == "__main__":
    main()