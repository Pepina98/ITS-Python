#Esercizio 8-14
i = 0

def information_car (name:str, model:str, **kwargs):
    car:dict = {"name_car": name, "model_car": model, **kwargs}
    print(kwargs)
    
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    while i < 3:
        car["key"] = value
        if i > 3:
            print("Non è possibile selezionare nuove informazioni")

        else:
            print(car)

    


    


