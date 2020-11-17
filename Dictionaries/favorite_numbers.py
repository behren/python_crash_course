favorite_numbers = {
    "nicole": ["7", "6", "5"],
    "chris": ["99", "14"],
    "sönke": ["2", "1000"],
    "mike": ["304", "8080"],
    "niclas": ["9", "09", "909"],
}

for name, numbers in favorite_numbers.items():
    print(f"\nDie Lieblingszahlen von {name.title()} sind:")
    for number in numbers:
        print(number)