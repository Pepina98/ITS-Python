#Esercizio 5
somma=0
i = 1
n:int = int(input("Inserisci un numero intero e positivo:"))

if n%1 == 0 and n>0:
   while True:
    if i<n:
         somma = somma + (i*i)
         i += 1
    else:
       print(f"La somma è {somma}")
       break

else:
   print("Errore, il numero inserito deve essere positivo") 


      
    
