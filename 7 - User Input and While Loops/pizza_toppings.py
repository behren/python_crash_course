prompt = "\nPlease tell me your favorite Pizza toppings:"
prompt += "\n(Enter 'quit' when you're finished.)\n"

active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"I will add {topping.title()} to your Pizza!")