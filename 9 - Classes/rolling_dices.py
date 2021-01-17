from die import Die

# 6 sided Die here:
d6 = Die()

results = []

for r in range(10):
    result = d6.roll_die()
    results.append(result)
print("Results of 10 dice rolls:")
print(results)

# 10 sided Die here:
d10 = Die(10)

results = []

for r in range(10):
    result = d10.roll_die()
    results.append(result)
print("Results of 10 dice rolls:")
print(results)

# 20 sided Die here:
d20 = Die(20)

results = []

for r in range(10):
    result = d20.roll_die()
    results.append(result)
print("Results of 10 dice rolls:")
print(results)