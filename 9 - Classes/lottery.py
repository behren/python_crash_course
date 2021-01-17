"""A class trying to emulate a lottery ticket"""

from random import choice


class Lottery:
    def __init__(self, possibilities):
        """initalizing attributes"""
        self.values = possibilities

    def draw_ticket(self):
        """Draw a ticket and add the value if it's no duplicate."""
        results = []
        while len(results) < 4:
            value = choice(self.values)
            if value not in results:
                results.append(value)
        return results

    def check_ticket(self, your_ticket, winning_ticket):
        for element in your_ticket:
            if element not in winning_ticket:
                return False
        return True