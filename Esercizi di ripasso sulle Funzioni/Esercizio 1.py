#Esercizio 1
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        
        if value == valore:
            return key

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))