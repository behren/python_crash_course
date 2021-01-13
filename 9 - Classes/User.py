class User:
    """
    Describes and greets a user.
    """

    def __init__(self, first, last, age, location):
        """Initialize user attributes."""
        self.first_name = first.title()
        self.last_name = last.title()
        self.age = age
        self.location = location.title()
        self.login_attempts = 0

    def greet_user(self):
        """Greets the user by name."""
        msg = (
            f"Hello, {self.first_name} {self.last_name}, how are you? Here"
            f" is a summary of what we know about you:"
        )
        print(msg)

    def describe_user(self):
        """Describes the user with all attributes."""
        summary = (
            f"Your name is {self.first_name} {self.last_name}, you are"
            f" {self.age} years old and located in {self.location}."
        )
        print(summary)

    def increment_login_attempts(self):
        """Increments the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts back to 0."""
        self.login_attempts = 0


class Privileges:
    """Shows user privileges"""

    def __init__(self, privileges=[]):
        """Initialize attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """Shows the admin privileges"""
        print("\nYou do have the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- " + privilege.title())
        else:
            print("This user has no privileges.")


class Admin(User):
    """
    Describes admin users.
    """

    def __init__(self, first, last, age, location):
        """Initialize attributes"""
        super().__init__(first, last, age, location)
        self.privileges = Privileges()


me = Admin("Niclas", "Behrendt", "30", "hamburg")

me.privileges.privileges = ["create user", "delete user", "ban user", "restore user"]

me.greet_user()
me.describe_user()

me.privileges.show_privileges()