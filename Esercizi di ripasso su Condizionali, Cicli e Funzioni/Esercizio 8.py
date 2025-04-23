#Esercizio 8
def seconds_since_noon (ore:int, minuti:int, secondi:int) -> int:
    if ore >= 0 and ore <= 12:
        x = ore * 3600
        
    if minuti >= 0 and minuti <= 59:
        y = minuti * 60
        
    if secondi >= 0 and secondi <= 59:
        z = secondi 
        
    i = x + y + z 
    return i 

print(seconds_since_noon(3, 15, 30))

def time_difference(ore:int, minuti:int, secondi:int, ore1:int, minuti1:int, secondi1:int) ->int:
    j = seconds_since_noon(ore, minuti, secondi)
    e = seconds_since_noon(ore1, minuti1, secondi1)

    difference = abs(j - e)
    return difference

    

