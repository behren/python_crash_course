class User:
    """
    Describes and greets a user.
    """
    def __init__ (self, first, last, age, location):
        """Initialize user attributes."""
        self.first_name = first.title()
        self.last_name = last.title()
        self.age = age
        self.location = location.title()

    def greet_user(self):
        """Greets the user by name."""
        msg = f"Hello, {self.first_name} {self.last_name}, how are you? Here" \
              f" is a summary of what we know about you:"
        print(msg)

    def describe_user(self):
        """Describes the user with all attributes."""
        summary = f"Your name is {self.first_name} {self.last_name}, you are" \
                    f" {self.age} years old and located in {self.location}."
        print(summary)

me = User('Niclas', 'Behrendt', '30', 'hamburg')
me.greet_user()
me.describe_user()