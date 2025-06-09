#Esercizio 5
def funzione5 (list4:list[int]) -> int:
    
    list4: list =[]
    threshold : int = 100
    risultato = 1

    for i in list4:
        if i < threshold:
            risultato *= i

    return risultato





    