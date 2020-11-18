print("Welcome to our Restaurant, what's the size of your group?")
group_size = input()
group_size = int(group_size)

if group_size > 8:
    print("Unfortunately you'll have to wait for a table.")
else:
    print("Okay, please follow me. I'll escort you to your table.")