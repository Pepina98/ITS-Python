#Esercizio 2
def funzione2(list2: list[int|float]) -> dict:
    
    dict2:dict[str, list[int|float]]= {"positivi" : [], "negativi": []}
    

    for i in list2 :
        
        if i >= 0:
            
            dict2["positivi"].append(i)
        
        else:
            
            dict2["negativi"].append(i)
    
    return dict2




    



        


    
    
