def sandwiches(*items):

    print("We are making you a sandwich with the following ingredients:")

    for ingredient in items:
        title_ingredient = ingredient.title()
        print(f"{title_ingredient}")

sandwiches('salami','cheese','pepperoni')