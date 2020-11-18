# Requesting and stripping forname
print("Hallo, wie ist dein Vorname?")
first_name = input()
first_name = first_name.strip().title()

# Requesting and stripping surname
print("Und dein Nachname?")
last_name = input()
last_name = last_name.strip().title()

# Putting full_name together
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name}!"

# Print adjusted name
print(message)