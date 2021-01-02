from message_functions import *

messages = ["Hello", "How are you?", "Goodbye"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)