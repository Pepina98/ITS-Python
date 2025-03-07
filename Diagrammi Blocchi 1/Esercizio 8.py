#Esercizio 8
i = 0
soglia:int = int(input("Inserisci un valore che sarà il tuo valore soglia:"))

while i < 7:
    
    n:int = int(input ("Inserisci un valore:"))

    if n > soglia:
        print(f"Il valore inserito dall'utente {n} è maggiore del valore soglia {soglia}")

    i +=1
    