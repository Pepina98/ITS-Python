#Esercizio 3
somma:float = 0


for i in range (5):
    numeri:float = float(input("Inserisci un valore:"))
    if numeri > 0:
        somma += numeri 

print(f"La somma è:{somma}")
