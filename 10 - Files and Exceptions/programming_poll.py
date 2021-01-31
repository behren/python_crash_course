filename = "data/poll_results.txt"
prompt = "Welcome to our poll. Please tell us why you like programming."
prompt += "Enter 'q' or 'exit' to leave."

active = True

while active:
    reason = input(prompt)

    if reason == "q" or reason == "exit":
        active = False
    else:
        with open(filename, "a") as poll_results:
            poll_results.write(f"{reason}\n")