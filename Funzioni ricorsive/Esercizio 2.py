#Esercizio 2
def sum(n:int) -> int:
    if n < 0:
        print("Errore! Inserted number is negative!")
    
        return None

    else:
        somma:int = 0
        while n:
            somma += n
            n -= 1
        
        return int(somma)

print(sum(5))