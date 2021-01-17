from user import User


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