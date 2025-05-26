#Esercizio 2 
def stipendio (ore:int) -> float:
    if ore <= 40:
        x:float = (ore * 10)
        return x
    
    else:
        y: float = ((ore - 40) * (10 * 1.5))+ 400
        return y
    
print(stipendio(35))


    