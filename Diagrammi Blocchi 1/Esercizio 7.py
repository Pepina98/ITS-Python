#Esercizio 7
pari = 0
dispari = 0 
i = 0

while i < 10:
    n:int = int(input("Inserisci 10 numeri:"))

    if n%2 == 0:
        pari += 1
       

    else:
        dispari += 1
        
    i += 1

print(f"Il numero dei pari è: {pari}")
print(f"Il numero dei dispari è: {dispari}")