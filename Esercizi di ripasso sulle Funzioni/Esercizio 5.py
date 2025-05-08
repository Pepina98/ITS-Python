#Esercizio 5
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    prodotti1 = {}
    for key,value in prodotti.items():
        if value > 20:
            a = abs(((value * 10) / 100) - value)
            prodotti1[key] = a
            
        else:
            continue
            
    




    return prodotti1








print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))