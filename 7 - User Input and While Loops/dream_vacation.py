destinations = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("What is your dream destination for a vacation?\n")

    destinations[name] = response

    repeat = input("Do you want another person to take the poll?\n")
    if repeat == "no":
        polling_active = False

print("--- Poll Results ---")
for name, response in destinations.items():
    print(f"{name.title()}'s dream destination is {response.title()}.")
