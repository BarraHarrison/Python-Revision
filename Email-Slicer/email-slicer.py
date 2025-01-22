# Email slicer program
# The email slcier program has been refactored and enhanced since I created the file in December

def welcome_message():
    print("Welcome to the email slicer program")
    print("You can analyze emails, view statistics and more.")
    print("Type 'exit' at any time to quit the program.")


def slice_email():
    """Slices the email into the username and the domain"""
    try:
        pass
    except:
        pass



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