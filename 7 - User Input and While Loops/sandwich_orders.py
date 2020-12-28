sandwich_orders = [
    "salami",
    "pastrami",
    "pastrami",
    "pastrami",
    "hawaii",
    "diavolo",
    "chicken",
]

finished_sandwiches = []

print("Unfortunately we have run out of Pastrami. :(\n")

for pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich.title()} sandwich.")
    finished_sandwiches.append(sandwich)


print("\nThe following sandwiches are finished:")
sandwiches = [s.title() for s in finished_sandwiches]
print(*sandwiches, sep=", ")