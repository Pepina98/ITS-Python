#Esercizio 2
def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    dizionario1= {}
    
    for key, value in dizionario.items():
        if value not in dizionario1.keys():
            dizionario1[value]= key
        else:
            continue
        
                
            

        
        
    return dizionario1
print(inverti_mappa({'a': 1, 'b': 1, 'c': 3}))    
        