filename = "guest.txt"

print("Please tell us your name")
guest = input()

with open(filename, "w") as guest_file:
    guest_file.write(guest)