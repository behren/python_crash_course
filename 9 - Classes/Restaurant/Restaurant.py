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
        self.number_served = number

    def increment_number_served(self, add_served):
        """Increments the number of served items."""
        self.number_served += add_served


restaurant = Restaurant("McDonalds", "fastfood")
restaurant.describe_restaurant()
print(f"Numbers served: {restaurant.number_served}.")
restaurant.open_restaurant()
restaurant.number_served = 42
print(f"Numbers served: {restaurant.number_served}.")
restaurant.set_number_served(1337)
print(f"Numbers served: {restaurant.number_served}.")
restaurant.increment_number_served(420_000)
print(f"Numbers served: {restaurant.number_served}.")