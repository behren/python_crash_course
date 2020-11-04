numbers = list(range(3,31,3))
print(numbers)


for number in numbers:
    print(number**3)


numbers_comprehension = [value ** 3 for value in range(3,30)]
for number in numbers_comprehension:
    print(number)