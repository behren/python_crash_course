def city_country(city, country):
    return(city.title() + ", " + country.title())

city = city_country('mölln', 'germany')
print(city)

city = city_country(country='japan', city='tokyo')
print(city)

print(city_country('hamburg', 'germany'))