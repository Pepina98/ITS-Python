#ESercizio 6
i = 1
fattoriale = 1

while True:
    n:int = int(input("Inserisci un numero intero e positivo:"))
    
    if n < 0:
        print("Il numero deve essere positivo")

    else:
        break

while i <= n:
    fattoriale = fattoriale * i 
    i += 1

print(fattoriale)
