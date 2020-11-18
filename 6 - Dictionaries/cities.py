cities = {
    "hamburg": {
        "country": "germany",
        "population": "2 million",
        "area": "755,2 km²",
    },
    "amsterdam": {
        "country": "netherlands",
        "population": "1 million",
        "area": "219,3 km²",
    },
    "london": {
        "country": "united kingdom",
        "population": "9 million",
        "area": "1.572 km²",
    },
}

for city, info in cities.items():
    print(
        f"{city.title()} is located in {info['country'].title()}, "
        f"has a population of {info['population'].title()} and "
        f"spans an area of {info['area'].title()}."
    )
