#Esercizio 3
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    count = 0
    for i in lista:
        for key, value in da_rimuovere.items():
            if i == key:
                lista.remove(i) 
                count += 1

            if count == value:
                break 
        if count == value:
            break
    return lista
    
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))