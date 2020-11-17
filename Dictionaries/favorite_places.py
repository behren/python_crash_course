favorite_places = {
    "nicole": ["london", "prague"],
    "niclas": ["amsterdam", "dresden", "paris"],
    "sönke": ["zuhause"],
}

for name, locations in favorite_places.items():
    if len(locations) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    for location in locations:
        print(f"{location.title()}")