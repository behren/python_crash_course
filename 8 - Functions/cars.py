def car_description(manufacturer, model, **car_information):
    car_dict = {'Manufacturer': manufacturer.title(),
                'Model': model.title()}

    for information, value in car_information.items():
        car_dict[information] = value

    return car_dict


car = car_description('mercedes', 'c63s', color='white', engine='v8')

print(car)