def car_description(manufacturer, model, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model
    return car_information

car = car_description('mercedes', 'c63s', color='white', engine='v8')

print(car)