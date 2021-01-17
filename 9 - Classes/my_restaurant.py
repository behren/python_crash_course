import restaurant


restaurant = restaurant.IceCreamStand("McDonalds", "Fast Food")
restaurant.flavors = ["vanilla", "chocolate", "strawberry"]
restaurant.describe_restaurant()
restaurant.show_flavors()
restaurant.set_number_served(300)
restaurant.show_number_served()
restaurant.increment_number_served(700)
restaurant.show_number_served()