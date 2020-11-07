rivers = {'egypt': 'nile', 'germany': 'elbe', 'usa': 'mississippi'}

for country, river in rivers.items():
    if country == 'usa':
        country = f'the {country.upper()}'
    else:
        country = country.title()
    print(f"The {river.title()} runs through {country}")

for country in rivers.keys():
    print(country)

for river in rivers.values():
    print(river)