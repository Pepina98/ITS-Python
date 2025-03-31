#Esercizio 10
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
    for key in dict2:
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]

        else:
            dict1[key]=dict2[key]

        return dict1

dict1= {"a": 1,"b": 2,"c": 3}
dict2 = {"c" : 2, "d" : 4}

print((merge_dictionaries)(dict1, dict2))
    
