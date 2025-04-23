#Esercizio 3
def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        ore_lavorate = ore_lavorate * 10
        return ore_lavorate

    elif ore_lavorate > 40:
        ore_lavorate = (40 * 10) + (ore_lavorate - 40)* 15 

    return ore_lavorate

