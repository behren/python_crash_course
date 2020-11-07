favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

persons = ["nicole", "sarah", "phil", "niclas", "chris"]

for name in persons:
    print(f"Hi {name.title()}")

    if name in favorite_languages.keys():
        print(f"Thank you, but you have already taken the poll.")
    else:
        print(f"Welcome, please take the poll.")

for person in persons:
    if person in favorite_languages:
        print(f"Hi {person.title()}, please take the poll.")
    else:
        print(f"Hi {person.title}, thank you but you have already taken the poll.")