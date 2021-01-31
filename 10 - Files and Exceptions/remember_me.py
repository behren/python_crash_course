import json


def get_stored_username():
    """Get stored username if available"""
    filename = "10 - Files and Exceptions\\data\\username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Get a new username"""
    username = input("What is your username?\n")
    filename = "10 - Files and Exceptions\\data\\username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    print(f"We will remember you {username}!")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify_user()
    else:
        get_new_username()


def verify_user():
    """Verify that it's the right user."""
    username = get_stored_username()
    reply = str(input(f"Are you {username}?" + " (y/n): ")).lower().strip()
    if reply == "y" or reply == "yes":
        print(f"Welcome back {username}!")
    elif reply == "n" or reply == "no":
        get_new_username()
    else:
        print("Please enter yes or no.")
        verify_user()


greet_user()