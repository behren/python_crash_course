import json

prompt = "Hello, please type in your favorite number."
prompt += "We will make sure to remember it for you!\n"
filename = "10 - Files and Exceptions\\data\\favorite_number.json"

try:
    with open(filename) as f:
        favoriteNumber = json.load(f)
    print(f"We remembered your favorite number! It's {favoriteNumber}.")
except FileNotFoundError:
    favoriteNumber = input(prompt)
    with open(filename, "w") as f:
        json.dump(favoriteNumber, f)