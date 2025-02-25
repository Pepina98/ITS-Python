#Esercizio 5
print("Costo barretta di cioccolato: 1.00 euro")
n:int = int(input("Inserire il numero di euro disponibili:"))

sconto:int = 0
somma_barrette:int = 0

while n > 0:
    somma_barrette += 1
    sconto += 1
    
    if sconto == 6:
        sconto = 0
        somma_barrette += 1
    
    n -= 1 
    
print(f"Il numero totale di barrette è:{somma_barrette}\nI buoni sconto inutilizzati sono: {sconto}")