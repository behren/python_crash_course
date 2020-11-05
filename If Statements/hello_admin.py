users = ['admin', 'nick', 'ragemoody', 'sonken', 'xakdude']

if users:
    for user in users:
        if user == 'admin':
            print("Hey admin, welcome back!")
        else:
            print(f"Hey {user}!")
else:
    print("We need to get more users!")