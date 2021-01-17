class Restaurant:
    """
    A class to describe a restaurant.
    """

    def __init__(self, name, cuisine):
        """Initialize the restaurant attributes."""
        self.restaurant_name = name.title()
        self.cuisine_type = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant by it's name and cuisine type."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Sets the number of served items."""
        print(f"Setting served dishes to {number}")
        self.number_served = number

    def increment_number_served(self, add_served):
        """Increments the number of served items."""
        print(f"Incrementing served dishes by {add_served}")
        self.number_served += add_served

    def show_number_served(self):
        """Tells user the numbers served"""
        print(f"We served {self.number_served} customers.")


class IceCreamStand(Restaurant):
    """Describe Ice Cream specific stuff. Yummy! :D"""

    def __init__(self, name, cuisine):
        """Initialize attributes"""
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):
        """Prints a selection of all Ice Cream flavors."""
        print(f"They offer the following Ice Cream flavors:")
        for flavor in self.flavors:
            print(f" -" + flavor.title())