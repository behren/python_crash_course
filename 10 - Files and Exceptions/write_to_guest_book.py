filename = "data/guestbook.txt"
prompt = "Please add your name to our Guest Book."
prompt += "Enter 'q' or 'exit' to leave."

active = True

while active:
    name = input(prompt)

    if name == "q" or name == "exit":
        active = False
    else:
        print(f"Hello {name}, welcome to our Hotel!")
        with open(filename, "a") as guestbook:
            guestbook.write(f"{name}\n")