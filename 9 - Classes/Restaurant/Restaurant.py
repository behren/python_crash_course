class Restaurant:
    """
    A class to describe a restaurant.
    """
    
    def __init__(self, name, cuisine):
        """Initialize the restaurant attributes."""
        self.restaurant_name = name.title()
        self.cuisine_type = cuisine.title()

    def describe_restaurant(self):
        """Describe the restaurant by it's name and cuisine type."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant('McDonalds', 'fastfood')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('Bullerei', 'star cook')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Lavastein', 'italian')
restaurant3.describe_restaurant()