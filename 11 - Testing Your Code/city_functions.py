def get_city_country(city, country, population=""):
    if population:
        full_location = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_location = f"{city.title()}, {country.title()}"
    return full_location