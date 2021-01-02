def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    print("\nWe are sending the following messages: ")

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)