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


me = User("Niclas", "Behrendt", "30", "hamburg")
me.greet_user()
me.describe_user()
print(f"Login attempts: {me.login_attempts}")
me.increment_login_attempts()
print(f"Login attempts: {me.login_attempts}")
me.increment_login_attempts()
print(f"Login attempts: {me.login_attempts}")
me.increment_login_attempts()
print(f"Login attempts: {me.login_attempts}")
me.increment_login_attempts()
print(f"Login attempts: {me.login_attempts}")
me.reset_login_attempts()
print(f"Login attempts: {me.login_attempts}")