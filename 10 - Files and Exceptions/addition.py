print("Welcome to my program. This will calculate the sum of two numbers.")
print("Press 'q' at any time to exit.")

active = False

while not active:
    number1 = input("Please enter the first number: ")
    if number1 == "q":
        print("Goodbye!")
        break
    number2 = input("Please enter the second number: ")
    if number2 == "q":
        print("Goodbye!")
        break
    try:
        number3 = int(number1) + int(number2)
    except:
        ValueError(print("Please enter numbers instead of text."))
    else:
        print(f"The sum of {number1} and {number2} is {number3}")
