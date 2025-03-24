#Esercizio 15
n:int = int(input("Inserire un valore intero:"))

somma_pari = 0
somma_dispari = 0
i = 1

if n >=1 and n <= 100:
    while i < n:
        if i % 2 == 0:
            somma_pari += i 
            i += 1
print(f"La somma dei numeri pari è:{somma_pari}")
            

elif n < 0 and n ==0:
    print("Errore")
            
else:
    while i < n:
           if i % 2 =! 0: 
                somma_dispari += i
                i += 1
print(f"La somma dei numeri dispari è:{somma_dispari}")