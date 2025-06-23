def car_information(manufacture:str, model:str, **kwargs) ->dict:
    make_car:dict = {}

    make_car["manufacture"] = manufacture
    make_car["model"] = model

    for key,value in kwargs.items():
        make_car[key] = value

    return make_car

print(car_information('subaru', 'outback', color='blue', tow_package=True))
