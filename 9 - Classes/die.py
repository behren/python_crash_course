"""A die with a default value of 6 sides."""
from random import randint


class Die:
    """A simple Die with 6 sides."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Let's get it rollin'"""
        return randint(1, self.sides)