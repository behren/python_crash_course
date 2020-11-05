current_users = ['admin', 'nick', 'ragemoody', 'sonken', 'xakdude']

new_users= ['rAgeMooDY', 'michab62', 'user42', 'sonken', 'frodo']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, username {user} already taken. Please chose another one")
    else:
        print(f"Username {user} is available!")