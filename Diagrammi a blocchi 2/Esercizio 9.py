#Esercizio 9
i = 0
numeri_divisibili = 0

n:int = int(input("Inserire un numero intero e positivo:"))



if n > 0:
    while True:
        if n % 1 == 0:
            break
        else:
            print("Il numero deve essere intero e positivo")
            n:int = int(input("Inserire un numero intero e positivo:"))

    while i < 10 :
        numeri_interi:int = int(input("Inserire 10 numeri interi:"))
        i += 1
        if numeri_interi % n == 0 : 
            numeri_divisibili += 1
        else:
            print("Il numero non è divisibile per il valore iniziale inserito")

    print(f"I numeri divisibili per il valore inserito all'inizio sono:{numeri_divisibili}")
else: 
    print ("Il numero inserito non è positivo o intero")