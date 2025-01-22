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
    pass

if __name__ == "__main__":
    main()