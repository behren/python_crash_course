prompt = "\nPlease tell me your favorite Pizza toppings:"
prompt += "\n(Enter 'quit' when you're finished.)\n"

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"I will add {topping.title()} to your Pizza! :)")