#Esercizio 3
def funzione3 (dict3: dict[str, int | float]) -> dict:
    dict_new:dict = {}

    for key, value in dict3.items():
        if value < 50:
            value *= 1.10
            x = round(value, 2)
            dict_new[key] = x
        

    return dict_new
        

