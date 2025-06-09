#Esercizio 1
def funzione1 (list1, dict1, value, key):
    list1 : list = []
    dict1 : dict = {}
    
    for i in list1:
        key, value = i[0], i[1]
        if key in dict1:
            dict1[key] =+ value 
        else:
            dict1[key] = value
    
    return dict1
        

            

    