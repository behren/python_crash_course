pizzas = ['salami', 'hawaii', 'san siro', 'pepperoni', 'tonno']


for pizza in pizzas:
    print(f"Ich mag {pizza.title()} Pizza")

print("Pizza is the best!")


print("The first three items in the list are:")
print(pizzas[0:3])

print("Three items from the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the list are:")
print(pizzas[2:5])

friend_pizzas = pizzas[:]

pizzas.append("funghi")
friend_pizzas.append("margherita")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza}")

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"{pizza}")